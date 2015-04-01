@test
def nest(expr, x, n):
    """
    Nests expr into itself (in the variable x) n times.

    >>> x, y = symbols('x y')
    >>> nest(x**x, x, 3)
    ((x**x)**(x**x))**((x**x)**(x**x))
    >>> nest(sin(x)*cos(y), x, 2)
    sin(sin(x)*cos(y))*cos(y)
    >>> nest(sin(x)*cos(y), y, 2)
    sin(x)*cos(sin(x)*cos(y))
    >>> nest(x**2, x, 1)
    x**2
    """
    origexpr = expr
    for i in range(n - 1):
        expr = expr.subs(x, origexpr)
    return expr
