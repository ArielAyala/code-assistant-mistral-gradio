import os
import logging
import gradio as gr
from mistralai import Mistral
from dotenv import load_dotenv
from typing import Optional, List, Dict

# Load environment variables
load_dotenv()

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constant for the model name
MODEL_NAME = "codestral-mamba-latest"

def get_api_key() -> str:
    """
    Retrieves the API key from environment variables.
    Raises an exception if the key is not found.
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        logging.error("MISTRAL_API_KEY environment variable not found.")
        raise ValueError("API key not found. Please set the MISTRAL_API_KEY environment variable.")
    return api_key

def create_mistral_client(api_key: str) -> Mistral:
    """
    Creates a Mistral client using the provided API key.
    """
    try:
        return Mistral(api_key=api_key)
    except ValueError as ve:
        logging.error(f"Invalid API key provided: {ve}")
        raise
    except Exception as e:
        logging.error(f"Failed to create Mistral client: {e}")
        raise

def get_chat_response(client: Mistral, conversation_history: List[Dict[str, str]], user_input: str, model: Optional[str] = MODEL_NAME) -> str:
    """
    Gets a response from the Mistral chatbot model.
    """
    try:
        conversation_history.append({"role": "user", "content": user_input})
        chat_response = client.chat.complete(model=model, messages=conversation_history)
        response_content = chat_response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": response_content})
        return response_content
    except KeyError as ke:
        logging.error(f"Unexpected response format: {ke}")
        return "An error occurred while processing the response, please try again later."
    except Exception as e:
        logging.error(f"Error interacting with the Mistral API: {e}")
        return "An error occurred while interacting with the Mistral API. Please try again later."

def update_conversation(user_input: str, history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Manages the conversation by updating the history and fetching the response.
    """
    try:
        api_key = get_api_key()
        client = create_mistral_client(api_key)
        get_chat_response(client, history, user_input)  # Updates the history in place
        return history
    except ValueError as ve:
        logging.error(f"Configuration error: {ve}")
        return [{"role": "assistant", "content": "Configuration error. Please check your API key settings."}]
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return [{"role": "assistant", "content": "An unexpected error occurred, please try again later."}]

def create_gradio_interface() -> None:
    """
    Creates and launches the Gradio user interface.
    Allows users to interact with the Mistral chatbot through a simple GUI.
    """
    conversation_history = gr.State([])

    def chatbot_response(user_input: str, conversation_history: List[Dict[str, str]]) -> List[Dict[str, str]]:
        updated_history = update_conversation(user_input, conversation_history)
        response_text = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in updated_history])
        return response_text, updated_history

    ui = gr.Interface(
        fn=chatbot_response,
        inputs=[gr.Textbox(label="Enter your message"), conversation_history],
        outputs=[gr.Markdown(label="Chatbot response"), gr.State()],
        title="Mistral Coding Assistant",
        description="A chatbot that helps with coding tasks.",
        examples=[
            ["What is the syntax for a for loop in Python?"],
            ["How do I create a new list in Python?"],
        ],
        allow_flagging="never",
    )

    # Check the environment to decide how to launch
    env = os.environ.get("ENV", "development")  # Default to 'development'

    if env == "production":
        ui.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 8080)))
    elif env == "docker":
        ui.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))  # Default Docker port
    else:
        ui.launch()  # Defaults for development

if __name__ == "__main__":
    create_gradio_interface()
