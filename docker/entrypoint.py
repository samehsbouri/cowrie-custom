# Entrypoint script for distroless image.
# Creates required runtime directories then starts twistd.
from __future__ import annotations

import os
import sys

# Ensure all required directories exist (named volumes shadow build-time dirs)
BASE = "/cowrie/cowrie-git/var"
dirs = [
    f"{BASE}/lib/cowrie/tty",
    f"{BASE}/lib/cowrie/downloads",
    f"{BASE}/log/cowrie",
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Replace ourselves with the CMD
os.execvp(sys.argv[1], sys.argv[1:])
