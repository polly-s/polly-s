{
 "metadata": {
  "name": "Matrices"
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
     "source": "Matrices"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "import sys\nimport os\nsys.path.insert(1, os.path.join(os.path.pardir, \"ipython_doctester\"))\nfrom sympy import *\nfrom ipython_doctester import test\n# Work around a bug in IPython. This will disable the ability to paste things with >>>\ndef notransform(line): return line\nfrom IPython.core import inputsplitter\ninputsplitter.transform_classic_prompt = notransform",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Use `row_del` and `row_insert` to go from one Matrix to the other."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef matrix1(M):\n    \"\"\"\n    >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n    >>> M\n    [1, 2, 3]\n    [4, 5, 6]\n    [7, 8, 9]\n    >>> matrix1(M)\n    [4, 5, 6]\n    [0, 0, 0]\n    [7, 8, 9]\n    \"\"\"\nM.row_del(0)\n    M = M.row_insert(1, Matrix([[0, 0, 0]]))\n    return M",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": "Matrix Constructors"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Use the matrix constructors to construct the following matrices.  There may be more than one correct answer."
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "$$\\left[\\begin{array}{ccc}4 & 0 & 0\\\\\\\\ \n0 & 4 & 0\\\\\\\\ \n0 & 0 & 4\\end{array}\\right]$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef matrix2():\n    \"\"\"\n    >>> matrix2()\n    [4, 0, 0]\n    [0, 4, 0]\n    [0, 0, 4]\n    \"\"\"\nreturn eye(3)*4\n    ",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "$$\\left[\\begin{array}{}1 & 1 & 1 & 0\\\\\\\\1 & 1 & 1 & 0\\\\\\\\0 & 0 & 0 & 1\\end{array}\\right]$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef matrix3():\n    \"\"\"\n    >>> matrix3()\n    [1, 1, 1, 0]\n    [1, 1, 1, 0]\n    [0, 0, 0, 1]\n    \"\"\"\nreturn diag(ones(2, 3), 1)",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "$$\\left[\\begin{array}{}-1 & -1 & -1 & 0 & 0 & 0\\\\\\\\-1 & -1 & -1 & 0 & 0 & 0\\\\\\\\-1 & -1 & -1 & 0 & 0 & 0\\\\\\\\0 & 0 & 0 & 0 & 0 & 0\\\\\\\\0 & 0 & 0 & 0 & 0 & 0\\\\\\\\0 & 0 & 0 & 0 & 0 & 0\\end{array}\\right]$$"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef matrix4():\n    \"\"\"\n    >>> matrix4()\n    [-1, -1, -1, 0, 0, 0]\n    [-1, -1, -1, 0, 0, 0]\n    [-1, -1, -1, 0, 0, 0]\n    [ 0,  0,  0, 0, 0, 0]\n    [ 0,  0,  0, 0, 0, 0]\n    [ 0,  0,  0, 0, 0, 0]\n    \"\"\"\nreturn diag(-ones(3, 3), zeros(3, 3))",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Recall that if $f$ is an analytic function, then we can define $f(M)$ for any square matrix $M$ by \"plugging\" $M$ into the power series formula for $f(x)$. In other words, if $$f(x) = \\sum_{n=0}^\\infty a_n x^n,$$ then we define $f(M)$ by $$f(M) = \\sum_{n=0}^\\infty a_n M^n,$$ where $M^0$ is $I$, the identity matrix. "
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Furthermore, if $M$ is a diagonalizable matrix, that is, $M=PDP^{-1}$, where $D$ is diagonal, then $M^n = PD^nP^{-1}$ (because $M^n = \\left(PDP^{-1}\\right)\\left(PDP^{-1}\\right)\\cdots\\left(PDP^{-1}\\right)=PD\\left(P^{-1}P\\right)D\\left(P^{-1}P\\right)\\cdots DP^{-1} = PD^nP^{-1}$).\n\nBut if \n\n$$ D = \\begin{bmatrix}\n         d_1 & 0 & \\cdots & 0 \\\\\\\\\n         0 & d_2 & \\cdots & 0 \\\\\\\\\n         \\vdots & \\vdots & \\ddots & \\vdots \\\\\\\\\n         0 & 0 & \\cdots & d_n\n      \\end{bmatrix}\n$$\n\nis a diagonal matrix, then \n\n$$ D^n = \\begin{bmatrix}\n         d_1^n & 0 & \\cdots & 0 \\\\\\\\\n         0 & d_2^n & \\cdots & 0 \\\\\\\\\n         \\vdots & \\vdots & \\ddots & \\vdots \\\\\\\\\n         0 & 0 & \\cdots & d_n^n\n      \\end{bmatrix}\n$$\n\nso that \n\n$$\n\\sum_{n=0}^\\infty a_n M^n = \\sum_{n=0}^\\infty a_n PD^nP^{-1} = P\\cdot\\begin{bmatrix}\n    \\sum_{n=0}^\\infty a_n d_1^n & 0 & \\cdots & 0 \\\\\\\\\n         0 & \\sum_{n=0}^\\infty a_n d_2^n & \\cdots & 0 \\\\\\\\\n         \\vdots & \\vdots & \\ddots & \\vdots \\\\\\\\\n         0 & 0 & \\cdots & \\sum_{n=0}^\\infty a_n d_n^n\n\\end{bmatrix}\\cdot P^{-1} = P\\cdot\\begin{bmatrix}\n    f(d_1) & 0 & \\cdots & 0 \\\\\\\\\n         0 & f(d_2) & \\cdots & 0 \\\\\\\\\n         \\vdots & \\vdots & \\ddots & \\vdots \\\\\\\\\n         0 & 0 & \\cdots & f(d_n)\n\\end{bmatrix}\\cdot P^{-1}\n$$"
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Let's create some square matrices, which we will use throughout the exercises."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "x = symbols('x')\nA = Matrix([[1, 1], [1, 0]])\nM = Matrix([[3, 10, -30], [0, 3, 0], [0, 2, -3]])\nN = Matrix([[-1, -2, 0, 2], [-1, -1, 2, 1], [0, 0, 2, 0], [-1, -2, 2, 2]])",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "First, verify that these matrices are indeed diagonalizable."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "print A.is_diagonalizable()\nprint M.is_diagonalizable()\nprint N.is_diagonalizable()",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "NameError",
       "evalue": "name 'A' is not defined",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-1-7fc2bcae2d1e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mprint\u001b[0m \u001b[0mA\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_diagonalizable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mprint\u001b[0m \u001b[0mM\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_diagonalizable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mprint\u001b[0m \u001b[0mN\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_diagonalizable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;31mNameError\u001b[0m: name 'A' is not defined"
       ]
      }
     ],
     "prompt_number": 1
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Now, we want to write a function that computes $f(M)$, for diagonalizable matrix $M$ and analytic function $f$.\n\nHowever, there is one complication. We can use `diagonalize` to get `P` and `D`, but we need to apply the function to the diagonal of `D`. We might think that we could use `eigenvals` to get the eigenvalues of the matrix, since the diagonal values of `D` are just the eigenvalues of `M`, but the issue is that they could be in any order in `D`.\n\nInstead, we can use matrix slicing to get the diagonal values (or indeed, any value) of a matrix. There is not enough time in this tutorial (or room in this document) to discuss the full details of matrix slicing. For now, we just note that `M[i, j]` returns the element at position `i, j` (which is the `i + 1, j + 1`th element of the matrix, due to Python's 0-indexing). For example"
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "M",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "M[0, 1]",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "That should be enough information to write the following function."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef matrix_func(M, func):\n    \"\"\"\n    Computes M at func. Assumes that M is square diagonalizable.\n\n    >>> matrix_func(M, exp)\n    [exp(3), -5*exp(-3)/3 + 5*exp(3)/3, -5*exp(3) + 5*exp(-3)]\n    [     0,                    exp(3),                     0]\n    [     0,     -exp(-3)/3 + exp(3)/3,               exp(-3)]\n\n    Note that for the function exp, we can also just use M.exp()\n\n    >>> matrix_func(M, exp) == M.exp()\n    True\n\n    But for other functions, we have to do it this way.\n\n    >>> M.sin()\n    Traceback (most recent call last):\n    ...\n    AttributeError: Matrix has no attribute sin.\n    >>> matrix_func(N, sin)\n    [-sin(1), -2*sin(1),      0, 2*sin(1)]\n    [-sin(1),   -sin(1), sin(2),   sin(1)]\n    [      0,         0, sin(2),        0]\n    [-sin(1), -2*sin(1), sin(2), 2*sin(1)]\n    \n    Note that we could also use this to compute the series expansion of a matrix, \n    if we know the closed form of that expansion. For example, suppose we wanted to compute\n    \n    I + M + M**2 + M**3 + \u2026\n\n    The series\n\n    1 + x + x**2 + x**3 + \u2026\n\n    is equal to the function 1/(1 - x).\n\n    >>> matrix_func(M, Lambda(x, 1/(1 - x))) # Note, Lambda works just like lambda, but is symbolic\n    [-1/2, -5/4, 15/4]\n    [   0, -1/2,    0]\n    [   0, -1/4,  1/4]\n    \"\"\"\nP, D = M.diagonalize()\n    diags = [func(D[i, i]) for i in range(M.shape[0])]\n    return P*diag(*diags)*P**-1",
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "Now lets investigate how this works in relation to the series expansion definition. Write a function that uses `matrix_func` and `series` to compute the approximation of a matrix evaluated at a function up to $O(M^n)$."
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "@test\ndef matrix_func_series(M, func, n):\n    \"\"\"\n    Computes the approximation of the func(M) using the series definition up to O(M**n).\n\n    >>> matrix_func_series(M, exp, 10)\n    [22471/1120,  14953/448, -44859/448]\n    [         0, 22471/1120,          0]\n    [         0, 14953/2240,    83/2240]\n    >>> matrix_func_series(M, exp, 10).evalf()\n    [20.0633928571429, 33.3772321428571,  -100.131696428571]\n    [               0, 20.0633928571429,                  0]\n    [               0, 6.67544642857143, 0.0370535714285714]\n    >>> matrix_func(M, exp).evalf()\n    [20.0855369231877, 33.3929164246997,  -100.178749274099]\n    [               0, 20.0855369231877,                  0]\n    [               0, 6.67858328493993, 0.0497870683678639]\n\n    It's pretty close. Basically what we might expect for those values up to O(x**10).\n\n    >>> matrix_func_series(N, sin, 3)\n    [-1, -2, 0, 2]\n    [-1, -1, 2, 1]\n    [ 0,  0, 2, 0]\n    [-1, -2, 2, 2]\n    >>> matrix_func(N, sin).evalf()\n    [-0.841470984807897,  -1.68294196961579,                 0,  1.68294196961579]\n    [-0.841470984807897, -0.841470984807897, 0.909297426825682, 0.841470984807897]\n    [                 0,                  0, 0.909297426825682,                 0]\n    [-0.841470984807897,  -1.68294196961579, 0.909297426825682,  1.68294196961579]\n\n    It's not as close, because we used O(x**3), but clearly still the same thing.\n\n    >>> matrix_func_series(M, Lambda(x, 1/(1 - x)), 10)\n    [29524, 73810, -221430]\n    [    0, 29524,       0]\n    [    0, 14762,  -14762]\n    >>> matrix_func(M, Lambda(x, 1/(1 - x)))\n    [-1/2, -5/4, 15/4]\n    [   0, -1/2,    0]\n    [   0, -1/4,  1/4]\n\n    Woah! That one's not close at all. What is happening here?  Let's try more terms\n\n    >>> matrix_func_series(M, Lambda(x, 1/(1 - x)), 100)\n    [257688760366005665518230564882810636351053761000, 644221900915014163795576412207026590877634402500, -1932665702745042491386729236621079772632903207500]\n    [                                               0, 257688760366005665518230564882810636351053761000,                                                  0]\n    [                                               0, 128844380183002832759115282441405318175526880500,  -128844380183002832759115282441405318175526880500]\n    \n    It just keeps getting bigger. In fact, the series diverges. Recall that \n    1/(1 - x) = 1 + x + x**2 + x**3 + \u2026 *only if* |x| < 1.  But the eigenvalues \n    of M are bigger than 1 in absolute value.\n    \n    >>> M.eigenvals()\n    {3: 2, -3: 1}\n\n    In fact, 1/(1 - M) is mathematically defined via the analytic continuation \n    of the series expansion 1 + x + x**2 + \u2026, which is just 1/(1 - x).  This is\n    well-defined as long as none of the eigenvalues of M are equal to 1.  Let's\n    try it on N.\n\n    >>> matrix_func(N, Lambda(x, 1/(1 - x)))\n    [nan, -oo, nan,  oo]\n    [nan, nan, nan, nan]\n    [nan, nan, nan, nan]\n    [nan, -oo, nan,  oo]\n    \n    That didn't work. What are the eigenvalues of N?\n\n    >>> N.eigenvals()\n    {1: 1, 2: 1, -1: 1, 0: 1}\n\n    Ah, the first one is 1, so we cannot define 1/(1 - N). \n    \"\"\"\nx = Dummy('x') # This works even if func already contains Symbol('x')\n    series_func = Lambda(x, func(x).series(x, 0, n).removeO())\n    return matrix_func(M, series_func)",
     "language": "python",
     "metadata": {},
     "outputs": []
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
