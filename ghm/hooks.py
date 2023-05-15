import os
import sys


def list_hooks():
    git_path = os.path.join(os.curdir, ".git")

    if not os.path.exists(git_path):
        sys.stderr.write("not a git repository")
        sys.exit(1)

    hooks_path = os.path.join(git_path, "hooks")

    for root, _, filenames in os.walk(hooks_path):
        root = os.path.basename(root)
        hook_type = ""

        if root.endswith(".d"):
            hook_type = root[:-len(".d")]

        for filename in filenames:
            if filename.endswith(".sample"):
                continue

            print(f"{hook_type}: {filename}")
