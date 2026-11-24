"""Install Python packages only when they are missing.

Usage in a notebook:
    from utils import ensure_installed

    ensure_installed(["anthropic", "python-dotenv"])
"""

import importlib
import importlib.metadata
import re
import subprocess
import sys


def _distribution_name(requirement):
    """'anthropic>=2.10' -> 'anthropic', 'pkg[extra]' -> 'pkg'."""
    return re.split(r"[\s\[<>=!~;]", requirement.strip(), maxsplit=1)[0]


def _is_installed(requirement):
    try:
        importlib.metadata.version(_distribution_name(requirement))
        return True
    except importlib.metadata.PackageNotFoundError:
        return False


def ensure_installed(packages, quiet=True):
    """Install any of `packages` that are not already installed.

    `packages` is a list of pip requirement strings, e.g.
    ["anthropic", "python-dotenv", "pydantic>=2"]. Only the package name is
    checked; a version specifier is passed to pip when installing.

    Packages go into the current interpreter's environment (the notebook kernel).
    Returns the list of packages that were installed.
    """
    if isinstance(packages, str):
        packages = [packages]

    missing = [pkg for pkg in packages if not _is_installed(pkg)]

    if not missing:
        print("All dependencies already installed")
        return []

    print(f"Installing: {', '.join(missing)}")
    cmd = [sys.executable, "-m", "pip", "install", *missing]
    if quiet:
        cmd.append("-q")
    subprocess.check_call(cmd)
    importlib.invalidate_caches()
    return missing
