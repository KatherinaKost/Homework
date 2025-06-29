"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

from pyowm import OWM
from pprint import pprint

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()
obs = mgr.weather_at_place(input('Введите город'))
w = obs.to_dict()
#pprint(w)
print(f"Температура:   {w['weather']['temperature']['temp']-273.15:.1f} °C")
print(f"Ощущается как: {w['weather']['temperature']['feels_like']-273.15:.1f} °C")
print(f"Макс/мин:      {w['weather']['temperature']['temp_max']-273.15:.1f} / {w['weather']['temperature']['temp_min']-273.15:.1f} °C")
print(f"Скорость ветра: {w['weather']['wind']['speed']} м/с")
print(f"Влажность:     {w['weather']['humidity']}%")
print(f"Давление:      {w['weather']['pressure']['press']} гПа")
     