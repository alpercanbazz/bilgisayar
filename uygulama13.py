#iki sayı yanyana yazınca toplamlarının 11 katı

for i in range(10,100):
    s=str(i)
    for j in range(10,100):
        a=str(j)
        b=a+s
        c=int(s)+int(a)
        if int(b)==11*c:
            print(a)
            print(s)
