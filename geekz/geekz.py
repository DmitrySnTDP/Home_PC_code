# следствие
# a = 0
# b = 1
# print(a <= b)

# print('a', 'b', 'c', 'd', 'e', 'F')
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 for e in 0,1:
#                     F = (b==e) or (not a <= e) or (not c and d)
#                     print(a, b, c, d, e, F)

# print('X Y W Z F')
# for x in (0,1):
#     for y in (0,1):
#         for w in (0,1):
#             for z in (0,1):
#                 f = (not (y <= x)) or (z <= w) or (not z)
#                 if f==0:
#                     print(x,y,w,z,int(f))

# import itertools


# alf= (0,1)
# combs = itertools.product(alf,repeat = 4)
# # print(list(combs))
# print('x y z w f')
# for x,y,z,w in combs:
    
#     f = (not (y <= x)) or (z <= w) or (not z)
#     if f==0:
#         print(x,y,z,w,int(f))

# alf = (0,1)
# combs = itertools.product(alf,repeat = 4)
# print('x y z w f')
# for x,y,z,w in combs:
#     f = (((not x) and y) == z) and w
#     if f ==1:
#         print(x,y,z,w,int(f))


#                       дз занятие 1 теоритическое

# import itertools


# alf = (0,1)
# combs = itertools.product(alf,repeat=3)
# print('X Y Z F')
# for x,y,z in combs:
#     f = (x and (not z)) or ((not y) and (not z))
#     print(x,y,z,int(f))


# alf = (0,1)
# combs = itertools.product(alf,repeat=3)
# print('X Y Z F')
# for x,y,z in combs:
#     f = x and ((not y) or z)
#     if f == 1:
#         print(x,y,z,int(f))


# alf = (0,1)
# combs = itertools.product(alf,repeat=3)
# print('X Y W F')
# for x,y,w in combs:
#     f = (x or (not y)) and w
#     if f ==1:
#         print(x,y,w,int(f))


# alf = (0,1)
# combs = itertools.product(alf,repeat=4)
# print('W X Y Z F')
# for w,x,y,z in combs:
#     f = ((x or (not y)) and (not(w==z)) and w)
#     if f==1:
#         print(w,x,y,z,int(f))


# alf = (0,1)
# combs = itertools.product(alf,repeat=4)
# print('W X Y Z F')
# for w,x,y,z in combs:
#     f = ((x==(not y))<=(z==(y or w)))
#     if f==0:
#         print(w,x,y,z,int(f))


# alf = (0,1)
# combs = itertools.product(alf,repeat=4)
# print('W X Y Z F')
# for w,x,y,z in combs:
#     f = (x<=y)and(y<=z)and(z<=w)
#     if f==1:
#         print(w,x,y,z,int(f))

#                                                  практика 1

# import itertools


# k = 0
# alf = (0,1)
# combs = itertools.product(alf,repeat=5)

# for a,b,c,d,e in combs:
#     f = ((not a)<=e) or ((not b) and c and (not d))
#     if f==0:
#         k+=1
# print(k)

#                                                практика 1 Дз

# import itertools

# k = 0
# alf = (0,1)
# combs = itertools.product(alf,repeat=4)
# print('X Y Z W F')
# for x,y,z,w in combs:
#     f = (x<=y) and (y<=z) and (z<=w)
#     if f==1:
#         # k+=1
#         print(x,y,z,w,int(f))
# print(k)

#                                              теория 2
# n = int(input())
# b = bin(n) # двоичная запись числа
# print(b[2:])


# №3
# for n in range(1000,10000):
#     a = (n//1000)+(n%10)
#     b = (n//100%10)+(n//10%10)

#     if b>a:
#         ab=str(a)+str(b)
#         if int(ab)==1016:
#             print(n)
#             break
#     else:
#         ba=str(b)+str(a)
#         if int(ba)==1016:
#             print(n)
#             break



# summ = 0
# for k in range(1000):
#     a = str(bin(k)[2:])
#     for i in a:
#         summ +=int(i)
#     a ='10'+a[2:]+'0' if summ%2==0 else '11'+a[2:]+'1'  
#     s = 0
#     n = 0
#     for i in range(len(a)-1,-1,-1):
#         s+=int(a[i])*2**n
#         n+=1
#     if s>16:
#         print(k)
#         break


