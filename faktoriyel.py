#faktoriyel

carpım=1
toplar=0
for i in range(1,100):
    carpım= carpım*i
    toplar= toplar+(1/carpım)
print(toplar+1)
