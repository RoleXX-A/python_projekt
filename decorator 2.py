def typed(type_):
    def real_decorator(function):
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип должен быть {type_}')
            return function(*args)

        return wrapped

    return real_decorator


@typed(int)
def calculate(a, b, c):  # calculate = typed(int)(calculate)
    return a + b + c


@typed(str)
def convert(a, b): # convert = typed(str)(convert)
    return a + b


if __name__ == '__main__':
    print(calculate(1, 2, 3))
    print(convert('1', 'hello'))