# №1
# def Suma(n):
#     summ = 0
#     for i in range(len(n)):
#         summ+=int(n[i])
#     return summ
# A = []
# for k in range(1,1000):
#     n = str(bin(k)[2:])
#     suma = Suma(n)
#     n+=str(suma%2)
#     summa = Suma(n)       
#     n+=str(summa%2)
#     N = 0
#     ch = 2**(len(n)-1)
#     for i in range(len(n)):
#         N+=ch*int(n[i])
#         ch//=2
#     if N<=67:
#         A.append(N)
# print(A)
# print(bin(78)[2:])


# №4
# summ = 0
# for k in range(1000,1,-1):
#     a = str(bin(k)[2:])
#     a=a+'10' if k%2==0 else a+'01'  
#     s = 0
#     n = 0
#     for i in range(len(a)-1,-1,-1):
#         s+=int(a[i])*2**n
#         n+=1
#     if s<=111:
#         print(s)
#         break

# №6
# summ = 0
# for k in range(1000):
#     a = str(bin(k)[2:])
#     a=a+'00' if k%2==0 else a+'11'  
#     s = 0
#     n = 0
#     for i in range(len(a)-1,-1,-1):
#         s+=int(a[i])*2**n
#         n+=1
#     if s>122:
#         print(s)
#         break


# №7
# count = 0
# for n in range(10000):
# # n = int(input())
#     k = n
#     n = n//4 if n%4==0 else n-1
#     n = n//5 if n%5==0 else n-2
#     n = n//17 if n%17==0 else n-1
#     if n==3:
#         count+=1
#         print(k)
# print(count)


# №8
# for n in range(10000):
#     k = bin(n)[2:]
#     k1 ='10'+str(k)[2:]+'11' if k.count('1')%2==0 else '11'+str(k)[2:]+'00'
#     r= int(k1,2)
#     if r>39:
#         print(n)
#         break


#                                                практика 02

# for n in range(10000):
#     b = bin(n)[2:]
#     b = '10'+b[2:]+'0' if b.count('1')%2==0 else '11'+b[2:]+'1'
#     if int(b,2)>40:
#         print(n)
#         break



# for n in range(10000,0,-1):
#     b = bin(n)[2:]
#     b = '10'+b[2:]+'0' if b.count('1')%2==0 else '11'+b[2:]+'1'
#     if int(b,2)<=160:
#         print(n)
#         break



# for n in range(10000):
#     b = bin(n)[2:]
#     b = b+'00' if b[-1]=='0' else b+'10'
#     b = b+'0' if b.count('1')%2==0 else b+'1'
#     count = 0
#     if int(b,2)>=130 and int(b,2)<=350:
#         count+=1
# print(count)



# A = []
# for n in range(100,1000):
#     n = str(n)
#     a = int(n[0])*int(n[1])
#     b = int(n[1])*int(n[2])
#     ab = str(b)+str(a) if a>=b else str(a)+str(b)
#     if ab=='832':
#         A.append(n)
# print(max(A))



#                                                Дз к практике 2

# №1
# for i in range(10000):
#     n = str(bin(i)[2:])
#     n = n+str(n.count('1')%2)
#     n = n+str(n.count('1')%2)
#     if int(n,2)>77:
#         print(i)
#         break



# №2
# for i in range(10000):
#     n = str(bin(i)[2:])
#     n = n+'01' if n[-1]=='0' else n+'10'
#     if int(n,2)>62:
#         print(int(n,2))
#         break



# №3
# for i in range(10000):
#     n = str(bin(i)[2:])
#     n+='00' if n[-1]=='0' else '11'
#     if int(n,2)>545:
#         print(i)
#         break



# №4
# A = []
# for n in range(1000,10000):
#     n = str(n)
#     a = int(n[0])+int(n[1])
#     b = int(n[2])+int(n[3])
#     ab = str(b)+str(a) if a>=b else str(a)+str(b)
#     if ab=='114':
#         A.append(int(n))
# print(max(A))



# №5
# A = []
# for i in range(1,25):
#     n = str(bin(i)[2:])
#     n='10'+n[2:]+'1' if n.count('1')%2==0 else '11'+n[2:]+'0'
#     A.append(int(n,2))
# print(max(A))


#                                 теория 3
# Задание 15

# for a in range(1,10000):
#     check = True
#     for x in range(1,10000):
#         if ((x&95!=0)<=((x&21==0)<=(x&a!=0)))==0:
#             check = False
#             break
    
#     if check:
#         print(a)
#         break



