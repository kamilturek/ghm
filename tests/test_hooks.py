import os
from unittest.mock import Mock

import pytest

from ghm.fs import FileSystem
from ghm.hooks import HooksManager, NotAGitRepository


@pytest.fixture
def mock_fs():
    fs = Mock(spec_set=FileSystem)
    fs.path_join = os.path.join
    return fs


class TestHooksPath:
    def test_returns_hooks_path(self, mock_fs):
        mock_fs.path_exists.return_value = True

        hooks_path = HooksManager(mock_fs).get_hooks_path("foo")

        assert hooks_path == "foo/.git/hooks"

    def test_raises_not_a_git_repository(self, mock_fs):
        mock_fs.path_exists.return_value = False

        with pytest.raises(NotAGitRepository):
            HooksManager(mock_fs).get_hooks_path("foo")
