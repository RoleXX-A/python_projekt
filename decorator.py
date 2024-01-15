def dec(test):
    def logger(*args):
        error = 'error'
        print(f'{test.__name__} starter')
        result = test(*args)
        print(f'{test.__name__} finished')
        if result == 4:
            return result
        else:
            return error

    return logger


@dec
def sum(a, b):
    return a + b

if __name__ == '__main__':
    print(sum(2,3))