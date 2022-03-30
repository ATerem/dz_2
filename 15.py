n=int(input("enter digit:"))

res = 0

while n:
  res += n % 10
  n //= 10

print(res)