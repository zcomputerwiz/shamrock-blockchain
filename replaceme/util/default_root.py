import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("SHAMROCK_ROOT", "~/.shamrock/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("SHAMROCK_KEYS_ROOT", "~/.shamrock_keys"))).resolve()
