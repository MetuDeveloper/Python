def asal_mi(x):
    i = 2
    if x ==1:
        return False
    elif x==2:
        return True
    else:
        while i<x:
            if x%i==0:
                return False
            i += 1
        return True

print(list(filter(asal_mi,range(1,100))))