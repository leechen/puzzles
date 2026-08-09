import runpy
from pathlib import Path

import pytest


PYTHON_FILES = sorted(Path("python").glob("*.py"))


@pytest.mark.parametrize("module_path", PYTHON_FILES, ids=lambda path: path.stem)
def test_module_import_has_no_output(module_path, capsys):
    runpy.run_path(module_path)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
