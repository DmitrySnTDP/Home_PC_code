a=input('Введите пароль:')
if len(a)<6:
    print('Слишком короткий пароль!')
elif a[:6]=='qwerty':
    print('Ненадёжный пароль!')
else:
    print('OK')
