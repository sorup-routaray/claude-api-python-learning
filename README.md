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

`src/utils/client.py` loads `.env`, creates the client and provides `chat()` and message helpers.
After `pip install -r requirements.txt` it can be imported from any notebook:

```python
from utils import client, chat, add_user_message, add_assistant_message

messages = []
add_user_message(messages, "Define quantum computing in one sentence")
chat(messages)
```

## Project layout

```
notebooks/   lessons, grouped by topic
src/utils/   shared client and helpers
data/        sample inputs/outputs
```
