import os
import sys
import pytest
from pathlib import Path

project_root = Path(__file__).parent.parent.absolute()
# sys.path.append(project_root)
os.environ["PYTHONPATH"] = f'{project_root}'


@pytest.fixture
def data_dir():
    return Path(__file__).parent / 'data'
