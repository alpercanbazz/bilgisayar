#4 basamaklı sayılar ilk son rakam büyüklük
sayac= 0
for i in range(1000,10000):
    s=str(i)
    if s[0]>s[3]:
      sayac=sayac+1
print(sayac)
