@test
def uparrow(x, n):
    """
    Computes x**(x**(...x)), with n copies of x.

    >>> x = symbols('x')
    >>> uparrow(x, 3)
    x**(x**x)
    >>> uparrow(x, 1)
    x
    >>> uparrow(x**x, 3)
    (x**x)**((x**x)**(x**x))
    """
    expr = x
    for i in range(n - 1):
        expr = x**expr
    return expr
