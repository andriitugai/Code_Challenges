class Solution:
    def originalDigits(self, s: str) -> str:
        def decremental(num, word, control_char):
            n = s_counts.get(control_char, 0)
            if n:
                for c in word:
                    s_counts[c] -= n

                result.extend([str(num)] * n)

        s_counts = {}
        for c in s:
            s_counts[c] = s_counts.get(c, 0) + 1

        result = []

        decremental(6, "six", "x")
        decremental(7, "seven", "s")
        decremental(0, "zero", "z")
        decremental(2, "two", "w")
        decremental(5, "five", "v")
        decremental(4, "four", "f")
        decremental(8, "eight", "g")
        decremental(9, "nine", "i")
        decremental(3, "three", "h")
        decremental(1, "one", "n")

        return ''.join(sorted(result))
