#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(None if b == 0 else (a / b)))
