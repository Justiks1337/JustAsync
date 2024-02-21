from wait_tools import sleep
from EventLoop import EventLoop

main_loop = EventLoop()


def main():
    task = main_loop.create_task(sleep(5))
    task2 = main_loop.create_task(sleep(5))

    yield from task
    yield from task2

    print("test passed")


if __name__ == '__main__':

    main_loop.create_task(main())
    main_loop.run_forever()
