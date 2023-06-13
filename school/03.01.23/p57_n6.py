a=int(input())
n=a//100+a//10%10
m=a%10+a//10%10
print(max(n,m),min(n,m))
