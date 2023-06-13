# elements = ["Первый элемент", "Второй элемент", "Третий элемент"]
# print(list(reversed(elements)))


# num = [1,2,3,4,5]

# print(sum(num))


# num = [1,2,3,4,5]

# a=(num[0]+num[1]+num[2]+num[3]+num[4])

# print(a)


eat = ["Молоко", "Хлеб","Сыр","Помидоры","Колбаса"]
print(eat)
eat.append("Масло")
eat[0] = ('Шоколад')
print("Длина списка: ", len(eat))
eat.sort()
del eat[-1]
print(eat)