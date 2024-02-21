from typing import Optional, Union, Coroutine

from Task import Task


class EventLoop:
    def __init__(self):
        self.done = False
        self.run = False
        self.first_task: Optional[Task] = None
        self.end_task: Optional[Task] = None

    def run_until_complete(self, task: Union[Coroutine, Task]):

        if isinstance(task, Coroutine):
            task = Task(task)

        self.__on_run()
        self.create_task(task)
        while not task.done:
            self.__iter_tasks()

    def run_forever(self):
        self.__on_run()
        while self.run:
            self.__iter_tasks()

    def create_task(self, coro):
        task = Task(coro)
        try:
            self.end_task.next, self.end_task = task, task
        except AttributeError:
            self.first_task, self.end_task = task, task
        return task

    def __iter_tasks(self):
        try:
            self.first_task.coro.__next__()
            self.first_task, self.end_task.next, self.end_task = self.first_task.next, self.first_task, self.first_task
        except StopIteration as error:
            self.first_task.result = error.value
            self.first_task.done = True
            self.first_task = self.first_task.next

    def __on_run(self):
        self.run = True
