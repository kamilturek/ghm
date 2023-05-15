#!/usr/bin/env python3

import os
import subprocess
import sys


def run_hooks():
    hook_type = os.path.basename(__file__)
    hooks_path = os.path.join(os.path.dirname(__file__), f"{hook_type}.d")

    for hook_filename in os.listdir(hooks_path):
        cmd = os.path.join(hooks_path, hook_filename)
        proc = subprocess.run([cmd, *sys.argv[1:]], capture_output=True)

        sys.stdout.write(proc.stdout.decode())
        sys.stderr.write(proc.stderr.decode())

        if proc.returncode != 0:
            sys.exit(proc.returncode)


if __name__ == "__main__":
    run_hooks()