# for a in range(1,10000):
#     check = True
#     for x in range(1,10000):
#         if ((x&83==0)<=((x&31!=0)<=(x&a!=0)))==0:
#             check = False
#             break
    
#     if check:
#         print(a)
#         break



# for a in range(10000,1,-1):
#     check = True
#     for x in range(1,10000):
#         if ((x&a!=0)<=((x&42==0)<=(x&15!=0)))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# for a  in range(10000,-10000,-1):
#     check = True
#     for x in range(10000):
#         for y in range(10000):
#             if ((y+4*x!=60)or(x>a)or(y>a))==0:
#                 check = False
#                 break
#         if not check:
#             break
#     if check:
#         print(a)
#         break




# for a in range(1000):
#     check = True
#     for x in range(1000):
#         for y in range(1000):
#             if ((2*x+3*y!=90)or(a>=x)or(a>=y))==0:
#                 check = False
#         if not check:
#             break
#     if check:
#         print(a)
#         break



# for a in range(-1000,1000):
#     Check = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if ((5*y+4*x<a)or(x+y>100))==0:
#                 Check = False
#         if not Check:
#             break
#     if Check:
#         print(a)
#         break



# дз



# №1
# for a in range(10000):
#     check = True
#     for x in range(10000):
#         for y in range(10000):
#             if ((2*x+3*y>90)or (x+y<=a))==0:
#                 check = False
#                 break
#         if not check:
#             break
#     if check:
#         print(a)
#         break



# №2
# for a in range(1,1000):
#     check = True
#     for x  in range(1,1000):
#         if (((x&26!=0)<=(x&a!=0))or ((x&42!=0)and(x&38!=0)))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# №3
# for a in range(1000,-1,-1):
#     check = True
#     for x in range(1000):
#         for y in range(1000):
#             if ((2*y+x!=18) or (a<=x)or (a<=y))==0:
#                 check = False
#                 break
#         if not check:
#             break
#     if check:
#         print(a)
#         break



# №4
# for a in range(1000,-1000,-1):
#     check = True
#     for x in range(-1000,1000):
#         if ((x&a!=0)<=((x&21==0)<=(x&7!=0)))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# №5
# for a in range(-1000,1000):
#     check = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if ((12*y+x<a)or(2*x+3*y>170))==0:
#                 check = False
#                 break
#         if not check:
#             break
#     if check:
#         print(a)
#         break



# №6
# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if (((x&15!=0)or (x&32!=0))<=(x&a!=0))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# №7
# for a in range(1000,-1000,-1):
#     check = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if ((y-x>a)or(12*x+13*y>350)or(3*y-2*x<=45))==0:
#                 check = False
#                 break
#         if not check:
#             break
#     if check:
#         print(a)
#         break



# №8
# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if ((x&41!=0)<=(x&a!=0)or(not((x&21!=0)or (x&a!=0))))==0:
#                 check = False
#                 break
#         if not check:
#             break
#     if check:
#         print(a)
#         break


#                                            практика 3



# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#             if (not(a<(180-x)) or (x%5==0)<=(not(x%23==0)))==0:
#                 check = False
#                 break
#     if check:
#         print(a)
#         break



# def dell(n,m):
#     return (n%m==0)

# def sumbol(s,d):
#     return (s+d>0)

# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if (dell(x,11)<=(not(sumbol(x,-30))) or ((x+a)>=120))==0:
#             check = False
#             break

#     if check:
#         print(a)
#         break



# def treg(n,m,k):
#     return (n+m>k and n+k>m and m+k>n)

# for a in range(1000,0,-1):
#     check = True
#     for x in range(1,1000):
#         if (treg(a,8,x)<=((max(x,15)<=21)==(not(treg(30,x,16)))))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# def od(n,m):
#     for i in range(2,min(n,m)+1):
#         if n%i==0 and m%i==0:
#             return True
#     return False


# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if ((od(x,44)<=(not(od(x,11)))) or (x+a>=30))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# def dell(n,m):
#     return (n%m==0)

# def f(x,a1,a2):
#     return(a1<=x<=a2) or ((47<=x<=73)<=(not(dell(x,5))))

# s = 9999

# for a1 in range(1,1000):
#     for a2 in range(a1+1,1000):
#         check = True
#         for x in range(1,1000):
#             if f(x,a1,a2)==0:
#                 check = False
#                 break
#         if check:
#             s = min(s,a2-a1)
# print(s)



