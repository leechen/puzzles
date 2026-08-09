"""Small, executable demonstration of basic Python control flow and lists."""


def describe_number(number: int) -> str:
    if number < 0:
        return "negative"
    if number > 2:
        return "n>2"
    return "0<n<2"


def main(number: int = 3) -> None:
    print(describe_number(number))
    print(float("inf"))

    values = [1, 2, 3]
    values.append(4)
    print(values)
    values.pop()
    print(values)
    values.pop(0)
    print(values)
    values.insert(1, 8)
    print(values)


if __name__ == "__main__":
    main()
