import importlib
from pathlib import Path

import pytest


PYTHON_FILES = sorted(Path("python").rglob("*.py"))


@pytest.mark.parametrize("module_path", PYTHON_FILES, ids=lambda path: str(path))
def test_module_import_has_no_output(module_path, capsys):
    module_name = ".".join(module_path.with_suffix("").parts)
    importlib.import_module(module_name)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