#                                               дз к практике 3



# №1
# def dell(n,m):
#     return(n%m==0)

# def sym(s,d):
#     return(s+d>0)

# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if (not(dell(x,17) and sym(x,-45)) or (x+a>=130))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# №2
# def treg(n,m,k):
#     return(n+m>k and n+k>m and m+k>n)

# for a in range(1000,0,-1):
#     check = True
#     for x in range(1,1000):
#         if (treg(a,12,x)<=((max(x,11)<=30) and (not(treg(46,x,21)))))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# №3
# def od(n,m):
#     for i in range(2,min(n,m)+1):
#         if n%i==0 and m%i==0:
#             return True
#     return False

# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         if ((x+a>=52) or (od(x,49)<=(not(od(x,42)))))==0:
#             check = False
#             break
#     if check:
#         print(a)
#         break



# №4
# def f(x,a1,a2):
#     return (((x>=78 and x<=102) and (x<50 or x>90))<=(x>=a1 and x<=a2)) and ((x<a1 or x>a2)<=((x<61 or x>130) or (x<50 or x>90)))

# s = 9999

# for a1 in range(1,1000):
#     for a2 in range(a1+1,1000):
#         check = True
#         for x in range(-1000,1000):
#             if f(x,a1,a2)== 0:
#                 check = False
#                 break
#         if check:
#             s = min(s,a2-a1)
# print(s)


#        теор 4
# file = open("geekz/xxx.txt")
# numbers = file.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_sum = -200000
# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if (abs((para[0])%4==0  or abs(para[1])%4 ==0) and abs(para[0])%21!=0):
#         count+=1
#         sum_para = sum(para)
#         max_sum = max(max_sum, sum_para)
# print(count,max_sum)



# f = open('geekz/xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_num = -200000
# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if ((para[0]%6==0 or para[1]%6==0) and para[0]%41!=0 and para[1]%41!=0):
#         count+=1
#         max_par = max(para)
#         max_num = max(max_num,max_par)
# print(count,max_num)



# f = open('geekz/xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_sred = -20000000
# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if (para[0]*para[1])%10==7 and (para[0]*para[1]>0):
#         count+=1
#         sred_para = (para[0]+para[1])//2
#         max_sred = max(max_sred,sred_para)
# print(count,max_sred)

# 

# f = open('geekz/xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# max_abs = 0
# count = 0
# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if (str(para[0])[-1]=='6' and str(para[1])[-1]!='6') or (str(para[1])[-1]=='6' and str(para[0])[-1]!='6') and  abs(para[0]-para[1])<=5*max(numbers):
#         count+=1
#         abs_par = abs(para[1]-para[0])
#         max_abs = max(abs_par, max_abs)
# print(count,max_abs)



# дз


# №1
# f = open('xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_num = -20000
# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if ((para[0]%14==0 or para[1]%14==0)and para[0]%22!=0 and para[1]%22!=0):
#         count+=1
#         max_num = max(max_num,para[0],para[1])
# print(count,max_num)

# №2
# f = open('xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_proizv = -200000000
# for i in range(len(numbers)-1):
#     para = numbers[i:i+2]
#     if (((para[0]%10==0 and para[1]%10!=0) or (para[0]%10!=0 and para[1]%10==0)) and para[0] < para[1]):
#         count+=1
#         proizv = para[0]*para[1]
#         max_proizv = max(max_proizv,proizv)
# print(count,max_proizv)

# №3
# f = open('xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_sr= -20000
# for i in range(len(numbers)-2):
#     para = numbers[i:i+3]
#     if ((para[0]%21==0 and para[1]%21!=0 and para[2]%21!=0) or (para[0]%21!=0 and para[1]%21==0 and para[2]%21!=0) or (para[0]%21!=0 and para[1]%21!=0 and para[2]%21==0)):
#         count+=1
#         sr = (para[0]+para[1]+para[2])//3
#         max_sr = max(sr, max_sr)
# print(count,max_sr)

# №4
# f = open('xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# min_num = 2000000
# for i in range(len(numbers)-2):
#     para = numbers[i:i+3]
#     if ((para[0]%11==0 and ((para[1]+para[2])%10)%2==0 and (para[1]+para[2])%10!=0) or (para[1]%11==0 and ((para[0]+para[2])%10)%2==0 and (para[0]+para[2])%10!=0) or (para[2]%11==0 and ((para[1]+para[0])%10)%2==0 and (para[1]+para[0])%10!=0)):
#         count+=1
#         min_num = min(min_num,para[0],para[1],para[2])
# print(count,min_num)



