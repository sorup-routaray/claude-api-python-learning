"""Shared Claude client and chat helpers for the notebooks.

Usage in a notebook:
    from utils import client, chat, add_user_message
"""

from anthropic import Anthropic
from dotenv import find_dotenv, load_dotenv

# Walk up from the current working directory to find the project's .env
load_dotenv(find_dotenv(usecwd=True))

MODEL = "claude-opus-5-5"

client = Anthropic()


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def get_message_text(message):
    return "".join(b.text for b in message.content if b.type == "text")


def chat(
    messages,
    system=None,
    temperature=None,
    max_tokens=1024,
    stop_sequences=None,
    model=MODEL,
):
    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    if system is not None:
        params["system"] = system
    if temperature is not None:
        params["temperature"] = temperature
    if stop_sequences is not None:
        params["stop_sequences"] = stop_sequences

    message = client.messages.create(**params)
    return get_message_text(message)
