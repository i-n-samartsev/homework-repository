def check_fibonacci(data_to_process):
    def _check_window(x: int, y: int, z: int) -> bool:
        return (x + y) == z

    a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
    while len(data_to_process) >= 3:
        if not _check_window(a, b, c):
            return "it's not a fib sequence!"
        data_to_process = data_to_process[1:]
        if len(data_to_process) >= 3:
            a, b, c = b, c, data_to_process[2]
        else:
            return "it's a fib sequence!"
