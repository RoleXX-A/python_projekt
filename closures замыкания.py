def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    values = []

    def inner(value: int) -> list:
        values.append(value)
        return sum(values) / (len(values))

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):
    def inner(value):
        return value ** base

    return inner


if __name__ == '__main__':


    pow__ = pow_(2)
    pow_2 = pow_(3)

    print(pow__(5))
    print(pow__(6))
    print(pow__(7))
    print(pow_2(5))
    print(pow_2(6))
    print(pow_2(7))
