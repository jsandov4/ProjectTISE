"""This is my Code """

def inputconsole(): # pragma: no cover
    import argparse 
    parse = argparse.ArgumentParser(description='Calculate states')
    parse.add_argument('-ty','--types',type=float,metavar ='',required=True,help='(0) for LegendrePolynomial'+\
                           ' otherwise for Fourier basis')
    parse.add_argument('-nb','--nbas',type=float,metavar ='',required=True,help='Size of basis')
    parse.add_argument('-v','--v0',type=float,metavar ='',required=True,help='Potential constant')
 
        
    return parse