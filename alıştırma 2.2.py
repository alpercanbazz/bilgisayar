#rekürsif olarak 1'den n'e sayıların toplamı


def toplam(n):
    if(n==1):
        return 1
    return toplam(n-1)+n
