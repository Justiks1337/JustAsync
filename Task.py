from typing import Optional, Generator


class Task:
    def __init__(self, coro):
        self.coro: Generator = coro
        self.done = False
        self.result = None
        self.next: Optional[Task] = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.done:
            return None
        raise StopIteration
