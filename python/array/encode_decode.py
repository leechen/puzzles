class Codec:
    def encode(self, strings: list[str]) -> str:
        # use an array to store the encoded strings, and then join them together with a separator
        # this is better than using a single string for performance reasons, as string concatenation is O(n^2) in python
        res = []
        for value in strings:
            res.append(f"{len(value)}#{value}")

        return "".join(res)

    def decode(self, encoded: str) -> list[str]:
        result, index = [], 0
        while index < len(encoded):
            separator = encoded.index("#", index)
            length = int(encoded[index:separator])
            cur = separator + 1
            result.append(encoded[cur : cur + length])
            index = cur + length
        return result
