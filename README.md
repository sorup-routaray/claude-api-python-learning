# Claude API Notebooks

Jupyter notebooks for learning the Claude API with the `anthropic` Python SDK.

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # then add your ANTHROPIC_API_KEY
```

Select the `.venv` kernel when opening the notebooks.

## Notebooks

Suggested order: basics → conversations → prompting → advanced. Notebooks are numbered within each folder.

| Folder | Notebook | Topic |
|--------|----------|-------|
| basics | [001_first_request](notebooks/basics/001_first_request.ipynb) | Creating a client and making a first request |
| basics | [002_multi_turn_messages](notebooks/basics/002_multi_turn_messages.ipynb) | Building a message list for multi-turn requests |
| conversations | [001_chat](notebooks/conversations/001_chat.ipynb) | Interactive chat loop |
| conversations | [002_math_tutor](notebooks/conversations/002_math_tutor.ipynb) | System prompts: a math tutor |
| prompting | [001_system_prompt_temperature](notebooks/prompting/001_system_prompt_temperature.ipynb) | System prompts and temperature |
| advanced | [001_event_streaming](notebooks/advanced/001_event_streaming.ipynb) | Streaming responses |
| advanced | [002_structured_output](notebooks/advanced/002_structured_output.ipynb) | Structured output and stop sequences |

## Shared helpers

`src/utils/claude_api_client.py` provides `ClaudeClient`, a thin wrapper around the Anthropic SDK
that loads `.env` and holds default settings (model, `max_tokens`, system prompt).
After `pip install -r requirements.txt` it can be imported from any notebook:

```python
from utils import ClaudeClient

claude = ClaudeClient()                      # optional: model=, max_tokens=, system=
claude.ask("Define quantum computing in one sentence")   # -> str

messages = []
claude.add_user_message(messages, "Name a prime number")
reply = claude.chat(messages)                # -> str
claude.add_assistant_message(messages, reply)

for chunk in claude.stream(messages):        # streamed text
    print(chunk, end="")

claude.create(messages)                      # full SDK Message object
claude.client                                # raw Anthropic client
```

## Project layout

```
notebooks/   lessons, grouped by topic
src/utils/   shared client and helpers
data/        sample inputs/outputs
```
