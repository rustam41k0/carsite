# list = [1, 2, 3, 4, 5, 6, 67, 78]
#
#
# def oper(list):
#     for i in range(len(list)):
#         print(list(i))
#         yield list[i]
#
#
# oper(list)

# def get_even(list_of_nums):
#     for i in list_of_nums:
#         if i % 2 == 0:
#             yield i
#
#
# # инициализация списка
# list_of_nums = [1, 2, 3, 8, 15, 42]
#
# # вывод начального списка
# print("До фильтрации в генераторе: " + str(list_of_nums))
#
# # вывод только четных значений из списка
# print("Только четные числа: ", end=" ")
# for i in get_even(list_of_nums):
#     print(i, end=" ")

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.keys()
# print(x)
# a = [[] for i in range(3)]
# print(a)
choosen_cars = ['mers', 'mazda', 'hundai']
cars = ''
for car in choosen_cars:
    cars += car + '\n'

print(cars)