class Codec:
    def encode(self, strings: list[str]) -> str:
        return "".join(f"{len(value)}#{value}" for value in strings)

    def decode(self, encoded: str) -> list[str]:
        result, index = [], 0
        while index < len(encoded):
            separator = encoded.index("#", index)
            length = int(encoded[index:separator])
            start = separator + 1
            result.append(encoded[start : start + length])
            index = start + length
        return result
