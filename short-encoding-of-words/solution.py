class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)
        for word in words:
            if word in word_set:
                for start_idx in range(1, len(word)):
                    word_set.discard(word[start_idx:])

        return len('#'.join(list(word_set))) + 1