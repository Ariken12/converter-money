import time
import urllib.request as rq
from xml.etree import ElementTree as ET
time = time.strftime('%d/%m/%Y', time.gmtime(time.time()))
print("Сегодня - " + time)
values = ET.parse(rq.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req={}".format(time)))
coins = float(input("Введите ваше количество рублей: "))
dictionary = []
i = 0
for value in values.findall("Valute"):
    name = value.find("Name").text
    price = value.find("Value").text
    print(str(i+1) + " - " + name)
    dictionary.append((name, float(price.replace(",", "."))))
    i += 1
choice = input()
name = dictionary[int(choice)-1][0]
coins = coins * dictionary[int(choice)-1][1]
print("Выберите валюту")
print("\n" * 35)
print("Ваше количество выбранной валюты({value}): {coin}".format(value=name, coin=coins))