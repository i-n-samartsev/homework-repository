"""Task01 - Calculator"""

def check_power_of_2(arg: int) -> bool:
    """Checking if a number is a power of two """
    if arg != 0:
        return not bool(arg & (arg - 1))
    return False
