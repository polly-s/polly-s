@test
def lhopital(expr, x, x0):
    """
    Computes limit(expr, x, x0) using l'Hopital's rule.

    >>> lhopital(sin(x)/x, x, 0)
    1
    >>> lhopital(exp(x)/x**2, x, oo)
    oo
    >>> lhopital((x**2 - 2*x + 4)/(2 - x), x, 2)
    -oo
    >>> lhopital(x/(2 - x), x, 2)
    -oo
    >>> lhopital(cos(x), x, 0)
    1
    >>> lhopital((x + sin(x))/x, x, 0)
    2
    """
    expr = cancel(expr)
    expr_num, expr_den = fraction(expr)
    expr_num_eval, expr_den_eval = expr_num.subs(x, x0), expr_den.subs(x, x0)
    indeterminates = [(0, 0), (oo, oo), (-oo, oo), (oo, -oo), (-oo, -oo)]
    if (expr_num_eval, expr_den_eval) in indeterminates:
        return lhopital(expr_num.diff(x)/expr_den.diff(x), x, x0)
    return expr_num_eval/expr_den_eval
