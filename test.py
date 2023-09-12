import math
import latexify


@latexify.with_latex
def solve(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


if __name__ == '__main__':
    print(solve)