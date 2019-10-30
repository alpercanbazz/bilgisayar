#ilk iki basamak toplamı>3. basamaktan
sayac = 0
for i in range(100,1000):
    s=str(i)
    if (int(s[0])+int(s[1]))==int(s[2]):
        print(s)
        sayac = sayac+1

print(sayac)
