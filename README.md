# MoodMirror 🪞

Advanced emotional AI companion combining mood detection with intelligent conversation and reasoning capabilities.

## Features

- **Mood Detection**: Analyzes emotional state from user input
- **Empathetic AI Responses**: Uses Dobby-70B model for supportive conversations
- **ROMA Framework**: Advanced reasoning and orchestration for complex tasks
- **Beautiful UI**: Modern gradient interface with smooth animations
- **Real-time Processing**: Instant mood analysis and AI responses

## Architecture

### Core Components

1. **Flask Web Server** - Handles HTTP requests and serves the UI
2. **Emotion Analyzer** - Keyword-based sentiment detection
3. **Dobby Executor** - Direct AI chat using Dobby-70B model
4. **ROMA Pipeline** - Multi-agent reasoning system for complex tasks
5. **Storage System** - Tracks conversation history

### Technology Stack

- **Backend**: Python, Flask
- **AI**: Dobby-70B (Fireworks AI), OpenRouter
- **Framework**: ROMA (Reasoning & Orchestration Multi-Agent)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## Installation

### Prerequisites

- Python 3.10+
- uv package manager (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/moodmirror.git
cd moodmirror
```

2. Install dependencies:
```bash
uv sync
```

Or with pip:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```

4. Add your API keys to `.env`:
```env
SENTIENT_API_KEY=your_fireworks_api_key
API_BASE_URL=https://api.fireworks.ai/inference/v1
AI_MODEL=accounts/sentientfoundation/models/dobby-unhinged-llama-3-3-70b-new
OPENROUTER_API_KEY=your_openrouter_key (optional, for ROMA)
```

## Usage

Start the application:
```bash
python main.py
```

Access the web interface at: `http://localhost:5000`

## How It Works

### Simple Emotional Chat
```
User Input → Emotion Analysis → Dobby AI → Response
```

### Complex Reasoning Tasks
```
User Input → ROMA Pipeline → Multi-Agent Processing → Response
```

ROMA automatically detects complex tasks and routes them through the multi-agent system for better reasoning.

## Project Structure

```
moodmirror/
├── main.py                 # Flask application entry point
├── dobby_executor.py      # Direct AI chat handler
├── roma_executor.py       # ROMA system executor
├── roma_pipeline.py       # Request routing logic
├── sentiment_toolkit.py   # Emotion detection
├── storage.py            # Conversation storage
├── prompts/              # AI persona configurations
├── templates/            # HTML templates
├── roma_dspy/           # ROMA framework
│   ├── api/            # REST API components
│   ├── config/         # Configuration schemas
│   ├── core/           # Core engine and modules
│   ├── tools/          # Tool integrations
│   └── types/          # Type definitions
└── pyproject.toml      # Dependencies
```

## Configuration

### Environment Variables

- `SENTIENT_API_KEY`: Fireworks AI API key for Dobby-70B
- `API_BASE_URL`: AI API endpoint
- `AI_MODEL`: Model identifier
- `OPENROUTER_API_KEY`: Optional, for ROMA advanced features
- `SESSION_SECRET`: Flask session secret

### Customization

Edit `prompts/dobby_persona.txt` to customize the AI personality.

## ROMA Framework

The ROMA (Reasoning and Orchestration Multi-Agent) framework provides:

- **Multi-Agent Orchestration**: Coordinated AI agents for complex tasks
- **Task Decomposition**: Breaks down complex requests
- **Reasoning Engine**: Advanced logic and planning
- **Tool Integration**: Web search, calculations, file operations
- **Observability**: Execution tracking and monitoring

## Development

### Running in Debug Mode

The app runs in debug mode by default:
```bash
python main.py
```

### Adding Emotions

Edit `EMOTION_KEYWORDS` in `sentiment_toolkit.py`:
```python
EMOTION_KEYWORDS = {
    "your_emotion": ["keyword1", "keyword2"],
}
```

## API Endpoints

- `GET /` - Web interface
- `POST /chat` - Send message, receive AI response

## Security

- Never commit `.env` files
- Rotate API keys regularly
- Use environment variables for secrets
- Keep dependencies updated

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- Powered by Fireworks AI and Dobby-70B
- ROMA framework for advanced reasoning
- OpenRouter for multi-model support

---

**Note**: This is an emotional support tool, not a replacement for professional mental health services.
