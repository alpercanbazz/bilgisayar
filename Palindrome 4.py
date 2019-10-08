#4 basamaklı palindromik

for i in range(1000,10000):
    s=str(i)
    t=s[::-1]
    if t==s:
        print(s)
