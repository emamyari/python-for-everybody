n=1234572293
i=2
print("start")
while i<n:
    if n%i==0:
        print("not prime")
        break
    else:
        i=i+1
else:
    print("is prime")

#Check that numbers are prime