def check(n):
    not_n = ''
    for i in range(len(n)-1,-1,-1):
        not_n+=n[i]
    return n==not_n


print(check(input()))