def type_int(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError('Тип должен быть int')
        return function(*args)
    return wrapped


@type_int
def calculate(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print(calculate(1, 2, 3))
