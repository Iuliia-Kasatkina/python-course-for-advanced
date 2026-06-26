# 6.2 Основы работы с кортежами. Часть 1
"""

Вам доступен кортеж countries. Напишите программу, которая выводит все элементы кортежа countries, кроме последних трех.

Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.

Тестовые данные 🟢
Номер теста	                                     Входные данные	                                                        Выходные данные
1	           countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')          ('Romania', 'Poland', 'Estonia', 'Bulgaria')


2	           countries = ('Chad', 'Canada', 'USA', 'Germany', 'Netherlands')                                      ('Chad', 'Canada')


3              countries = ('Belarus', 'Estonia', 'Egypt', 'Turkey', 'France', 'Belgium')                           ('Belarus', 'Estonia', 'Egypt')


"""

print(countries[:- 3])