from time import sleep


def do_something():
    sleep(2)
    return 1 + 1


if __name__ == '__main__':
    variable = 0
    while True:
        variable += do_something()
        print(variable)
