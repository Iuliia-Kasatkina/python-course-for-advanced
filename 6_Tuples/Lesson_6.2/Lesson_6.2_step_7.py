# 6.2 Основы работы с кортежами. Часть 1
"""
Вам доступен кортеж countries. Напишите программу, которая выводит элементы кортежа countries, кроме первых двух.

Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.

Тестовые данные 🟢
Номер теста	                                     Входные данные	                                                      Выходные данные
1              countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')  ('Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')


2	           countries = ('Chad', 'Canada', 'USA', 'Germany', 'Netherlands')                              ('USA', 'Germany', 'Netherlands')


3	          countries = ('Belarus', 'Estonia', 'Egypt', 'Turkey', 'France', 'Belgium')                    ('Egypt', 'Turkey', 'France', 'Belgium')

"""

print(countries[2:])

