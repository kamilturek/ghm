from typing import Iterable

from ghm.fs import FileSystem


class NotAGitRepository(Exception):
    pass


class HooksManager:
    def __init__(self, fs: FileSystem) -> None:
        self._fs = fs

    def get_hooks_path(self, repository_path: str) -> str:
        git_path = self._fs.path_join(repository_path, ".git")

        if not self._fs.path_exists(git_path):
            raise NotAGitRepository

        hooks_path = self._fs.path_join(git_path, "hooks")

        return hooks_path

    def list_hooks(self, repository_path: str) -> Iterable[str]:
        if repository_path is None:
            repository_path = self._fs.path_default

        hooks_path = self.get_hooks_path(repository_path)

        for root, _, file_names in self._fs.walk(hooks_path):
            root = self._fs.path_basename(root)
            hook_type = ""

            if root.endswith(".d"):
                hook_type = root[: -len(".d")]

            for file_name in file_names:
                if file_name.endswith(".sample"):
                    continue

                hook_name = file_name
                if hook_type:
                    hook_name = f"{hook_name} ({hook_type})"

                yield hook_name
