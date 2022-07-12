# Problem 66:
#     Diophantine Equation
#
# Description:
#     Consider quadratic Diophantine equations of the form:
#         x^2 – Dy^2 = 1
#
#     For example, when D = 13, the minimal solution in x is 649^2 - 13 * 180^2 = 1.
#
#     It can be assumed that there are no solutions in positive integers when D is square.
#
#     By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#         3^2 - 2 * 2^2 = 1
#         2^2 - 3 * 1^2 = 1
#         9^2 - 5 * 4^2 = 1
#         5^2 - 6 * 2^2 = 1
#         8^2 - 7 * 3^2 = 1
#
#     Hence, by considering minimal solutions in x for D ≤ 7,
#       the largest x is obtained when D = 5.
#
#     Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

from math import floor, sqrt
from typing import Tuple


def is_perfect_square(n: int) -> bool:
    """
    Returns True iff `n` is a positive perfect square.

    Args:
        n (int): Integer

    Returns:
        (bool): True iff `n` is a positive perfect square

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int
    if n < 1:
        return False
    else:
        r = sqrt(n)
        return int(r) == r


def main(d_max: int) -> Tuple[int, int, int]:
    """
    Returns D, x, and y in the diophantine equation x^2 - Dy^2 = 1
      such that D ≤ `d_max` and x is the largest minimal solution among such D.

    Args:
        d_max (int): Natural number greater than 1

    Returns:
        (Tuple[int, int, int]): D, x, and y in the diophantine equation
          such that D ≤ `d_max` and x is the largest minimal solution among such D.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(d_max) == int and d_max > 1

    x_highest = y_best = d_best = 0

    for d in range(2, d_max+1):
        if is_perfect_square(d):
            # No solution, so skip
            continue

        # Idea:
        #     Apparently can use the convergents of continued fraction representations of sqrt(d)
        #     to iteratively look for possible solutions to the Pell equation. (???)
        #     Interesting stuff lol

        # Use these to keep figuring out `a` in continued fraction sequence
        r = 0
        q = 1
        a = floor((sqrt(d)-r)/q)

        # Only need to keep track of previous two numerators/denominators
        ns = [1, a]
        ds = [0, 1]

        # Keep iterating until something is found
        while ns[-1]**2 - d*ds[-1]**2 != 1:
            # Compute next iteration of continued fraction
            z = r + a*q  # Just to simplify redundant stuff
            r = -1 * z
            q = (d - z**2) // q
            a = floor((sqrt(d) - r) / q)

            # Compute next numerator/denominator of convergent
            ns.append(a*ns[-1]+ns[-2])
            ds.append(a*ds[-1]+ds[-2])
            ns.pop(0)
            ds.pop(0)

        # Found minimal solution to equation for `d`
        x = ns[-1]
        y = ds[-1]

        # Update best x seen so far
        if x > x_highest:
            x_highest = x
            y_best = y
            d_best = d
        else:
            continue

    return d_best, x_highest, y_best


if __name__ == '__main__':
    maximum_D = int(input('Enter a natural number: '))
    best_D, best_x, best_y = main(maximum_D)
    print('Diophantine equation (for D ≤ {}) having highest minimal x:'.format(maximum_D))
    print('  {}^2 - {} * {}^2 = 1'.format(best_x, best_D, best_y))
    print('  x = {}'.format(best_x))
    print('  y = {}'.format(best_y))
    print('  D = {}'.format(best_D))
