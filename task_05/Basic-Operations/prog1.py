@test
def evaluate(exprs, x, x0):
    """
    Evaluate each expression in exprs at the point x = x0.

    >>> x, y = symbols('x y')
    >>> exprs = [x**2, cos(x), x*y]
    >>> evaluate(exprs, x, 1)
    [1, cos(1), y]
    >>> evaluate(exprs, y, 0)
    [x**2, cos(x), 0]
    """
    return [expr.subs(x, x0) for expr in exprs]
    
    
    
