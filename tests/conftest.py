import os
import pytest
from pathlib import Path

project_root = Path(__file__).parent.parent.absolute()
os.environ["PYTHONPATH"] = f'{project_root}'


@pytest.fixture
def data_dir():
    return Path(__file__).parent / 'data'
