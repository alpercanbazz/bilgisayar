#palindrome 3 basamaklı

for i in range (100,1000):
    s= str(i)
    t= s[::-1]
    if (t==s):
        print(i)
    
