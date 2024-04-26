class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            n = len(s)
            res += f"{n}${s}"
        return res
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        cur = ""
        l = len(str)
        i = 0
        while i < l:
            j = i
            while str[j] != '$':
                j += 1
            length = int(str[i:j])
            cur = str[j+1:j+length+1]
            res.append(cur)
            i = j+length+1

        return res

sol = Solution()
mid = sol.encode(["lint","code","love","you"])

print(mid)
res = sol.decode(mid)

print(res)