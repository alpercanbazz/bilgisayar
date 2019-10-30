#rakamları toplamı 9dan küçük olan

for i in range(100,999):
    s=str(i)
    a=int(s[0])+int(s[1])+int(s[2])
    if a<9:
        print(s, end=" ")
 
