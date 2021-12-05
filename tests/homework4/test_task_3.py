from homework4.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_print_to_stdout(capsys):
    my_precious_logger('print to stdout')
    captured = capsys.readouterr()
    assert captured.out == "print to stdout"


def test_my_precious_logger_print_to_stderr(capsys):
    my_precious_logger('error 404')
    captured = capsys.readouterr()
    assert captured.err == "error 404"
