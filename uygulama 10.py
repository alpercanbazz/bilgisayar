#ilk iki rakam son iki rakam eşitmi

sayac=0
for i in range(10000,100000):
     s=str(i)
     if int(s[0]+s[1])==int(s[3]+s[4]):
         print(s) #sayıları gosterir
         sayac=sayac+1

print(sayac)
