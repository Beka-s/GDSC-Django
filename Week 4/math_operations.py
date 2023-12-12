def basic_operations(a, b):
    try:
        result = {}

        result['addition'] = a + b
        result['multiplication'] = a * b
        result['division'] = a / b
        result['subtraction'] = a - b

        return result
    except ValueError:
        print("Oops!  That was an invalid input.  Try again...")
    except ZeroDivisionError:
        print('b must be different from 0')


def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            result %= kwargs['modulo']

        return result
    except ValueError:
        print("Oops!  That was an invalid input.  Try again...")


def apply_operations(operation_list):
    return list(map(lambda x: x[0](*x[1]), operation_list))