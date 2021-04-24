
def letterCombinations(digits):
    mapping = {
        "2": 'abc', "3": 'def', "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    def get_combs(number):
        if len(number) == 1:
            return [c for c in mapping[number[0]]]

        return [ch + ct for ct in get_combs(number[1:])
                for ch in mapping[number[0]]]

    digits = ''.join([d for d in digits if d in mapping])
    return [''.join(m) for m in get_combs(digits)]


if __name__ == '__main__':
    print(letterCombinations("7313221"))