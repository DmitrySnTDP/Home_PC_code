n = int(input())
a = str(n%2)
n //= 2

while n>0:
    a = a+str(n%2)
    n //= 2

s = int(a[-1])
a1 = a[-1]

for i in range(-2, (len(a)+1)*-1,-1):
    s += int(a[i])
    a1 = a1+a[i]

s1 = int(a1[0])
a1 += str(s%2)

for i in range(1,len(a1)):
    s1 += int(a1[i])

a1 += str(s1%2)
c = 0
d = int(a1[-1])*2**c

for i in range(-2,(len(a1)+1)*-1,-1):
    c += 1
    d += int(a1[i])*2**c

print(a1,d)