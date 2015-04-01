{
 "metadata": {
  "name": "Basic Operations"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "heading",
     "level": 1,
     "metadata": {},
     "source": "Basic Operations"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Boilerplate to make the doctester work.  Run this cell first."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "import sys\nimport os\nsys.path.insert(1, os.path.join(os.path.pardir, \"ipython_doctester\"))\nfrom sympy import *\nfrom ipython_doctester import test",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "For each exercise, fill in the function according to its docstring. Execute the cell to see if you did it right. "
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Substitution"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that takes a list of expressions, a variable, and a point, and evaluates each expression in the list at that point."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef evaluate(exprs, x, x0):\n    \"\"\"\n    Evaluate each expression in exprs at the point x = x0.\n\n    >>> x, y = symbols('x y')\n    >>> exprs = [x**2, cos(x), x*y]\n    >>> evaluate(exprs, x, 1)\n    [1, cos(1), y]\n    >>> evaluate(exprs, y, 0)\n    [x**2, cos(x), 0]\n    \"\"\"\nreturn [expr.subs(x, x0) for expr in exprs]",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that computes \n\n$$\n{\\underbrace{x^{{}^{.^{.^{.^x}}}}}_\\text{n copies of x}}\n$$\n\nThat is, `x**(x**(...x))`, with `n` copies of `x`.  In [Knuth up-arrow notation](http://en.wikipedia.org/wiki/Up_arrow_notation), $x\\uparrow\\uparrow n$."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef uparrow(x, n):\n    \"\"\"\n    Computes x**(x**(...x)), with n copies of x.\n\n    >>> x = symbols('x')\n    >>> uparrow(x, 3)\n    x**(x**x)\n    >>> uparrow(x, 1)\n    x\n    >>> uparrow(x**x, 3)\n    (x**x)**((x**x)**(x**x))\n    \"\"\"\nexpr = x\n    for i in range(n - 1):\n        expr = x**expr\n    return expr",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that takes a function and nests it within itself n times. \n\nFor example, if we started with $x^x$, and $n=3$, we would end up with \n\n$$\\left(\\left(x^{x}\\right)^{\\left(x^{x}\\right)}\\right)^\\left({\\left(x^{x}\\right)^{\\left(x^{x}\\right)}}\\right)$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef nest(expr, x, n):\n    \"\"\"\n    Nests expr into itself (in the variable x) n times.\n\n    >>> x, y = symbols('x y')\n    >>> nest(x**x, x, 3)\n    ((x**x)**(x**x))**((x**x)**(x**x))\n    >>> nest(sin(x)*cos(y), x, 2)\n    sin(sin(x)*cos(y))*cos(y)\n    >>> nest(sin(x)*cos(y), y, 2)\n    sin(x)*cos(sin(x)*cos(y))\n    >>> nest(x**2, x, 1)\n    x**2\n    \"\"\"\norigexpr = expr\n    for i in range(n - 1):\n        expr = expr.subs(x, origexpr)\n    return expr",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that replaces all trig functions in terms of $\\sin(x)$ and $\\cos(x)$. You can assume that the trig function will be of the form $t(x)$, where $x$ is the variable.  The trig functions implemented in SymPy are\n\n$$\\tan(x) = \\frac{\\sin(x)}{\\cos(x)}$$\n$$\\cot(x) = \\frac{\\cos(x)}{\\sin(x)}$$\n$$\\sec(x) = \\frac{1}{\\cos(x)}$$\n$$\\csc(x) = \\frac{1}{\\sin(x)}$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef trig_rewrite(expr, x):\n    \"\"\"\n    Rewrite all trig functions t(x) in terms of sin(x) and cos(x)\n\n    >>> x, y = symbols('x y')\n    >>> trig_rewrite(tan(x), x)\n    sin(x)/cos(x)\n    >>> trig_rewrite(tan(x) + cos(x)*sec(x), x)\n    sin(x)/cos(x) + 1\n    >>> trig_rewrite(cot(x) + sin(x)*csc(x), x)\n    1 + cos(x)/sin(x)\n    >>> trig_rewrite(tan(x)*tan(y), x)\n    sin(x)*tan(y)/cos(x)\n    >>> trig_rewrite(tan(x)*tan(y), y)\n    sin(y)*tan(x)/cos(y)\n    \"\"\"\nreturn expr.subs([(tan(x), sin(x)/cos(x)), (sec(x), 1/cos(x)), (csc(x), 1/sin(x)), (cot(x), cos(x)/sin(x))])",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Suppose we are working with the series expansion of a function at $x=0$, like $a_0 + a_1x + a_2x^2 + \\cdots$.  In this expansion, the terms with higher powers are less significant to the calculation.  For example, if we had\n\n$$1 + x + \\frac{x^{2}}{2} + \\frac{x^{3}}{6} + \\frac{x^{4}}{24} + \\frac{x^{5}}{120} + \\frac{x^{6}}{720} + \\frac{x^{7}}{5040} + \\frac{x^{8}}{40320} + \\frac{x^{9}}{362880}$$\n\nWe might only care about the terms with powers less than 5\n\n$$1 + x + \\frac{x^{2}}{2} + \\frac{x^{3}}{6} + \\frac{x^{4}}{24}$$\n\nWe will see later that this is can be done automatically using the `O` class, but it can also be done using `subs`."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef series_reduce(expr, x, p):\n    \"\"\"\n    Remove all powers of x in expr with power greater than p.\n\n    You may assume that there are no powers of x greater than 10.\n\n    Bonus: which functions are represented by the series expansions below (you\n    can use expr.series(x, 0, 10) to check if you are right)?\n\n    >>> x, y = symbols('x y')\n    >>> series_reduce(1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320, x, 5)\n    x**4/24 - x**2/2 + 1\n    >>> series_reduce(1 + x + x**2 + x**3 + x**4 + x**5 + x**6 + x**7 + x**8 + x**9 + x**10, x, 0)\n    1\n    >>> series_reduce(x*y + x**3*y**3/3 + 2*x**5*y**5/15 + 17*x**7*y**7/315 + 62*x**9*y**9/2835, x, 5)\n    2*x**5*y**5/15 + x**3*y**3/3 + x*y\n    \"\"\"\nreturn expr.subs([(x**i, 0) for i in range(11) if  i > p])",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Evalf"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "At the 763rd place in the decimal expansion of $\\pi$, there is `999999` (see the below comic ref: http://www.qwantz.com/index.php?comic=1013).  Note T-Rex's counting is off if you count the digits like\n\n\n       pi: 3 . 1 4 1 5 9\n \n    digit: 1   2 3 4 5 6"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "from IPython.core.display import Image \nImage(filename='../imgs/comic2-1040.png') ",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that takes a symbolic expression (like `pi`), and determines the first place where `999999` appears.  "
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Tip: Use the string representation of the number. Python starts counting at 0, but the decimal point offsets this"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "str(1.2345).find('345')",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef find_999999(expr, limit=100000):\n    \"\"\"\n    Find the first place in the decimal expr where 999999 appears.\n\n    Only checks up to limit digits. \n\n    Returns False when 999999 does not appear.\n\n    >>> find_999999(pi)\n    763\n    >>> find_999999(E)\n    False\n    >>> find_999999(E, 1000000) # This one will take a few seconds to compute\n    384341\n    \"\"\"\nfound = str(expr.evalf(limit)).find('999999')\n    if found < 0:\n        return False\n    return found",
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}
