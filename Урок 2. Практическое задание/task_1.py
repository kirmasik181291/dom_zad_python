#"""
#Задание 1. Создать список и заполнить его элементами различных типов данных.
#Реализовать проверку типа данных каждого элемента.
#Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя,
#а указать явно, в программе.

#Пример:
#для списка [5, "string", 0.15, True, None]
#результат

#<class 'int'>
#<class 'str'>
#<class 'float'>
#<class 'bool'>
#<class 'NoneType'>
#"""
my_list=[(-1+0j),1,2.2,True,None,'String',[3,4],
         (5,6,6.5),{7:'seven',8: 'eight'},{9,10},
         frozenset(),range(11),b'twelwe',bytearray(b'thirteen'),
         zip(*[(14,15),(16,17),('a','b')]),TypeError]
for i,val in enumerate(my_list,1):
    print(f"{i}) {val} - {type(val)}")
