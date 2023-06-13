a=input('Введите строку:')
for i in range(len(a)):
    if a[i] in [' ']:
        a=a[:i]+a[i+1:]
    if len(a)==i+1:
        break
print(a)