@test
def trig_rewrite(expr, x):
    """
    Rewrite all trig functions t(x) in terms of sin(x) and cos(x)

    >>> x, y = symbols('x y')
    >>> trig_rewrite(tan(x), x)
    sin(x)/cos(x)
    >>> trig_rewrite(tan(x) + cos(x)*sec(x), x)
    sin(x)/cos(x) + 1
    >>> trig_rewrite(cot(x) + sin(x)*csc(x), x)
    1 + cos(x)/sin(x)
    >>> trig_rewrite(tan(x)*tan(y), x)
    sin(x)*tan(y)/cos(x)
    >>> trig_rewrite(tan(x)*tan(y), y)
    sin(y)*tan(x)/cos(y)
    """
    return expr.subs([(tan(x), sin(x)/cos(x)), (sec(x), 1/cos(x)), (csc(x), 1/sin(x)), (cot(x), cos(x)/sin(x))])
