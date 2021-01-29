from enum import IntEnum

x = 0

if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")


# bad example
OPEN = 1
IN_PROGRESS = 2
CLOSED = 3


def handle_open_status():
    print("open")


def handle_in_progress_status():
    print("close")


def handle_close_status():
    print("change")


def handle_status_change(status):
    if status == OPEN:
        handle_open_status()
    elif status == IN_PROGRESS:
        handle_in_progress_status()
    elif status == CLOSED:
        handle_close_status()


handle_status_change(1)

#  bad example


# good example
class StatusE(IntEnum):
    OPEN = 1
    IN_PROGRESS = 2
    CLOSED = 3


handlers = {
    StatusE.OPEN.value: handle_open_status,
    StatusE.IN_PROGRESS.value: handle_in_progress_status,
    StatusE.CLOSED.value: handle_close_status,
}


def handle_status_change2(status):
    if status not in handlers:
        raise Exception(f'No handler found fot status: {status}')
    handler = handlers[status]
    handler()


handle_status_change2(StatusE.OPEN.value)