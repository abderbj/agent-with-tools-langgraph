# Customer Support Bot

A conversational AI customer support bot built with LangGraph, Ollama, and LangChain. The bot can handle customer inquiries and use tools to provide helpful information.

## Features

- **Conversational AI**: Powered by Llama 3.2 model via Ollama
- **Tool Integration**: Built-in tools for common support tasks
- **Memory**: Maintains conversation context across interactions
- **Extensible**: Easy to add new tools and capabilities

## Available Tools

1. **Current Time**: Get the current date and time
2. **Random Number Generator**: Generate random numbers within a specified range
3. **Calculator**: Perform basic mathematical operations (addition)
4. **Customer Support Info**: Provide information about billing, technical support, returns, shipping, and account management

## Prerequisites

- Python 3.8 or higher
- Windows, macOS, or Linux

## Installation & Setup

### 1. Clone or Download the Project

```bash
git clone <your-repository-url>
cd "customer support bot"
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

#### Windows:
1. Download Ollama from [https://ollama.ai/](https://ollama.ai/)
2. Run the installer and follow the setup instructions

#### macOS:
```bash
brew install ollama
```

#### Linux:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 5. Start Ollama Service

Open a new terminal window and start the Ollama service:

```bash
ollama serve
```

Keep this terminal window open while using the bot.

### 6. Download the Llama 3.2 Model

In another terminal window, download the required model:

```bash
ollama pull llama3.2
```

This will download the Llama 3.2 model (approximately 2GB). Wait for the download to complete.

### 7. Verify Ollama Installation

Check if the model is available:

```bash
ollama list
```

You should see `llama3.2` in the list of available models.

## Usage

### Running the Bot

1. Make sure Ollama is running (`ollama serve` in a separate terminal)
2. Activate your virtual environment
3. Run the bot:

```bash
python flow.py
```

### Example Interactions

**Getting Current Time:**
```
🤖 Pass your prompt here: What time is it?
```

**Generating Random Numbers:**
```
🤖 Pass your prompt here: Generate a random number between 1 and 100
```

**Mathematical Calculations:**
```
🤖 Pass your prompt here: What's 25 plus 37?
```

**Customer Support:**
```
🤖 Pass your prompt here: I need help with billing
🤖 Pass your prompt here: How do I return an item?
🤖 Pass your prompt here: What are your shipping options?
```

**General Conversation:**
```
🤖 Pass your prompt here: Hello, how can you help me?
```

### Exiting the Bot

Type `quit`, `exit`, or press `Ctrl+C` to stop the bot.

## Project Structure

```
customer support bot/
├── flow.py              # Main application file
├── tool.py              # Tool definitions
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Troubleshooting

### Common Issues

1. **Connection Error**: If you see a connection error, make sure Ollama is running with `ollama serve`

2. **Model Not Found**: If you get a model error, ensure you've downloaded the model with `ollama pull llama3.2`

3. **Import Errors**: Make sure you've activated your virtual environment and installed all requirements

4. **Tool Binding Error**: Ensure you're using the correct Ollama model that supports tool calling

### Checking Ollama Status

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# List available models
ollama list

# Test model directly
ollama run llama3.2 "Hello"
```

## Development

### Adding New Tools

To add new tools, edit `tool.py`:

1. Create a new function with the `@tool` decorator
2. Add proper type hints and docstring
3. Add the tool to the `X` list at the bottom of the file

Example:
```python
@tool
def my_new_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"
```

### Customizing the Bot

- **Change Model**: Edit the model name in `flow.py` (line 12)
- **Modify Personality**: Add system prompts or modify the chatbot function
- **Add Memory**: The bot already has conversation memory enabled

## Dependencies

- `langgraph`: For building conversational AI workflows
- `langchain-ollama`: For integrating with Ollama models
- `langchain-core`: Core LangChain functionality
- `colorama`: For terminal text coloring
- `typing-extensions`: Enhanced type hints
- `pydantic`: Data validation

## License

This project is open source. Feel free to modify and distribute as needed.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Ensure all installation steps were completed
3. Verify Ollama is running and the model is downloaded
