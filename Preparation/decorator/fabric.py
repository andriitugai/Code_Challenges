
def pow(n):
    def inner(x):
        return x ** n

    return inner


if __name__ == '__main__':
    cube = pow(3)
    print(cube(10))
