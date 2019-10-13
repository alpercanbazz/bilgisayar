#ilk iki basamak toplamı>3. basamaktan
sayac = 0
for i in range(100,1000):
    s=str(i)
    if (s[0]+s[1])>s[2]:
        print(s)
        sayac = sayac+1

print(sayac)
