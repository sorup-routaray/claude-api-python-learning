"""Thin wrapper around the Anthropic SDK client.

Usage in a notebook:
    from utils import ClaudeClient

    claude = ClaudeClient()
    claude.ask("Define quantum computing in one sentence")
"""

from anthropic import Anthropic
from dotenv import find_dotenv, load_dotenv

DEFAULT_MODEL = "claude-haiku-5-5"
DEFAULT_MAX_TOKENS = 1024


class ClaudeClient:
    """Holds default request settings and exposes a few convenience methods.

    The underlying SDK client is available as `.client` for anything not wrapped here.
    """

    def __init__(
        self,
        model=DEFAULT_MODEL,
        max_tokens=DEFAULT_MAX_TOKENS,
        system=None,
        api_key=None,
    ):
        # Walk up from the current working directory to find the project's .env
        load_dotenv(find_dotenv(usecwd=True))
        self.client = Anthropic(api_key=api_key) if api_key else Anthropic()
        self.model = model
        self.max_tokens = max_tokens
        self.system = system

    # ---- message list helpers -------------------------------------------

    @staticmethod
    def add_user_message(messages, text):
        messages.append({"role": "user", "content": text})

    @staticmethod
    def add_assistant_message(messages, text):
        messages.append({"role": "assistant", "content": text})

    @staticmethod
    def get_text(message):
        return "".join(b.text for b in message.content if b.type == "text")

    # ---- requests -------------------------------------------------------

    def _params(self, messages, **overrides):
        params = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": messages,
        }
        if self.system is not None:
            params["system"] = self.system
        # Only pass options that were actually set (e.g. temperature, stop_sequences)
        params.update({k: v for k, v in overrides.items() if v is not None})
        return params

    def create(self, messages, **overrides):
        """Send messages and return the full SDK `Message` object."""
        return self.client.messages.create(**self._params(messages, **overrides))

    def chat(self, messages, **overrides):
        """Send a message list and return the reply text."""
        return self.get_text(self.create(messages, **overrides))

    def ask(self, prompt, **overrides):
        """Send a single user prompt and return the reply text."""
        return self.chat([{"role": "user", "content": prompt}], **overrides)

    def stream(self, messages, **overrides):
        """Yield reply text chunks as they arrive."""
        with self.client.messages.stream(**self._params(messages, **overrides)) as s:
            yield from s.text_stream
