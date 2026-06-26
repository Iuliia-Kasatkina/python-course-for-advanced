# 6.2 Основы работы с кортежами. Часть 1
"""

Вам доступен кортеж countries. Напишите программу, которая выводит все элементы кортежа countries,
 кроме двух последних и трех первых.

Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.

Тестовые данные 🟢
Номер теста	                                           Входные данные	                                                Выходные данные
1	              countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')           ('Bulgaria', 'Slovakia')


2	              countries = ('Australia', 'Russia', 'Nigeria', 'Chad', 'Canada', 'USA', 'Germany', 'Netherlands')     ('Chad', 'Canada', 'USA')


3	              countries = ('Belarus', 'Estonia', 'Egypt', 'Turkey', 'France', 'Belgium')                            ('Turkey',)


"""

print(countries[3:- 2])