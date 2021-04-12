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

        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1

        if i < len(s1) and i < len(s2) and order[s1[i]] < order[s2[i]]:
            return True
        if i == len(s1):            # s1 is shorter than s2
            return True

        return False

    for idx in range(1, len(A)):
        if not less_than(A[idx - 1], A[idx]):
            return False

    return True


if __name__ == '__main__':
    a = ["hello", "leetcode"]
    ordering = "hlabcdefgijkmnopqrstuvwxyz"

    print(verifyOrdering(a, ordering))
