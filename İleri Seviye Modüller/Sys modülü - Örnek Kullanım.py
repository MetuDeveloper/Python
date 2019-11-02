import sys

def kök_bulma(a,b,c):
    delta = b**2 - 4*a*c
    x1 = (-b - delta*0.5)/(2*a)
    x2 = (-b + delta*0.5)/(2*a)
    return (x1,x2)

if len(sys.argv) == 4:
    print("Kök Bulma",kök_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Yanlış sayıda parametre girdiniz....")