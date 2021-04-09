def append_four(lst):
    # print(f'Inner. id before: {hex(id(lst))}')
    # lst.append(4)
    # lst += [4]
    # lst = lst + [4]
    # lst.extend([4])
    print(f'Inner. List after: {lst}')
    # print(f'Inner. id after: {hex(id(lst))}')


if __name__ == '__main__':
    a = [1, 2, 3]
    append_four(a)
    print(f'Outer. List after: {a}')
