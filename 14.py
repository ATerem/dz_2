

n=int(input("enter digit:"))
sum=0
while n!=0 :

    m=n%10
    n=n/10
    sum=int(sum+m)

print(sum)

