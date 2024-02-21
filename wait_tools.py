from typing import Union
from time import time


def sleep(secs: Union[int, float]):
    started_at = time()
    while time() - secs < started_at:
        yield
