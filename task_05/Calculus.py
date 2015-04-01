{
 "metadata": {
  "name": "Calculus"
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
     "source": "Calculus"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Boilerplate to make the doctester work. "
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "import sys\nimport os\nsys.path.insert(1, os.path.join(os.path.pardir, \"ipython_doctester\"))\nfrom sympy import *\nfrom ipython_doctester import test\n# Work around a bug in IPython. This will disable the ability to paste things with >>>\ndef notransform(line): return line\nfrom IPython.core import inputsplitter\ninputsplitter.transform_classic_prompt = notransform",
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 1
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "For each exercise, fill in the function according to its docstring. Execute the cell to see if you did it right. "
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "x, y, z = symbols('x y z')",
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Derivatives"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Compute the following\n\n$$ \\frac{d}{dx}\\sin(x)e^x$$\n$$ \\frac{\\partial}{\\partial x}\\sin(xy)e^x $$\n$$ \\frac{\\partial^2}{\\partial x\\partial y}\\sin(xy)e^x $$\n"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "diff(sin(x)*exp(x), x)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "diff(sin(x*y)*exp(x), x)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "diff(sin(x*y)*exp(x), x, y)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Recall l'Hopital's rule, which states that if $$\\lim_{x\\to x_0}\\frac{f(x)}{g(x)}$$ is $\\frac{0}{0}$, $\\frac{\\infty}{\\infty}$, or $-\\frac{\\infty}{\\infty}$, then it is equal to $$\\lim_{x\\to x_0} \\frac{f'(x)}{g'(x)}$$ (we will not consider other indeterminate forms here).  \n\nWrite a function that computes $\\lim_{x\\to x_0}\\frac{f(x)}{g(x)}$. Use the `fraction` function to get the numerator and denominator of an expression, for example"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "fraction(x/y)",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 3,
       "text": "(x, y)"
      }
     ],
     "prompt_number": 3
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "You may assume that the only indeterminate forms are the ones mentioned above, and that l'Hopital's rule will terminate after a finite number of steps. Do not use `limit` (use `subs`). Remember that after taking the derivatives, you will need to put the expression into the form $\\frac{f(x)}{g(x)}$ before applying l'Hopital's rule again (what function did we learn that does this?)."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef lhopital(expr, x, x0):\n    \"\"\"\n    Computes limit(expr, x, x0) using l'Hopital's rule.\n\n    >>> lhopital(sin(x)/x, x, 0)\n    1\n    >>> lhopital(exp(x)/x**2, x, oo)\n    oo\n    >>> lhopital((x**2 - 2*x + 4)/(2 - x), x, 2)\n    -oo\n    >>> lhopital(x/(2 - x), x, 2)\n    -oo\n    >>> lhopital(cos(x), x, 0)\n    1\n    >>> lhopital((x + sin(x))/x, x, 0)\n    2\n    \"\"\"\nexpr = cancel(expr)\n    expr_num, expr_den = fraction(expr)\n    expr_num_eval, expr_den_eval = expr_num.subs(x, x0), expr_den.subs(x, x0)\n    indeterminates = [(0, 0), (oo, oo), (-oo, oo), (oo, -oo), (-oo, -oo)]\n    if (expr_num_eval, expr_den_eval) in indeterminates:\n        return lhopital(expr_num.diff(x)/expr_den.diff(x), x, x0)\n    return expr_num_eval/expr_den_eval",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Integrals"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Recall that the mean value of a function on an interval $[a, b]$ can be computed by the formula\n\n$$\\frac{1}{b - a}\\int_{a}^{b} f{\\left (x \\right )} dx. % Why doesn't \\, work? $$\n\nWrite a function that computes the mean value of an expression on a given interval."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef average_value(expr, x, a, b):\n    \"\"\"\n    Computes the average value of expr with respect to x on [a, b].\n\n    >>> average_value(sin(x), x, 0, pi)\n    2/pi\n    >>> average_value(x, x, 2, 4)\n    3\n    >>> average_value(x*y, x, 2, 4)\n    3*y\n    \"\"\"\nreturn integrate(expr, (x, a, b))/(b - a)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that takes a list of expressions and produces an \"integral table\", like\n\n1. $$\\int \\sin(x)dx = -\\cos(x) + C$$\n2. $$\\int \\cos(x)dx = \\sin(x) + C$$\n3. $$\\int e^xdx = e^x + C$$\n4. $$\\int \\log(x)dx = x(\\log(x) - 1) + C$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef int_table(exprs, x):\n    \"\"\"\n    Produces a nice integral table of the integrals of exprs\n\n    (note, we have to use pprint(use_unicode=False) because unicode is not supported\n    by the IPython doctester)\n\n    >>> int_table([sin(x), cos(x), exp(x), log(x)], x)\n      /                      \n     |                       \n     | sin(x) dx = C - cos(x)\n     |                       \n    /                        \n      /                      \n     |                       \n     | cos(x) dx = C + sin(x)\n     |                       \n    /                        \n      /              \n     |               \n     |  x           x\n     | e  dx = C + e \n     |               \n    /                \n      /                            \n     |                             \n     | log(x) dx = C + x*log(x) - x\n     |                             \n    /                              \n    \"\"\"\nC = symbols('C')\n    \n    for expr in exprs:\n        pprint(Eq(Integral(expr, x), integrate(expr, x) + C), use_unicode=False)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Now use your function to compute the integrals in this Mathematica ad.  Remember that the inverse trig functions are spelled like `asin` in SymPy. \n\nThe ad below probably has a typo, because one of the integrals is trivial to compute. Include what you think the integral should be, and see if SymPy can compute that as well."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "from IPython.core.display import Image \nImage(filename='../imgs/Mathematica-ring-a.png') ",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "png": "iVBORw0KGgoAAAANSUhEUgAAANAAAAEECAYAAABZfLr5AAAACXBIWXMAAAsTAAALEwEAmpwYAAAK\nT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AU\nkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXX\nPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgAB\neNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAt\nAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3\nAMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dX\nLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+\n5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk\n5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd\n0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA\n4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzA\nBhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/ph\nCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5\nh1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+\nQ8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhM\nWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQ\nAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+Io\nUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdp\nr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZ\nD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61Mb\nU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY\n/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllir\nSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79u\np+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6Vh\nlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1\nmz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lO\nk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7Ry\nFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3I\nveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+B\nZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/\n0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5p\nDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5q\nPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIs\nOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5\nhCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQ\nrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9\nrGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1d\nT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aX\nDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7\nvPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3S\nPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKa\nRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO\n32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21\ne2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfV\nP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i\n/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8\nIH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADq\nYAAAOpgAABdvkl/FRgAAv9BJREFUeNrU/XmU3dd134l+zjm/4Y41YAY4AKRAQuIgkwJlDaZE+knR\n4FB2EktO6HbiKN2hYrcT97O0Vi9bK89Wr5bc3ZH8nuN+K4nciSy3bTqW7I4tilLLUgyKjGiJhEjJ\nJEQCEEVwQGEq1HCn33TOeX+c87tD1a1CjVDeXeuiClW37v0NZ5+993d/93eLNF20bPihgICr+zBA\nG2sLQKzyuo2eVgMhom0/C2tbQL6GF679jISIEaJ2heuyFceeg+1gMVv6WUKUXycBeZXXlcbazrrX\nTWCt3cRCtv5ExVU8UeGfFqxd5+naofewY97X+kUdXgUD0oAevXZ2I6Zvx9yT7T72wh//+o5WrPif\n8n3xG7K4Kucx+tkpUKzbcIONHaj1T+09wdX2QmroGJYfmt2UB0qB6lW4YcYveMFG7MWO/cXVMqDc\nG9DQZjZyHnasldghT2PNwOOMWJAIrrrxuHWcDF3DdRnQpi6l30XVVfZCEdAbPVk7fNk3cwOKMQti\nezYBa3PAugVlBwtqY0GBuUrRQHnP7ZJrbdccRpfnN+485VUIn5cfTzK0ma07hDMbvIjl1wJr5VX2\nQuXOZ65wYdYSuo1778wb6XbeNPxCdLuxRbD2cHql89j+0MdFHIU/Vrsld3LwnxBrr3b4VnqfjW28\nweYP1iJEjrVX2wvFfqHbZZm23RSwYLG2uApAgl2yA9t1/e3WgSYbWXB6aPMS6zB2Me4q9DdDQXyV\n1xBY213HuWxpCGeHnoXfTa+mF4pGjWfLQjhYEzq2ZeHQuJ9tZBGZq2RE2l8ftcZrbddg5HZrMooN\nhevppq5bsHnjKRPD9Cp7IQmEYNOVIu1NLOrshwuEbBjYuRrXPt8Gj2eBGCHUD8H7LAVDrkoIZ5fk\nQaUXyrc9dxh9VLD0tsErmCFwZDvzOMvqCJZlOcq10vfmKuzg2iNwFiHMKhnNeo3ZIETM1az9uFpW\nAsIuOWZxtQxoqSeyCJFgbXgVvVA8BCZsRfJphxZKhhDbCWfbMZvRSr+HUfzaLskhylx0uwEEQ4lS\nuvxNjD1mhyoO0MXyZ+Pf0yLE1QahADpYCrDSXbv+6dirYUDLjWfghTK/sK9WGBcD3a0JKfp5lEGI\nYpuPfTUPJEaMxV6RcXG1kCvjoXexiuHTR9KGjWxlgNH48C28aqZjbTaEvLnN1yI2VD8Its54Si/U\nxdroqnkhIaqegiE2nkcsQ+7MVciDVH9hCWGXFEjtOs/F+lLCdl/zHGvNGnIVu/Zjt1z18M1tuMOs\nA/vDCOGGq7bDRqSBhKtRzXeP0F8Is8qOw0g4sbZdqvBx/nbdWNGvpYwe1xJvZAc5kF0GBw+DOME2\nG5DF2qwfdo072hVTolXvi4KrWDy1NvXgwdJ8c2PAyCYMyIz1Ru7i9oDKVfJCyhtra3SxL/Eqg5su\n1njh9FWrB42GbGVIMewNV9vdr074Zq3xfLGlOdgqlmNXD15L8EBcNQOyWNv191UuyS83tlY3aEDL\njWdQmS4JmT2gdjWCOG+si6xenBwXt9tVESfn5rfn5vbDIDsMBKx2XHbV7zfGKNlI/rPSdRVjDHo1\nTpwdiiCuTrjvjr+zyia6oUKq2bA1l387ajzl4uv6hb39sa0QIdaG/gJJtqa2on0etF2bgBxC0Ta7\ngEokazsfZbFcrnBd18+JA+XbL65W+Fa2waghe1kPzWuLQQRrxwEK5SPzXqh+FS5N4MO4dMt2sxKy\nFVeXWbIBgy9vfLitRmRt5vIxsXXnJ0TgAYSrhbwNvE+5dEV5QmJj4fCGc6BRrzNsPGaJF6peBS8k\nfKglV1mIq+U7Sy6cLdGYctdV23RT7YaT15UBne3KHdI+lLH5e+W+Xi3jGXgf7QxGjNmm7Jpwj+UG\nJGUda8cbhENJzOjPrfX2a1fxPiXKlCDE1fJCkX9mG9jRl/LpbN+AXMK5PQYkRIS1vY3ZzFIoYVs9\npR0CENaGZo5DPYVgaF1JhKhfJePJMKY9MH9/YGLEpkvPtL4LKZfvZN5I+sbDCFBgx9J4lj6H/669\nzbvjYDG6YpxZ92K05XPpr0zpgbbrIdfmXIaP0a60bW0fD3G4A3WtpYBxryuPvwx+rhb6Zu3i2HXh\nVzXWbuoOLrkVyzo6bf8Gjg/VVtseha/4JlfJUa8DtFjBaEZfUjKPr1KeY5cb9Jq6bqz1XnK7DGjr\nr4GU1atkPCnG9K4YhYz2jq39GbgFVww7awa8qqUh2zjkZdx+aJftAEJcDUSugoNF05U/y66vi9/a\n3F+LrV+cAomxW26G27IIr7RLr7egKkTjqhiQMYtLooiV7uWGmQjRkAGVZEA7lOTadVjm4D0GHkt4\nD7T9uZCDswOsTcf0269joQ291qE32lf6t/qAw62zHru9BrQpI15Sm5My3p7rOdbwk1WMZfT/1l4Z\nJJGq6gEQiRAS6WLncEzItlrBcSUmsR2Kc4cNS2DtAlejYi5EdbRIuYZQbeWwTnr6iuaH/lglH3In\nHmzTIjQYk2/piUhZ52poNxizCDZf4eaPr1etxUWMnIv7ZsAnGzCuVvM+jAnprpSM5R6H324DqvuF\nb9dnNCsambn6BnQF4GD8Y7t6l7K1ZmJrDlyvRvHU2p6j7Xif0t/Y7WoXXazzJsnSgCQulBNj2MB2\n/Da45JYup9CM81qLV8ELqf65bBZEGHjV7QISgvGehc1ow231Qsy28P0tUlbY3kZFt+lp3fYo6nIa\nkd1s2a2/EVSGM+1wKJRbyWhWWoj2CsZTZpI51ravkhda0UuvPaTrAwnZtixSIdTakbYf0sOYbOUL\nOTYqWSXwsQYp69tOO7I2cYzrVT7H2tVSk7VsVSFCVByVR/Qz7ooHFAqWw9ErUWtLMoQdC7sshQeF\naCNEc1tjYEENgwQxRrhwRTbKSso+glJ4YutvvPDX3m5isVgcp0wO3cetBxDEsqsmxvxXrHqcQiqk\nrGzLcQ7fPK3L2qNaHRhcVoEWVzw2IVwRuMzjlqyIssOTJeHZGqr44ySLxuiyOVRrm72QUD5UWE/C\nsZJ3Ej6EM9ti6lvlybZjV3fFU7uqb7FDYdG452AZWd8iv73om6v7dLhSyWSjXt+1oNf6KOKYT4lG\nULnlrs6ugszZkTBp/OuMN6DtZSdcuc5gGS4Sr3ZB3WLIt+EYNwhjj4uO7PYsRjbZJjG0DSNldZuV\ndyxaL2zuaK+wUzgPWhlxOWMeNbByldxmZeO5cn4hgeQqIHJl4XaFfG4duZBz9+l2mPm6jGUlRG6r\nVEKX5z+pn8CwFbDi9lN3Bt5nHR2mdhQY6P/XxWoglCsRiBAhKz6/FlcyIAl9qHEt4dtSr3OlpMx6\nL7R98LAQEilqjKUqbaAuZGzKtqf6S4zli198hH/8wf+Rd7/nn/Af/+ThFf/ItQVsRwiXew+0+X4l\nt3NvL/u6KOaX3CKxhiOzA2RuaAGPqg6V+XttWQF4lYA0RohsCVt4dbHwtT8k2B7W9jZM6Th+/DjH\njh2j3W7TarU4e/YsBw4c4OjRo9x///0uIZR1bLHoEsN1GM3yMxVYk27TbZdjZx3963/9Wfbt282/\n+Bc/z8MPP8Kjjz7Jz/zMT6zi1eUWG49xJNJNm4/tC4dsJ/pmjFtPo6DA+o7eLoNKBn8vRIyUy+tX\nwerhRc0jUHrF9Guj84VcatXyieX64uJPf/rTPPTQQ3zyk5/k5ptvHjGqj33sYxw7dowPf/jD3HTT\njQgRDI3iuHL4u/KvjefFbW0Y4o5vVELr0Uef4KmnTvCZz/yvANx55y0AtNsdGo06K9zjrd7P13bd\nrmiIjimv1GDxtVotms3mlh6t1vMuwe83yI3b9MW6wug+tUcEK7InrrAlBEMewq6Cvq2/hVoI6avF\n62Nqf+pTn+LBBx9cZjwAR48e5ZOf/CQnT57kIx/5CO1218esdk1h2pqS6i2Pk5bflK9//Un27du9\n7Of/4T98nqeeOrGOq7zJ8A09BKJc+Tm+BGQRIkSImFarxcc+9jFOnjy5xd6ni/ERwjAquBwZGvfD\npVQ0uyQzEUhZWzH8XINPjX1CfiVh8PXd1jLGdBy5tSWqx48f56GHHuK+++5bZjzl4+abb+b++++n\n1Wrx6U//rkNMtqSgyhZzwgY3aOnj0UefWPazP/mTh3n44UdWiBXUlodwxmRDU+jWDw6WvTYg+yWF\nhx56iGPHjm0D8lb2+4jxx7OuavUonVSIECkbq7iYNcToQjR8NT5jfJF0HcazpEhZVo3Xkgs99NBD\nANx7772rvu5973sfDz74IA899BD/9J9+kFotwpicTqfLt4+f4G1vfyMADz/8CO12h7e97Y3s3798\nx2+3O3z960/SbnfYt28399xz96qf22q1eOSRR/ohytGjR9m/f//Ia06ePMnx48f7HvPGG3egh9Zp\n6WHa7e6Itzk3cxGAU6dexFpoNGq0212sNShVJwgmOXDgwLLPK49reNcfft3x48c5efIkN998M0eP\nHh26t24G0GOPHeemmw7RaNT40pce4fDhQ/2QsjT2c+cu0mjUedvb7hoNMS0IqVCqzszMDGfPnu1f\nA4BmszmyES69NittkktzH2OSNRl3/5iWRW8rxcESpSZXDfPUv/yX//I31pT0Y1nbKAixrjzDGWGO\nlFdmJ3zsYx8D4Fd/9VdXfV2z2eTP/uzPyLKMI0dex8GD1/A//8//H/63/+3f8/VHn+TNb/4R/tW/\n+j949tnTfPWr3+CrX32ct7/9jTSbg5t/6tSLfPzj/5Y777yFRqPOb//2Z5mZOc9b3/r2sdXqmZkZ\nPvjBD3L06FF27tzJn/7pn9JqtfqLstVq8dGPfpSTJ0/ylre8hSzL+M3f/E1mZs5z6603EkURjz76\nBP/pP32Vc+cukmU5585d5NlnT/Hss6c4deoM7XaXdrvL6dMvIgRkWc7v/M7v8/DDXyOKIm6//fZ+\nbvGzP/uzvPWtb6XZbJJlGY8//ji/+Zu/SZZlHD16lJMnT/Kxj32MZrPJsWPHePDBB9m1axc333wz\n1moefPAP+Y3f+G2+9rXHufXWm/id3/l9vva1b/C1r32Dn/u5n6Ld7vAbv/GvaTbrHD58iM997kt8\n7WuP87a33UUURf1lKWVEEEzx4IMPcubMGWZmZti/fz9Z5lrvDx06tOK1OXv2LLfffjtxHK+4oIpi\nDmPSDQAUYvDvMhaFS0uCYGIZcFDe+/LrGg2oVL7MgWJDQ6xWZgKJfr/NajDn8ePH+cpXvgLAP/7H\n/3hN4d7MzAxHjhzhtttu4e67b+Gb3/wuly/Ps3//bn75l3+en/iJe4jjkG9+8ztEUcQb3nCLN4aL\n/Mqv/C/8D//Dz/PmN9/BwYPX0GjU+IM/+HNuu+11HDhw7VhgI45jfumXfolDhw5x11138dBDD/Gu\nd70LgI9+9KOcPXuWT3ziExw6dKi/u/7xH38OLNx5560cvP4a3vGOt/KHf/jn3HrrTXziEx/hHe94\nK+94x1vJ85ynnjrBRz7y3/FzP/dT3HrrTdx00yHa7Q4nTpzmfe+7r2+sx44d46GHHiKKIo4ePUoc\nxxw6dKgPvLz44ot85CMf4Zd+6Zd43/vex7333stDDz3E888/z0//9E9jbcZrX3uAVqvNiROnabe7\n/NRPvpObbjrE4ZsOcucdt/CRj/wmb3rTHXzgAz/B/n27ufPOW/gPn/k8zWadW2+9yec+AqUmkbLC\n0aNHmZ2d5fjx4zzwwAO8613v4tChQ6temwcffLDvjVbyPloveOBNbMiAypLPsNgJuIKplFPLNsul\nBrQOs5UIMeEKrOvp4rJXgLlteTG2r19IiBgpIhoNt5sMw8Hl96dOvTiSb7TbnX5I9dRTJ2i3nRzs\n889/b+xnzMzMcPLkyX54sn//fj784Q/3F/Tx48c5evToCPrk4Hb4k899iZlzFzd09m9721G/YXx7\nZPMYDnnLn91zzz00m80+3F+GwmUoNTMz4zc7jTFFPxy7445buPttd/H+D7yXD37w/XzpS49w6vQZ\nf32e5amnnmVm5sIgBPXJpUCg1OpNlFe6Ng8++GD/uJbC7EXRwhjtgJgtXToCpabW5NXW6fciEM1l\nrm4l73PFJH2k87PwyinjHwcOHBiJldf62L9/v4Oe11HEe+qpEzQadf7jf3yYr3/9CU6edMb1T/7J\n+3m7z5+WPu69915arRYf+tCH+NSnPtUPVYaPd/gcyscb3nDHisDBlbN1y+HD17N//96+0bRaLWZm\nZrjvvvtotVp9Izp+/Djve9/7+tfkk5/85EhuOXxNlzYRHj58cOTj+8bz9Am+9GVnTKdOn+GDH3w/\n73//ewdtlDK6Yufpatdm2KMuN6AEYzougoHlPT927WmGHSlgG5SaWHO5Ilj/bt7AUXF6q8LYV/I6\ndtkJGaxtAY2x7nj//v3s37+/v9NfKcEsb8yRI0e8S167Ac3MXOTOO2/hN3/zI8sxsxUMsVywJXjx\n0EMP8eEPf5j77rtvc7CtXbbTsFT25e1v/zH+43/8s35h+d5772X//v089NBDHD9+nPvuu4+ZmZmR\nazYzM8Mf/dEf0W63+wm7M0KLMcWqe+u5cw7Q+PjHP7zqoSt15VrPRq6NtZaiaA/NFloPYDAeNBjw\n9Wqrom6b9EDlkUwyOhpifSHbSoLkTr+rtSq6ttKOtPSmlAl86QUcDWNtTXaNRt2HbeP4emZFYun9\n99/PH/7hH3Lffff1a1bDnqhEocY9+nUfO25rHN9xM4DuX9P3MseOHeOee+7pn/uxY8c4duzYMuP5\n0Ic+BMCv//qv94+3DN/KKQwrPcpQ+NFHn1x1naxFeWct12YpsmhtgtbtNbVFLIOyVysoCIe6rYfw\nuqHigdNgm1xev7lSNX/V3wt/81YelnXfffexf//+fj1opceDDz5Is9nkgQceWAKCXJniDoPK/5/8\nyZfGQsLjDKhECJvNZt/zlAujzDXKMGvU252n0ahx5x23LLvLaytfKO655+00m00eeeQR9u/f388l\nyg3nt37rt0ag/2PHjtFqtcaWA1z+k62alB8+7JL/z33u4THQf9d7n7Uxr1e7NmfPnu2XA0aRtwVG\nmNPrcearIMVSTqwrUtmwAQ1CuRoDgfnV283XpmZZ1oV6K8LTv/Ebv8H+/fv59Kc/PdYTPfjggxw/\nfpxf+ZVfGRPmyX4IsNpx/czPvLcPJvzrf/1ZnnrqBI8++gQf//i/YWbmvF9gy1G/4UXQbDb7N79M\n2GdmZvrI0jBS+MEPvp96o7am9fDlLz8yEkYJJALBPffcQ6vV6htNueE4j9EYuRalgT300EO0Wi2O\nHz/e9wDHjh3j3Llzqx7De997D/v27eb06TN89KOf4tFHn+Spp07wO7/z+z6XsyjVWHGhlpvfzMzM\nFa/NAw88MAIuGJOidZcR+YEROsT6TKlcvELEKDWxbjtYM4w9PpQLgJ4XYhfrDNlW8lLG7wa1se+5\nc+dO3vWudxHHMb/7u7/L8ePHmZ2d5ZlnnuGzn/0sAL/2a7/G7bffPhKyfPrTn+aRRx4F4MyZsxw+\nfIhWu8snPvFvOHfuIufOXeTy5Xne9KY72LlzioMHD/DUU9/j2WdP8bWvfYPTp8/wz/7Zz3L48PUI\nES5Dl1qtFr/7u7/bX5DHjh3jE5/4BDt37hxJiD/72c8yOzvLmTNn+L3f+z0eeOC/493vfiMgeOqp\nE/zv//vvDx3PAgcPHqDRqLNz51T/OP78z79Ko+HgYoFAqjp5bjl58uSI143jmNnZWY4cOTKyi998\n880888wzPP744zz00EMcOHCAe++9l0ceeYSZmRkOH76eL3/56/z5n3+VLMs5ceI0WZZ7eBqiKOTW\nW2/i1KkXOXHiNI899iTf+tZ3eMc73sp733sPIAnDHcs8UAmlnzx5kq985SvEccztt9++4rX50Ic+\nNBJeAuT5xWXcwZX9yvj2Y7H0d8Idr5TRmjb5ka9pmtrhXXm95FBj5rB2ntU7UtdkOSPRfhDsW5N6\nS5nvrFYvGL0B5zCmu+a6QQlv33T4UH8olJRVwnD/shi8rLYvrbAvNbQycT569CjWatL05TXN92m3\nu5w69eIIEwAkUbS7X+1fmi/MzMzQaDTGkjdPnjw5EvKdPfsqu3YF6KK9ZrHtc+cu9kGXcsdUqkEY\n7hmbo5TnP+5eLb024+o+aXpuTXHb2ozJUU9VMEEQ7Fhj5LXFBgQGYy5gTG9wwdbldeyYaXIGKRsE\nwW62nuPVIs8vsSYa89jWBkeOjKK9W8LMttaQZWfHhoVruXZSRoThnnXH7uOPpSBLZzCb6b61hija\niwq2lm0NkKUzaNPb0N+KZcYkhu7lgTUzGTZRSF05jRJicoD3r9l4BiL2S7TyPVO7sy3sZ+fV1ibq\nvuIAeqtXDCOu+sPCVs5E0maTw5VFiJBb3zhnTBe9iZ6swb0UfUMHQRju3FSfktyaRVlFiPraxQwB\nrFhiOKOzQq3Fs2ztFhvQKoIja9RlGyBV/7U87BYZULapMSmuCFndhpH1lqIYP2Fho4Zk+1y3yqbe\nb8viI8cbqqzxQi/1OqWo93A4JzCms+5+oTUhJ6qxouGsba3aLfVAbsHZjf7xFslE2S3ZFLZDtkrr\nLlpvxToQ/bRDysoVmdZX1YBc38f0WqK2FXZNO+SVhi/e/DaEcV5wZCSEXIvVD8tz5evul1n5pm7s\nNrjDkWyFVJS1XkTRig2/gRTRluRio2/rdd625FqX2gZqLEr4QzYgtzClnBy/m65aJ7JYK8ZMqxYY\nMzzfZauO0wnj2TVd74HhjCrh5P+V5EFyy3IgY5INv5XFIlW8Jih4fcfUc3WfLfNqFqWamw7dtsWA\n3OKcRBCzstLnEnc6kjeNm89iMGarvVDJErarG84Stf5Rwy5gCwyoVLq0P2RtXzcKxGzwb8sIpMJW\nCjRYa9C6tUWe3t1YKSsEwdSWHec2GJBEqunBvmTHj4Uo3bNdpuFlx+xCmdf72srjLJnCdlXDWfle\naMyWeCCx6Vk5W5FzuKa0zSzMcMt29YEBJWjdWS6guwkAKQynt1TccVt0hspQbsWakhVDult2FEQY\ns8Cs1WjdYisROYfG1QciEms1nCHX4ThxP0zXYbdsMbj8h409KbUD4i00HktRtNz92SKnJmVjrDTV\nZh7bJFQsEKKJED1fy5ErhHN2FcNZvhsZ0/XyQltzjG7HnO8bztLH6dNneOqpE5w+/SKHDx/iAx94\n75IwLsNas+FFPDMzw7Fjx3juuWd5zWv28YEP/MQPzRSdCunGHo89dpwLF9o8/fQJ7r//fo4ePcqx\nY8eYmZnh+PHj/Z+t1/sURXvLED1XcJ7elgx0e0xIhCg5TTm4a3XjWX02peh7ofaW7vhSOtRoterV\n6dMvrkDb9x5ok/H52bNn+frX/8t6gaRBn9AW5RqbA0Qkjz7618sY1WW36UY8a54vbOVq3DLU7aoZ\nEIAYak4aX2RdaVQkYzyW8PpfvS01cueFxifPhw8f5D3vuWfl22wKP8l77Y+Stweuz+VKCkOrzxhU\nW7IoNsv4uOeeu7n33h8f+dm999575XNbxRtq3XVMtU3vESXqtj1T8bZ7bDZSTnvOmB2DwomVvc+y\n4qbrWnWojNmynckZ0AbrMP3uzbU9jh07xm/91m+tYikrG8z41ENsiQFpnWzimorlhelNPvJ8bh2b\nyOqbjxTxtoRuV82AXLJeus81ijOu0rW61ewEKWOf/NoNnJvAmGTNBNyPfexjIx5o6a2wdr1rZmtC\nuM0wEFwX59bt7q7uk6x+DdZgTNZnBsE2hW5DIMK2iSsPLdIaxtS95sEVFsAVu1adFxKickUS4HBr\nd9nEVfaXHD9+vN+V6TxkQrvd67cvjLYMjH+cO3eJxx77CkpNcNddb1xVp2FY9KP8fvT17h6cOn2G\np58+QaNRWzF8PHfuIo895vKyN77xLbzudW9Y8bxLoGJpuFgKKh49epTrrlubATz99AlOnz7D4cMH\nueOOW/y9rW6haLwlz+dXtIxxMcz4H7pfBMH0lhr3WAOytr3hCQnreSi1w2th50OOT4yELmua1SME\nRnewasIL049frKUewQMPPNDXSSsff/RHfzTSDSllhT/+48/xuc89TLvd5YMffP8VDehLX3qExx57\nkve//728+OI8H/rQh0ZauZeGbqU003DPy7ABnTt3kY9+9FP978+du8iXvvQIv/3b/6+R9/ryl92k\nhg984L2cPv0Sv/iLH+5/bimu32q1eOCBB/pGcvbs2b4Yy7333suDDz44Ysi/+qv/PXfffeeKG+nT\nT5/gM5/5PG972xt59NEn+MxnPs8//+f/iPe85+1bukCLor0uzpsdbzdYLEpWCIKJbV/XcjBycXvr\nGc7VT4/3wevpH/J8uX5f/JjH0aNH+52Zx44d48CBA3z4wx/m3nvv5Z577uGP/uiPlhh3jb//93+S\nf/7P/9GaDuHRR5/kM5/5PL/6q7/AnXe8jn/wD/4e9913H5/+9KfHhmj33ntvX+fswIED3H///dx/\n//0jTW7nzl3kV3/1F/j4xz/Mv//3/wt3330Xp703Kh+PPTb43DvuuIUPfOBvc9997+1/7tGjR/mV\nX/mV/nm/733v45Of/CT/7t/9O/bv38+DDz7IF77wBX7lV36l/3OAz33ui6saz0c/+ik+8IGf4P3v\nfy8f//hHaDRqfO5zXwLUlhlQqfO2Ucb18IoSCFQwuekC9Vo+VZYojBPz2G5AoY6UzdGEdQPDrgaI\n3Mq7Vbk4m80m999/P/fddx+//uu/PrYz06mihn21mSs9PvOZz7Nv325OnXqRp57+Hk8++eQy77Le\nx5133k6jMfCob3ub05877TXYhj/39OkXefrpEzz11LPLPrc8v1LaqvxZqZVw77339l9z8803c+ed\nr+f06RdXPK59+3Y7YcW77wKcIs/hw4c4d+4igapvWZ1G646/n5sf5qWCJkFQ3/b1rHWHwAl5GC/w\n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\nRU5ErkJggg==\n",
       "prompt_number": 4,
       "text": "<IPython.core.display.Image at 0x1023b7f50>"
      }
     ],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "a, b, c, n = symbols('a b c n')\nint_table([x*atanh(a), a*x**n + b*x + c, csc(a*x)*sec(a*x)**2, x*atanh(a*x)], x)\n",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Limits"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Recall that the definition of the derivative of $f(x)$ at $x=x_0$ is $$f'(x_0) = \\lim_{x\\to x_0}\\frac{f(x) - f(x_0)}{x - x_0}.$$  Write a function that computes the derivative using the limit definition, using `limit`."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef lim_deriv(expr, x, x0):\n    \"\"\"\n    Computes the derivative of expr with respect to x at x0 using the limit definition.\n\n    >>> lim_deriv(x**2, x, 0)\n    0\n    >>> lim_deriv(cos(x*y), x, pi)\n    -y*sin(pi*y)\n    \n    Note that we must use this trick to take the derivative without evaluating at a point.\n    >>> lim_deriv(exp(x**2), x, y).subs(y, x)\n    2*x*exp(x**2)\n    \"\"\"\nreturn limit((expr - expr.subs(x, x0))/(x - x0), x, x0)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "The function you wrote above to compute limits using l'Hopital's rule is very fragile. And even if you try to make it sophisticated, it will still be unable to compute many limits.  Try it on the following limits, and see what happens. Then try computing the same limits with `limit`. \n\n1. $$\\lim_{x\\to 0}\\frac{\\log(x)}{x}$$\n2. $$\\lim_{x\\to \\infty}\\frac{2^x}{3^x} \\textbf{Warning: Be sure to save the notebook before you test this one, and be prepared to kill the kernel!}$$\n3. $$\\lim_{x\\to \\infty}x\\sin{\\left(\\frac{1}{x}\\right)}$$\n4. $$\\lim_{x\\to 1}\\arctan\\left(\\frac{1}{1 - x}\\right)\\; \\text{Remember that $\\arctan$ is called }\\mathtt{atan}\\text{ in SymPy}$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "hopital(log(x)/x, x, 0)\n\n",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "limit(log(x)/x, x, 0)\n",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "NameError",
       "evalue": "name 'limit' is not defined",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-2-c06b53409f43>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlimit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mNameError\u001b[0m: name 'limit' is not defined"
       ]
      }
     ],
     "prompt_number": 2
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "lhopital(2**x/3**x, x, oo) XXX: Don't run. This hangs the notebook\n    \n    ",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "limit(2**x/3**x, x, oo)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "lhopital(x**(1/x**2), x, 0)\n",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "limit(x**(1/x**.5), x, 0)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "lhopital(x*sin(1/x), x, oo)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "limit(x*sin(1/x), x, oo)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "lhopital(atan(1/(1 - x)), x, 1)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "limit(atan(1/(1 - x)), x, 1)\n",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "NameError",
       "evalue": "name 'limit' is not defined",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-3-4c10d37ef4b6>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlimit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0matan\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mNameError\u001b[0m: name 'limit' is not defined"
       ]
      }
     ],
     "prompt_number": 3
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Series"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "The Fibonicci sequence is rexcursively defined by \n\n$$F_0 = 0,$$\n$$F_1 = 1,$$\n$$F_n = F_{n - 1} + F_{n - 2}.$$\n\nThe first few vales are 0, 1, 1, 2, 3, 5, 8, 13, 21, \u2026\n\nThe Fibonicci sequence has a generating function given by $$s(x) = \\frac{x}{1 - x - x^2}$$ (see http://en.wikipedia.org/wiki/Fibonacci_number#Power_series for a derivation). What this means is that if we expand $s(x)$ as a power series, the coefficients are the Fibonicci numbers, $$s(x) = \\sum_{n=0}^\\infty F_nx^n$$"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that uses series to compute the nth Fibonicci number. \n\nHint: `expr.coeff(x, n)` will give the coefficient of $x^n$ in an expression. For example"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "(1 + 2*x - x**2).coeff(x, 0)",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 7,
       "text": "1"
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "(1 + 2*x - x**2).coeff(x, 1)",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 8,
       "text": "2"
      }
     ],
     "prompt_number": 8
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "(1 + 2*x - x**2).coeff(x, 2)",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 9,
       "text": "-1"
      }
     ],
     "prompt_number": 9
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef fib(n):\n    \"\"\"\n    Uses series expansion and a generating function to compute the nth Fibonnicci number.\n\n    >>> fib(0)\n    0\n    >>> fib(4)\n    3\n    >>> fib(9)\n    34\n    \"\"\"\ns = x/(1 - x - x**2)\n    return s.series(x, 0, n + 1).coeff(x, n)\n",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "IndentationError",
       "evalue": "unexpected indent (<ipython-input-4-69c81548302f>, line 14)",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-69c81548302f>\"\u001b[0;36m, line \u001b[0;32m14\u001b[0m\n\u001b[0;31m    return s.series(x, 0, n + 1).coeff(x, n)\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
       ]
      }
     ],
     "prompt_number": 4
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Note: if you really want to compute Fibonicci numbers, there is a function in SymPy called `fibonicci` that can do this far more efficiently."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "[fibonacci(i) for i in range(10)]",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 5,
       "text": "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"
      }
     ],
     "prompt_number": 5
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "`series` is nice if you want a fixed power series, but what if you don't know ahead of time how many terms you want? For that, there is the `lseries` method, which returns a generator of series terms.  This is more efficient than recomputing the whole series again if you determine you need more terms. Here is an example usage (**Warning**: since series are in general infinite, `lseries` will return an infinite generator. Here we use `zip` to limit the number of terms)."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "for term, _ in zip(cos(x).lseries(x, 0), range(10)):\n    print term",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": "1\n-x**2/2\nx**4/24\n-x**6/720\nx**8/40320\n-x**10/3628800\nx**12/479001600\n-x**14/87178291200\nx**16/20922789888000\n-x**18/6402373705728000\n"
      }
     ],
     "prompt_number": 6
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Write a function that computes the number of terms of a series expansion of a given function are needed to compute the given value near the given point within the given accuracy. For example, in the expansion of cos(x) near $\\pi$, suppode we wish to compute $\\pi + 1$. Let us see if terms up to $O(x^6)$ are sufficient (remember that due to a limitation in SymPy, when computing the series away from 0 with `series`, we have to use a shift)"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "a = cos(x).series(x, pi, 5).removeO().subs(x, x - pi).evalf(subs={x: pi + 1})\na",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 10,
       "text": "-0.541666666666667"
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "b = cos(pi + 1).evalf()\nb",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 11,
       "text": "-0.540302305868140"
      }
     ],
     "prompt_number": 11
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "So the expansion is accurate up to two places after the decimal point, i.e., within `0.01`. "
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "abs(a - b) < 0.01",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 12,
       "text": "True"
      }
     ],
     "prompt_number": 12
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Note, with `lseries`, we do not need to worry about shifts"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "for term, _ in zip(cos(x).lseries(x, pi), range(10)):\n    print term",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": "-1\n(x - pi)**2/2\n-(x - pi)**4/24\n(x - pi)**6/720\n-(x - pi)**8/40320\n(x - pi)**10/3628800\n-(x - pi)**12/479001600\n(x - pi)**14/87178291200\n-(x - pi)**16/20922789888000\n(x - pi)**18/6402373705728000\n"
      }
     ],
     "prompt_number": 13
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Hint: to get the exponent from a term like `3*(x - 1)**5`, use `as_coeff_exponent`. "
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "(3*(x - 1)**5).as_coeff_exponent(x - 1)",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 14,
       "text": "(3, 5)"
      }
     ],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef series_accuracy(func, expansion_point, evaluation_point, accuracy, x):\n    \"\"\"\n    Returns n such that series terms up to and including (x - expansion_point)**n \n    (i.e., O((x - expansion_point)**(n + 1)) are needed to compute func at \n    evaluation_point within the given accuracy.\n\n    >>> series_accuracy(cos(x), pi, pi + 1, 0.01, x)\n    4\n    >>> series_accuracy(exp(x), 1, 10, 1, x)\n    23\n    \"\"\"\n digits = max(15, round(1/accuracy) + 1)\n    real_value = func.evalf(digits, subs={x: evaluation_point})\n    expansion = 0\n    for term in func.lseries(x, expansion_point):\n        expansion += term\n        series_value = expansion.evalf(digits, subs={x: evaluation_point})\n        if abs(real_value - series_value) < accuracy:\n            return term.as_coeff_exponent(x - expansion_point)[1]\n        ",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "IndentationError",
       "evalue": "unindent does not match any outer indentation level (<ipython-input-5-253204ec2585>, line 13)",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-5-253204ec2585>\"\u001b[0;36m, line \u001b[0;32m13\u001b[0m\n\u001b[0;31m    digits = max(15, round(1/accuracy) + 1)\u001b[0m\n\u001b[0m                                           ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unindent does not match any outer indentation level\n"
       ]
      }
     ],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "",
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}
