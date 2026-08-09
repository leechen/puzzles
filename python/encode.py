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
    def decode(self, encoded):
        # write your code here
        res = []
        cur = ""
        l = len(encoded)
        i = 0
        while i < l:
            j = i
            while encoded[j] != '$':
                j += 1
            length = int(encoded[i:j])
            cur = encoded[j+1:j+length+1]
            res.append(cur)
            i = j+length+1

        return res

def main() -> None:
    solution = Solution()
    encoded = solution.encode(["lint", "code", "love", "you"])
    print(encoded)
    print(solution.decode(encoded))


if __name__ == "__main__":
    main()
