def tubson(n):
    k=0
    for i in range(1,n+1):
        if n%i==0:
            k=k+1

    if k==2:
        return 'Tub son'
    else:
        return 'Tub emas'


print(tubson(271))
