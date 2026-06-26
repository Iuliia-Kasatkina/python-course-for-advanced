# 6.2 Основы работы с кортежами. Часть 1
"""
Вам доступен кортеж countries. Напишите программу, которая выводит последний элемент кортежа countries.

Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.

Тестовые данные 🟢
Номер теста	                             Входные данные	                                                                       Выходные данные
1               countries = ('Chad', 'Canada', 'USA', 'Germany', 'Netherlands')                          Netherlands


2	            countries = ('Belarus', 'Estonia', 'Egypt', 'Turkey', 'France', 'Belgium')               Belgium


3	            countries = ('Australia', 'Canada', 'USA')                                               USA


"""

print(countries[len(countries) - 1])