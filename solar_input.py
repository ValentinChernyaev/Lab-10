﻿# coding: utf-8
# license: GPLv3

from solar_objects import *


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """
    global title_header
    # Заголовок по умолчанию
    title_header.title="Небесная механика 1.0"
    objects = []
    with open(input_filename,encoding='utf-8') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_star_parameters(line, planet)
                objects.append(planet)
            else: # это заголовок из файла строка без коментария
               title_header.title=line
               print(title_header.title)

    input_file.close
    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    lines = line.split()
    star.R = float(lines[1])
    star.color = lines[2]
    star.m = float(lines[3])
    star.x = float(lines[4])
    star.y = float(lines[5])
    star.Vx = float(lines[6])
    star.Vy = float(lines[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    lines = line.split()
    planet.R = float(lines[1])
    planet.color = lines[2]
    planet.m = float(lines[3])
    planet.x = float(lines[4])
    planet.y = float(lines[5])
    planet.Vx = float(lines[6])
    planet.Vy = float(lines[7])

def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """

    with open(output_filename, 'w', encoding='utf-8' ) as out_file:
        for obj in space_objects:
         line='{0:6s} | {1:3.0f} | {2:6s} | {3:6.3e} | {4:6.3e} | {5:6.3e} | {6:6.3e} | {7:6.3e} '.\
         format(obj.type, obj.R,
         obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy)
         print (line, file=out_file)
    out_file.close


if __name__ == "__main__":
      print("Это вспомогательный модуль. Запуск программы через solar_main.py")