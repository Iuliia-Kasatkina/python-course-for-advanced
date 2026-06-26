# 6.2 Основы работы с кортежами. Часть 1
"""

Вам доступен кортеж countries. Напишите программу, которая выводит количество вхождений строки 'Spain' в кортеж countries.

Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.

Тестовые данные 🟢
Номер теста	                                   Входные данные	                                                                                     Выходные данные
1	            countries = ('Mexico', 'New Zealand', 'Spain', 'Poland', 'Latvia', 'Spain')                                                                   2



2	           countries = ('China', 'Moldova', 'Cuba', 'Brazil')                                                                                             0


3	           countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')      3

"""

print(countries.count('Spain'))