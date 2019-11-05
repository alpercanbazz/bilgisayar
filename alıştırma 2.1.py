

import random
import math
j= 0
l= 0
print("doğru yer sayacı = j",j)
print("yanlış yer sayacı= l",l)



x=int(input("bir sayı giriniz= "))
def mastermind(x):
    a=random.randint(10,98)
    x=str(x)
    a=str(a)
    if (len(x)==2):
        if (a[0]==x[0]):
            j=j+1
            print(j)
        elif (a[1]==x[1]):
            j=j+1
            print(j)
        elif (a[0]==x[1]):
            l=l-1
            print(l)

        elif (a[1]==x[0]):
            l=l-1
            print(l)
            
        
#çalışmıyor :((
