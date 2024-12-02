![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF9900?style=for-the-badge&logo=gradio&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Mistral](https://img.shields.io/badge/Mistral%20AI-0078D4?style=for-the-badge&logo=azuredevops&logoColor=white)
![dotenv](https://img.shields.io/badge/dotenv-00C853?style=for-the-badge&logo=python&logoColor=white)

# Code Assistant with Mistral and Gradio

<div align="center">
  <img src="preview.jpg" width="500" height="auto">
</div>

## Project Description

This project is a coding assistant chatbot powered by Mistral AI and hosted on a Gradio interface. The assistant helps developers with coding-related queries, providing clear and concise answers. It is implemented using **Python** and integrates **Gradio** for the user interface, and **Mistral AI** for natural language understanding.

The application can run locally or using Docker.

- Interactive coding assistant chatbot.
- Powered by Mistral AI for natural language responses.
- Gradio-based user-friendly interface.
- Runs locally or inside a Docker container.

## Technologies Used

- **Python**
- **Gradio**
- **Mistral AI**
- **Docker**
- **Python-dotenv**

## Installation

### Clone the repository:
```bash
git clone https://github.com/ArielAyala/code-assistant-mistral-gradio.git
```

### Navigate to the project directory:
```
cd code-assistant-mistral-gradio
```

### Create a virtual environment:
```
python -m venv venv
```
### Activate the virtual environment:
Windows: ```venv\Scripts\activate```

Linux/macOS: ```source venv/bin/activate```

### Install the dependencies:
```
pip install -r requirements.txt
```

### Run the app locally:
```
python main.py
```

## Deployment
## Run with Docker:
This project includes a ```Dockerfile```, ```docker-compose.yml```, and ```.dockerignore``` file to simplify containerization.
1. Build and run the Docker container:
```
docker-compose up --build
```
2. Access the app: Open http://localhost:7860 in your browser.

### Preview:
You can interact with the chatbot on this Gradio interface:

[Live Demo](https://code-assistant-mistral-gradio.onrender.com)

<div align="center"> <img src="assets\example_uit.jpg" width="700" height="auto"> </div>

<div align="center"> <img src="assets\example_chat.jpg" width="700" height="auto"> </div>

### Environment Variables

To use the Mistral AI API, you need to provide your API key in a .env file at the root of the project:

```
MISTRAL_API_KEY=your_api_key_here
```

_Note: Never expose your API key in public repositories._


### Contributions
Feel free to contribute to this project by submitting issues or pull requests. Your feedback is welcome!


### License
This project is licensed under the MIT License. See the LICENSE file for details
