class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d = dict(
            a={1,3,5,7},
            b={2,4,6,8},
            c={1, 3, 5, 7},
            d={2, 4, 6, 8},
            e={1, 3, 5, 7},
            f={2, 4, 6, 8},
            g={1, 3, 5, 7},
            h={2, 4, 6, 8},
        )
        s = d.get(coordinates[0])
        return False if int(coordinates[1]) in s else True

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2: return True
        sent_words1 = sentence1.split(" ")
        sent_words2 = sentence2.split(" ")
        long_sent_words = sent_words1 if len(sent_words1) > len(sent_words2) else sent_words2
        short_sent_words = sent_words2 if len(sent_words1) > len(sent_words2) else sent_words1

        i = 0
        m = len(long_sent_words)
        n = len(short_sent_words)

        # 头部插入
        if long_sent_words[i] != short_sent_words[i]:
            j = len(short_sent_words) - 1
            long_end = m - 1
            while j >= 0:
                if long_sent_words[long_end] != short_sent_words[j]:
                    return False
                j -= 1
                long_end -= 1
            return True
        # 尾部插入
        if long_sent_words[i] == short_sent_words[i] and long_sent_words[m-1] != short_sent_words[n-1]:
            for l in range(n):
                if long_sent_words[l] != short_sent_words[l]:
                    return False
            return True
        # 中间插入
        if long_sent_words[i] == short_sent_words[i] and long_sent_words[m-1] == short_sent_words[n-1]:
            long_start = 0
            long_end = m - 1
            short_start = 0
            short_end = n - 1
            while short_start <= short_end and long_sent_words[long_start] == short_sent_words[short_start]:
                long_start += 1
                short_start += 1
            while short_start <= short_end and long_sent_words[long_end] == short_sent_words[short_end]:
                long_end -= 1
                short_end -= 1

            return short_start > short_end

        return False







if __name__ == '__main__':
    s = Solution()
    s1 = "Game is ON"
    s2 = "Game are ON"
    print(s.areSentencesSimilar(s1, s2))


