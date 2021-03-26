class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # words = set(wordlist)
        def devow(wrd):
            return ''.join(['_' if c in 'aeiou' else c for c in wrd])

        def solve(query):
            if query in wordlist:
                return query
            lw = query.lower()
            if lw in lower_words:
                return lower_words[lw]
            novow = devow(lw)
            return novow_words.get(novow, "")

        lower_words = {}
        novow_words = {}
        for word in wordlist:
            lw = word.lower()
            if lw not in lower_words:
                lower_words[lw] = word
            novow = devow(lw)
            if novow not in novow_words:
                novow_words[novow] = word

        return map(solve, queries)
