#-------------------------------------------------------------------------------
# Описание класса Vector
# Теория:
# https://www.math10.com/ru/geometria/
# operatsii-s-vektorami/operatsii-s-vektorami.html
#-------------------------------------------------------------------------------
class Vector:
# Конструктор с учётом возможности передачи строковых данных
    def __init__(self, x=0, y=0 ):

      if  type(x) == int:  self.x = x
      if  type(x) == str:  self.x =int(x)
      if  type(y) == int:  self.y = y
      if  type(y) == str:  self.y =int(y)

# Переопределение операции сложения
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
# Переопределение операции вычитания
    def ___sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
# Переопределение операции сравнения <
    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y
# Переопределение операции сравнения < СТОИТ ПОДУМАТЬ ПРО МОДУЛЬ
    def __gt__(self, other):
        return self.x > other.x or self.x == other.x and self.y > other.y

# Переопределение операции умножения
# Для векторов это скалярное произведение
    def __mul__(self, other):
        return Vector(self.x *other.y, self.y*other.x)

Vectors=[]

i=0
N=int(input("Введите количество векторов"))
for i in range(N):

  x, y=input("Координаты радиус-вектора: x,y").split(',')
  Vectors.append(Vector(x,y))

sum_vector=Vector(0,0) # определение структуры вектора суммы
i=0
for next_vector in Vectors:
    sum_vector=sum_vector+next_vector

print("Координаты центра масс точек :", sum_vector.x/N, sum_vector.y/N)

