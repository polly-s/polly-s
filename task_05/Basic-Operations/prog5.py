@test
def series_reduce(expr, x, p):
    """
    Remove all powers of x in expr with power greater than p.

    You may assume that there are no powers of x greater than 10.

    Bonus: which functions are represented by the series expansions below (you
    can use expr.series(x, 0, 10) to check if you are right)?

    >>> x, y = symbols('x y')
    >>> series_reduce(1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320, x, 5)
    x**4/24 - x**2/2 + 1
    >>> series_reduce(1 + x + x**2 + x**3 + x**4 + x**5 + x**6 + x**7 + x**8 + x**9 + x**10, x, 0)
    1
    >>> series_reduce(x*y + x**3*y**3/3 + 2*x**5*y**5/15 + 17*x**7*y**7/315 + 62*x**9*y**9/2835, x, 5)
    2*x**5*y**5/15 + x**3*y**3/3 + x*y
    """
    return expr.subs([(x**i, 0) for i in range(11) if  i > p])
