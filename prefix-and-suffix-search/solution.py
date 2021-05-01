from collections import defaultdict
from functools import lru_cache


class WordFilter:

    def __init__(self, words):
        self.prefixes = defaultdict(list)
        self.suffixes = defaultdict(list)

        for idx, word in enumerate(words):
            key_len = min(len(word), 10)
            for i in range(1, key_len + 1):
                self.prefixes[word[:i]].append(idx)
                self.suffixes[word[-i:]].append(idx)

    @lru_cache
    def f(self, prefix: str, suffix: str) -> int:
        pref_idx = set(self.prefixes[prefix])
        suff_idx = set(self.suffixes[suffix])
        indices = pref_idx.intersection(suff_idx)

        if not indices:
            return -1

        return max(indices)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

if __name__ == '__main__':
    words = ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa",
             "accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]
    wfilter = WordFilter(words)

    print(wfilter.f("a", "aa"))