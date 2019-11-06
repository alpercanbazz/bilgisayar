
#rekürsif olarak 1'den n'e sayıların çarpımı


def çarpım(n):
    if(n==1):
        return 1
    return n*çarpım(n-1)
