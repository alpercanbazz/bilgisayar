#2005 yılındaki yaşı doğduğu yılın rakamları toplamı

for i in range(1000,2005):
    a=2005-i
    s=str(i)
    b=int(s[0])+int(s[1])+int(s[2])+int(s[3])
    if a==b:
        print(i)
