# Ollama Streamlit Demo with Gemma

A simple Streamlit application that demonstrates the integration of Langchain with the Gemma language model through Ollama.

## Overview

This application provides a web interface where users can input questions and receive responses from the Gemma 2B model. It uses Langchain for prompt management and chain orchestration, and Streamlit for the web interface.

## Prerequisites

- Python 3.8 or higher
- Ollama installed on your system
- Gemma 2B model pulled in Ollama

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akshada2712/Gemma-AI-Assistant-LangChain-Demo.git
cd Ollama_basics
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages using requirements.txt:
```bash
pip install -r requirements.txt
```

4. Set up your `.env` file with the following variables:
```
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
```

## Project Structure

```
Ollama_basics/
├── app.py          # Main application file
├── .env           # Environment variables
├── requirements.txt # Package dependencies
└── README.md      # This file
```

## Running the Application

To run the application, navigate to the project directory and execute:

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501` by default.

## Features

- Simple web interface for question-answering
- Integration with Gemma 2B model through Ollama
- Langchain for prompt management
- Langsmith tracking capabilities

## Code Components

- **Environment Setup**: Uses `python-dotenv` for environment variable management
- **Langsmith Integration**: Configures Langchain tracking
- **Prompt Template**: Defines a system and user message template
- **Model Configuration**: Uses the Gemma 2B model through Ollama
- **Web Interface**: Streamlit-based user interface for interaction

## Environment Variables

The following environment variables need to be set in your `.env` file:

- `LANGCHAIN_API_KEY`: Your Langchain API key for tracking
- `LANGCHAIN_PROJECT`: Your Langchain project name

## Usage

1. Start the application using the command mentioned above
2. Enter your question in the text input field
3. The response from the Gemma model will be displayed below the input field

## Notes

- Make sure Ollama is running on your system before starting the application
- Ensure you have pulled the Gemma 2B model in Ollama using: `ollama pull gemma:2b`
- The application uses Langsmith tracking, which requires a valid API key

## Troubleshooting

If you encounter any issues:

1. Verify Ollama is running
2. Ensure all environment variables are properly set
3. Check that all required packages are installed
4. Verify the Gemma model is properly pulled in Ollama
