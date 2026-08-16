def move(f, t):
    print(f"Move disc from {f} to {t}!")


def hanoi(n, f, h, t):
    """n: number of discs

    f: 'from' peg
    h: 'helper' (auxiliary) peg
    t: 'target' peg
    """
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)

hanoi(5, "A", "B", "C")