# Практика 4


# f = open('xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# max_num = -9999999
# for i in range(len(numbers)-2):
#     para = numbers[i:i+3]
#     if ((para[0]%35==0 or para[1]%35==0 or para[2]%35==0)):
#         count+=1
#         max_num = max(max_num, max(para))
# print(count,max_num)



# f = open('xxx.txt')
# numbers = f.readlines()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# count = 0
# min_sum = 9999999
# for i in range(len(numbers)-2):
#     para = numbers[i:i+3]
#     if ((str(para[0])[-1]=='3' or str(para[1])[-1]=='3' or str(para[2])[-1]=='3') and ((sum(para))%3==0)):
#         count+=1
#         min_sum = min(min_sum, sum(para))

# print(count,min_sum)



# f = open('xxx.txt')
# numbers = f.readlines()
# num = -999999999
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     if (int(str(numbers[i])[-1])%2==0 and int(str(numbers[i])[-1])!=0):
#         num = max (numbers[i],num) 
# print(num)
# num = num**2
# count = 0
# max_sum = -9999999
# for i in range(len(numbers)-2):
#     para = numbers[i:i+3]
#     if ((para[0]==para[1] or para[1]==para[2] or para[0]==para[2]) and sum(para)<num):
#         count+=1
#         max_sum = max(max_sum, sum(para))

# print(count,max_sum)



#                                                  занятие 5
# def print_hello():
#     print('Hello!')

# print_hello()



# def factorial(n):
#     a = 1
#     for i in range(1,n+1):
#         a*=i
#     return a

# print(factorial(5))



# def strok(surname,name,age):
#     return f'{name} {surname}, возраст {age}'
# print(strok('Иванов','Коля',16))



# def F(n):
#     if n<=10:
#         return n*n+11
#     elif n>10:
#         return F(n-3)+n*n-5

# print(F(40))



# def F(n):
#     if n<3:
#         return 1
#     elif n>=3:
#         return F(n-1)+F(n-2)

# print(F(100))



# def func(n):
#     if n<=1:
#         return 1
#     else:
#         return func(n-1)*n

# print(func(5))



# def F(n):
#     if n<=4:
#         return 2*n-1
#     elif n>4:
#         return F(n-2)+F(n//2)+n
    
# print(F(60))



# def f(n):
#     if n<=3:
#         return 3
#     elif n>3 and n%2==0:
#         return f(n//2)+5
#     elif n>3 and n%2!=0:
#         return f(n-1)-f(n-2)
    
# print(f(20))



# import sys
# sys.setrecursionlimit(5000)

# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)

# print(f(2023)//f(2020))



#                                           дз


# №1
# def F(n):
#     if n>210:
#         return n//2
#     else:
#         return F(n+4)+F(n*2)
# print(F(52))



# №2
# def f(n):
#     if n==1:
#         return 1
#     elif n%2==0:
#         return n+2+f(n-1)
#     else:
#         return 2*f(n-2)
# print(f(24))



# №3
# def f(n):
#     if n<=5:
#         return 1+n
#     elif n>5 and n%5==0:
#         return f(n//2)+(n*2)+1
#     elif n>5 and n%5!=0:
#         return f(n-1)+f(n-4)
# print(f(300))



# №4
# count = 0
# def F(n):
#     global count
#     count+=1
#     if n >= 1:
#         count+=1
#         F(n - 1)
#         F(n - 2)
#         F(n - 3)
# F(22)
# print(count)



# №5
# def f(n):
#     if n==1:
#         return 1
#     elif n>=2:
#         return f(n-1)+2*g(n-1)


# def g(n):
#     if n==1:
#         return 1
#     elif n>=2:
#         return f(n-1)+2*g(n-1)

# print(f(13)+g(10))



# №6
# import sys
# sys.setrecursionlimit(2000)
# def f(n):
#     if n==1:
#         return 1
#     elif n>1:
#         return (n+n%1000)*f(n-1)
    
# print(f(1663)//f(1659))



#                                           практика 5
# from functools import lru_cache


# №1
# def f(n):
#     if n<4:
#         return n-1
#     elif n>=4 and n%5==0:
#         return f(n-3)
#     elif n>=4 and n%5!=0:
#         return f(n-1)+f(n-3)
# print(f(65))



