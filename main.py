import os
import logging
import gradio as gr
from mistralai import Mistral
from dotenv import load_dotenv
from typing import Optional

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

def get_chat_response(client: Mistral, user_input: str, model: Optional[str] = MODEL_NAME) -> str:
    """
    Gets a response from the Mistral chatbot model.
    """
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ]
        )
        return chat_response.choices[0].message.content
    except KeyError as ke:
        logging.error(f"Unexpected response format: {ke}")
        return "An error occurred while processing the response, please try again later."
    except Exception as e:
        logging.error(f"Error interacting with the Mistral API: {e}")
        return "An error occurred while interacting with the Mistral API. Please try again later."

def chat_with_mistral(user_input: str) -> str:
    """
    Facilitates the interaction with Mistral using user input.
    """
    try:
        api_key = get_api_key()
        client = create_mistral_client(api_key)
        return get_chat_response(client, user_input)
    except ValueError as ve:
        logging.error(f"Configuration error: {ve}")
        return "Configuration error. Please check your API key settings."
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "An unexpected error occurred, please try again later."

def create_gradio_interface() -> None:
    """
    Creates and launches the Gradio user interface.
    Allows users to interact with the Mistral chatbot through a simple GUI.
    """
    ui = gr.Interface(
        fn=chat_with_mistral,
        inputs=gr.Textbox(label="Enter your message"),
        outputs=gr.Markdown(label="Chatbot response"),
        title="Mistral Coding Assistant",
        description="A chatbot that helps with coding tasks.",
        examples=[
            ["What is the syntax for a for loop in Python?"],
            ["How do I create a new list in Python?"],
        ],
        allow_flagging="never",
    )
    ui.launch()

if __name__ == "__main__":
    create_gradio_interface()