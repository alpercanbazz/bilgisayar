
# şifrelenecek metni alıyorum
metin1 = input("metini giriniz : ")


def sifreleme(metin1):
    #boşluklar kaldırılsın :))
    metin="".join(metin1.split())
    sifre = ""
    alfabe=['a','b' ,'c' ,'ç', 'd', 'e', 'f', 'g','ğ' ,'h' ,'ı','i' ,'j','k' ,'l' ,'m' ,'n' ,'o','ö' ,'p' ,'r' ,'s','ş' ,'t' ,'u','ü' ,'v', 'y' ,'z',]
    for i in metin: #metnin her harfi bir basamak sağındakiyle değişiyor
        b=alfabe.index(i) #her harfin alfabe listesindeki indisi
        #ya z olursa 
        if b==28:
            b=-1
        sifre+=alfabe[b+1]
    print("sifre :",sifre)
    return metin
sifreleme(metin1)
