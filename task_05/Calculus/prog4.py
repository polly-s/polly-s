@test
def int_table(exprs, x):
    """
    Produces a nice integral table of the integrals of exprs

    (note, we have to use pprint(use_unicode=False) because unicode is not supported
    by the IPython doctester)

    >>> int_table([sin(x), cos(x), exp(x), log(x)], x)
      /                      
     |                       
     | sin(x) dx = C - cos(x)
     |                       
    /                        
      /                      
     |                       
     | cos(x) dx = C + sin(x)
     |                       
    /                        
      /              
     |               
     |  x           x
     | e  dx = C + e 
     |               
    /                
      /                            
     |                             
     | log(x) dx = C + x*log(x) - x
     |                             
    /                              
    """
    C = symbols('C')
    
    for expr in exprs:
        pprint(Eq(Integral(expr, x), integrate(expr, x) + C), use_unicode=False)
