class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dp(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                # No swap
                if dp(a[:i], b[:i]) and dp(a[i:], b[i:]):
                    return True
                # With swap
                if dp(a[:i], b[-i:]) and dp(a[i:], b[:-i]):
                    return True
            return False

        return dp(s1, s2)
