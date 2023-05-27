import os
from abc import ABC, abstractmethod
from typing import Iterable


class FileSystem(ABC):
    @abstractmethod
    def walk(self, top: str) -> Iterable[tuple[str, list[str], list[str]]]:
        raise NotImplementedError

    @property
    @abstractmethod
    def path_default(self) -> str:
        raise NotImplementedError

    def path_exists(self, path: str) -> bool:
        raise NotImplementedError

    def path_basename(self, path: str) -> str:
        raise NotImplementedError

    def path_join(self, *paths: str) -> str:
        raise NotImplementedError


class OSFileSystem(FileSystem):
    def walk(self, top: str) -> Iterable[tuple[str, list[str], list[str]]]:
        return os.walk(top)

    @property
    def path_default(self) -> str:
        return os.curdir

    def path_exists(self, path: str) -> bool:
        return os.path.exists(path)

    def path_basename(self, path: str) -> str:
        return os.path.basename(path)

    def path_join(self, *paths: str) -> str:
        return os.path.join(*paths)
