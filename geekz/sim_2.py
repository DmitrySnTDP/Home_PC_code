# №1
# alf = (0,1)
# print('a e f l F')
# for a in alf:
#     for e in alf:
#         for f in alf:
#             for l in alf:
#                 if ((not(f) and e)<=(not(not(l) or a)))==0:
#                     print(a,e,f,l)


# №2
# count = 0
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 for e in 0,1:
#                     if (((not(a))<=e) or ((not(b)) and c and (not(d))))==0:
#                         count+=1
# print(count)


# №3
# for n in range(10000,100000):
#     n = str(n)
#     n1 = int(n[0])+int(n[2])+int(n[4])
#     n2 = int(n[1])+int(n[3])
#     r = str(min(n1,n2))+str(max(n1,n2))
#     if int(r)==922:
#         print(n)
#         break


# №4
# def prav(r):
#     count_0 = 0
#     count_1 = 0
#     for i in r:
#         if i=='0':
#             count_0+=1
#         else:
#             count_1+=1
#     if count_0<count_1:
#         r = r+'0'
#     else:
#         r = '11'+r
#     return r


# for n in range(1,100000):
#     r = bin(n)[2:]
#     r = prav(r)
#     r = prav(r)
#     if int(r,2)>989:
#         print(n)
#         break


# №5
# def dell(n,m):
#     return n%m==0


# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if ((dell(x,a) and not(dell(x,16)))<=(dell(x,23)))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break


# №6
# for g in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if (((x&13!=0) and (x&39!=0))<=((x&g!=0) and (x&13!=0)))==0:
#             check = False
#             break
#     if check:
#         print(g)
#         break


# №7
def F(n):
    if n<=1:
        return 42
    elif n>1 and n%2==0:
        return F(n-2)+F(n-3)+n
    else:
        return F(n-1)+F(n-3)-n

print(F(99))


# №8
# def F(n):
#     if n == 1:
#         return 1
#     elif n>1:
#         return (2*n-1)*F(n-1)

# print(F(15)/F(5))


# №9
# f = open('9.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# max_nums = 0
# count = 0

# for i in range(len(numbers)-2):
#     para = numbers[i:i+3]
#     for n in numbers:
#         if sum(para)//3==n:
#             count+=1
#             max_nums = max(max_nums,(para[0]*para[1]*para[2]))
#             break
# print(count,max_nums)


# №10
# f = open('10.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# count = 0
# max_sr = -100000

# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if sum(para)%2==0 and str(sum(para))[-1]!='6':
#         count+=1
#         max_sr = max(max_sr,(sum(para)/2))
# print(count,max_sr)


# №9 ответ 2386 948255822849597030