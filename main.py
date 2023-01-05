import openpyxl
import os
import datetime
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
dirs = config.get("settings", "dirs").split('\n')  # Берем данные из conf.ini каждый элемент массива с новой строки
path = config.get("settings", "path")
list = []

#  Запрашиваем нужную дату
print('Введите день:')
day = input()
print('Введите месяц:')
month = input()
date = ('2023' + '-' + month + '-' + day)  # Год поменять тут

for i in range(len(dirs)):
    directory = (path + dirs[i])
    os.chdir(directory)
    counter = 0  # счетчик количества файлов

    names = os.listdir(os.getcwd())  # создаем массив из файлов директории
    cwd = os.getcwd()
    for file in names:
        fullname = os.path.join(cwd,
                                file)  # достаем полный путь к файлу, объединяя текущую папку с именем файла из массива
        if (datetime.datetime.fromtimestamp(os.path.getmtime(fullname)).strftime(
                '%Y-%m-%d')) == date:  # конвертируем дату создания файла в год-месяц-день и сравниваем с требуемой
            counter += 1
    # for i in range(len(dirs)):
    print('Файлы в', dirs[i], 'посчитали')
    list.append({'Место': dirs[i],
                 month + '.' + day: counter})

    df = pd.DataFrame(list)
df.to_excel('D:\\Calls\\calls.xlsx')
input('Press ENTER to exit')