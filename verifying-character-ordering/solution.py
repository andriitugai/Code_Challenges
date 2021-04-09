def verifyOrdering(A, ordering):
    '''
    :type A: list of str
    :type ordering: str
    :rtype: bool
    '''
    order = {}
    for i, c in enumerate(ordering):
        order[c] = i

    def less_than(s1, s2):
        nonlocal order

        last_eq = False
        for c1, c2 in zip(s1, s2):
            if order[c1] > order[c2]:
                return False
            last_eq = c1 == c2

        if (last_eq and len(s1) <= len(s2)) or not last_eq:
            return True

        return False

    for idx in range(1, len(A)):
        if not less_than(A[idx - 1], A[idx]):
            return False

    return True


if __name__ == '__main__':
    a = ["hello", "hey", "a"]
    ordering = "hlbcdefgijkmnopqrstuvwxzya"

    print(verifyOrdering(a, ordering))
