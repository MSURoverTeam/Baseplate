import os
from typing import List, Union

CURRENT_LEVEL = os.getenv("RUN_LEVEL", "dev")


def validate_run_level(require: Union[str, List[str]]) -> None:
    if not isinstance(require, list):
        require = [require]
    assert CURRENT_LEVEL in require
