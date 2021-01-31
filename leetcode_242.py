class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n, counter = len(s), [0] * 26
        for i in range(n):
            counter[ord(s[i]) - 97] += 1
            counter[ord(t[i]) - 97] -= 1
        return not any(counter)


if __name__ == '__main__':
    print(Solution().isAnagram('a', 'b'))