# №2
# def f(n):
#     if n==1:
#         return 3
#     elif n>1:
#         return f(n-1)*(2*n-5)
# print(f(678)/f(675))



# №3
# def f(n):
#     if n<7:
#         return 1
#     elif n>=7 and n%3==0:
#         return f(n-5)
#     elif n>=7 and n%3!=0:
#         return f(n-1)+f(n-2)
# print(f(91))



# №4
# count = 0
# def f(n):
#     global count
#     count+=1
#     if n>=10:
#         f(n-3)
#         count+=1
#         f(n-5)
#         count+=1
#         f(n-8)
# f(70)
# print(count)



# №5
# def f(n):
#     if n<=1:
#         return n
#     elif n>1 and n%11==0:
#         return f(n//2-(n%2))+n*n
#     elif n>1 and n%11!=0:
#         return f(n-2)+2
# for n in range(1000,0,-1):
#     if f(n)<=100000:
#         print(n)
#         break



# №6
# def f(n):
#     if n<3:
#         return n
#     elif n>=3:
#         return f(n//6)
# def g(n):
#     if n<2:
#         return n+1
#     elif n>=2:
#         return g(f(n))
# summ = 0
# for n in range (50,71):
#     summ+=g(n)
# print(summ)



# №7
# def f(n):
#     global count
#     count+=n*n
#     if n>2:
#         count+=n-3
#         f(n-2)
#         f(n-3)
# for n in range (1,100000):
#     count = 0
#     f(n)
#     if count>1000000:
#         print(n,count)
#         break



# №8
# def f(n):
#     if n>38:
#         return 2*n+1
#     elif n<=38 and n%2==0:
#         return 2*f(n+1)+f(n+3)
#     elif n<=38 and n%2!=0:
#         return f(n+2)+2*f(n+4)
    
# count = 0 
# for n in range(1,1001):
#     check = True
#     for i in str(f(n)):
#         if i=='0':
#             check = False
#             break
#     if check:
#             count+=1
# print(count)



# №9
# def f(n):
#     if n<=5:
#         return n-1
#     elif n>5 and n%3==0:
#         return f(n-1)+f(n//2-n)
#     elif n>1 and n%3!=0:
#         return 2*f(n-2)+n*n
# count = 0
# for n in range(1,1001):
#     summ = 0
#     for i in str(f(n)):
#         summ+=int(i)
#     if summ==24:
#         count+=1
# print(count)



# №10
# def f(n):
#     if n>=60:
#         fuc = 1
#         for i in range(1,n+1):
#            fuc*=i
#         return fuc
#     elif n<60:
#         return f(n+4)+2*f(n+2)
# print(f(4)//f(14))



#                                       дз

# №1
# def f(n):
#     if n<5:
#         return n+1
#     elif n>=5:
#         return f(n-4)*f(n//7)+3
# print(1000*f(345)/f(338))


# №2
# def f(n):
#     if n<10:
#         return n
#     elif n>=10 and n%4==0:
#         return f(n-3)+1
#     elif n>=10 and n%4!=0:
#         return f(n-2)+2*f(n-3)

# print(f(91))



# №3
# import sys
# sys.setrecursionlimit(5000)
# @lru_cache
# def f(n):
#     if n<=2:
#         return 1+n
#     elif n>2 and n%8==0:
#         return f(n-5)+3
#     elif n>2 and n%8!=0:
#         return f(n-1)+f(n//2)
    

# for n in range(1000,0,-1):
#     if f(n)<=100000:
#         print(n)
#         break



# №4
# def f(n):
#     if n<5:
#         return 3
#     elif n>=5:
#         return f(n-3)+3
    
# def g(n):
#     if n<4:
#         return n+1
#     elif n>=4:
#         return g(f(n-6))+1

# count = 0
# for n in range(67,83):
#     count+=g(n)
# print(count)



# №5
# def f(n):
#     if n>51:
#         return n+n%10
#     elif n<=51 and n%3==0:
#         return f(n+2)+3*f(n+4)
#     elif n<=51 and n%3!=0:
#         return 3*f(n+1)+f(n+7)

# count = 0
# for n in range(1,1001):
#     check = True
#     check_2 = False
#     for i in str(f(n)):
#         if i=='3':
#             check = False
#             break
#         if i=='5':
#             check_2 = True
#     if check and check_2:
#         count+=1
# print(count)