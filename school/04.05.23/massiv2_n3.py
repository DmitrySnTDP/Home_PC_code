n = 5
mass = input('Массив:\n')
A = mass.split()
B = [int(i) for i in A]
print(f'Среднее арифметическое {sum(B)/len(B)}')
