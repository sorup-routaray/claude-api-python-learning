from utils.dependencies import ensure_installed

__all__ = ["ClaudeClient", "DEFAULT_MODEL", "ensure_installed"]


def __getattr__(name):
    # Import lazily so `from utils import ensure_installed` works
    # before anthropic / python-dotenv are installed.
    if name in ("ClaudeClient", "DEFAULT_MODEL"):
        from utils import claude_api_client

        return getattr(claude_api_client, name)
    raise AttributeError(f"module 'utils' has no attribute {name!r}")
