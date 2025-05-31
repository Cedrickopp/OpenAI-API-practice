# OpenAI API Practice Project

This project serves as a learning ground for exploring and understanding the OpenAI API, specifically focusing on the GPT-3.5 Turbo model. It demonstrates basic concepts of API integration, conversation management, and response handling.

## Project Overview

The project implements a simple travel guide chatbot that provides information about Darmstadt, Germany. It showcases:
- Basic OpenAI API integration
- Conversation management
- System prompt implementation
- Response handling
- Environment variable usage

## Project Structure

```
openai-api-practice/
├── main.py              # Main entry point
├── functions.py         # Core functionality and API calls
├── system_prompt.py     # System prompt definition
├── user_prompts.py      # User questions and prompts
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Features

- Integration with OpenAI's GPT-3.5 Turbo model
- Structured conversation management
- Environment variable handling for API keys
- Modular code structure for easy expansion
- Pre-defined Q&A format for consistent responses

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the main script:
```
python main.py
```

The script will process the predefined questions and generate responses about Darmstadt.

## Future Development Plans

- Implement conversation history management
- Add more sophisticated prompt engineering
- Explore different OpenAI models
- Add error handling and retry mechanisms
- Implement streaming responses
- Add unit tests
- Create a simple web interface

## Learning Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/gpt-best-practices)


