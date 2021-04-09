import math

def changeBase(numAsString, b1, b2):
    '''
    :type numAsString: str
    :type b1: int
    :type b2: int
    :rtype: str
    '''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_to_ten = {}
    for i, c in enumerate(digits):
        digits_to_ten[c] = i

    # convert numAsString from b1-base into 10-base
    r_base10 = 0
    if b1 != 10:
        pw = 0
        for c in numAsString[::-1]:
            r_base10 += digits_to_ten[c]*b1**pw
            pw += 1

    else:
        r_base10 = int(numAsString)

    # convert r_base10 from 10-base into b2-base
    if b2 != 10:
        pw = int(math.log(r_base10, b2))
        result = ""
        while pw >= 0:
            c = digits[r_base10//(b2**pw)]
            r_base10 %= (b2**pw)
            pw -= 1
            result += c
    else:
        result = str(r_base10)

    return result


if __name__ == '__main__':
    print(changeBase("13", 16, 10))
