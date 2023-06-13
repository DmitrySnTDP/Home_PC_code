# №1
# n = int(input())
# m = 60*int(input())
# s = int(input())
# p = int(input())
# time = n*(m+s+p)-p
# print(time//60)
# print(time%60)


# №2
# n = int(input())
# k = int(input())
# p = int(input())
# u = int(input())
# count = 0
# while p!=u:
#     a = u-p
#     if a>0:
#         if p-1<k and 1+k*(a//k+1)-u<u-(p+k*(a//k)) and u-(p+k*(a//k))<3 and 1+k*(a//k+1)-u>0:
#             p=1
#         elif (a%k==0 or a>k or (a<k and abs(u-(p+k))<u-p) and n-k>=p):
#             p+=k
#         else:
#             p+=1

#     else:
#         if n-p<k and n-u<abs(a):
#             p=n
#         elif (abs(a)%k==0 or abs(a)>k or (abs(a)<k and abs(u-(p-k))<p-u)) and n>p:
#             p-=k
        
#         else:
#             p-=1
#     count+=1
# print(count)


# №3
# import math
# a = int(input())
# r1 = int(input())
# r2 = int(input())
# x = 1
# y = math.sqrt(r2**2-(a-x)**2)
# while r1**2!=y**2+x**2:
#     x+=1
#     y = math.sqrt(r2**2-(a-x)**2)
# print(x)
# print(y*(-1))


# №4

n = int(input())
k = int(input())
stopk = [i for i in range(1,n+1)]
count = 1
while len(stopk)>0:
    if stopk[0]==k:
        print('Yes')
        print(count)
        break
    stopk.pop(0)
    count+=1
    if len(stopk)>0:
        if stopk[0]==k:
            print('No')
            print(count)
            break
        stopk.pop(0)
        count+=1
    else:
        break
    if len(stopk)>0:
        stopk.append(stopk[0])
        stopk.pop(0)
        count+=1
    else:
        break

# №5
