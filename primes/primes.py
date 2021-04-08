def enumeratePrimes(n):
    '''
    :type n: int
    :rtype: list of int
    '''
    bools = [False] * 2 + [True] * (n - 2)
    primes = [2]
    cur_prime = 2

    while True:
        idx = cur_prime
        while cur_prime + idx < n:
            idx += cur_prime
            bools[idx] = False

        i = cur_prime + 1
        while i < n and not bools[i]:
            i += 1

        if i == n:
            break

        cur_prime = i
        primes.append(cur_prime)

    return primes


if __name__ == '__main__':
    print(enumeratePrimes(50))
