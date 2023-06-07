# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
import math
from datetime import timedelta

def minsec2time(value : float) :
    '''Переводим значение длительности песни в формате 3.03 что есть 3 минуты 3 секунды в значение timedelta
    Параметры:
        value(float) длительность песни в формате MMMM.SSS Минуты.Секунды
    Возвращаемое значение:
        значение timedelta на основе исходного значения длительности     
    '''
    #разделяем значение на дробную и целую части
    fractional, integer = math.modf(value)
    
    seconds_part = int(round(fractional * 100))
    ret_val = timedelta(hours= 0, minutes=integer, seconds=seconds_part)
    return ret_val

#3.03
#3*60 + 0.03*100
def minsec2sec(value : float) : 
    '''Переводим значение длительности песни в формате 3.03 что есть 3 минуты 3 секунды в значение в секундах что будет равно 183
    Параметры:
        value(float) длительность песни в формате MMMM.SSS Минуты.Секунды
    Возвращаемое значение:
        целочисленное значение в секундах на основе исходного значения длительности
    '''
    #разделяем значение на дробную и целую части
    fractional, integer = math.modf(value)

    seconds_part = int(round(fractional * 100))
    minutes_part = int(integer) * 60
    return minutes_part + seconds_part

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

##############################################
# вариант без использования  модуля datetime

#длина списка
list_size = len(my_favorite_songs)

#три случайно выбранных индекса песен 
index_tuple  = ( random.randint(0, list_size - 1),  random.randint(0, list_size - 1), random.randint(0, list_size - 1) )

#сумма звучания трех песен в секундах
total_time_sec = ( minsec2sec(my_favorite_songs[index_tuple[0]][1])  + 
                   minsec2sec(my_favorite_songs[index_tuple[1]][1]) +  
                   minsec2sec(my_favorite_songs[index_tuple[2]][1])
)

#сумма звучания трех песен в минутах без учета секунд
total_time_min = int( total_time_sec / 60)

# если остаток в секундах больше или равен 30, округляем увеличивая на одну минуту
if  total_time_sec % 60 >= 30:
    total_time_min += 1

print(f'1_2 Пункт А, вариант без использования  модуля datetime: три песни звучат {total_time_min} минут')

##############################################
# вариант C ИСПОЛЬЗОВАНИЕМ  модуля datetime

total_time = (minsec2time(my_favorite_songs[index_tuple[0]][1])  + 
              minsec2time(my_favorite_songs[index_tuple[1]][1]) +  
              minsec2time(my_favorite_songs[index_tuple[2]][1])
)
print(f'1_2 Пункт А, вариант C ИСПОЛЬЗОВАНИЕМ  модуля datetime: три песни звучат {round(total_time.total_seconds()/60)} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

#три случайно выбранных  песни
tuple_dict  = random.sample(list(my_favorite_songs_dict.items()),  3)
                      
total_time_dict = ( minsec2time(tuple_dict[0][1] )  + 
                    minsec2time(tuple_dict[1][1]) +  
                    minsec2time(tuple_dict[2][1])
)

print(f'1_2 Пункт B, три песни звучат {round(total_time_dict.total_seconds()/60)} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
