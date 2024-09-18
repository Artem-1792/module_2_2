#Задача "Все ли равны?":

first = input('Введите число: ')
second = input('Введите число: ')
third = input('Введите число: ')

if  first == second or first == third or second == third:
    print(2)

elif first == second == third:
    print(3)

else:
    print(0)

