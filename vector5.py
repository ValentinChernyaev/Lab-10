#-------------------------------------------------------------------------------
# Используются классы ТОЧКА (аналог VECTOR),  ОТРЕЗОК и ТРЕУГОЛЬНИК
# Теория:
# https://www.math10.com/ru/geometria/
# operatsii-s-vektorami/operatsii-s-vektorami.html
# Идея http://www.programmersforum.ru/showthread.php?t=171474
#-------------------------------------------------------------------------------

# Класс ТОЧКА
class Point:
# Конструктор с учётом возможности передачи строковых данных
    def __init__(self, x=0, y=0 ):

      if  type(x) == int:  self.x = x
      if  type(x) == str:  self.x =int(x)
      if  type(y) == int:  self.y = y
      if  type(y) == str:  self.y =int(y)
# Переопределение отображения строки
# Полезно для печати в print()
    def __str__(self):
        return '{0:3.2f},{1:3.2f}'. \
            format(self.x, self.y)


# # Используем крутое форматирование через метод format()
# блоее прогрессивное чет дурацкие %
# {0:3.3f} {0:}-вставка значения параметра 0 (первого в функции format()
# 3.2f - три на целую часть, два на дробную
# f-число с пл.точкой

class Cut (Point): # Класс ОТРЕЗОК на основе двух экземпляров класса ТОЧКА
   def __init__(self, Point1,Point2):

   # Метод dist вычисляет длинну отрезка
      self.dist=((Point1.x-Point2.x)**2+(Point1.y-Point2.y)**2)**0.5

class Triangle(Point):
    def __init__(self, Point1,Point2,Point3):

    # Для красоты выведены наружу из класса ссылки на длины отрезков
     self.ab=Cut(Point1,Point2).dist
     self.bc=Cut(Point2,Point3).dist
     self.ac=Cut(Point1,Point3).dist
# Метод perimetr вычисляет периметр пользуясь классом ОТРЕЗОК
     self.perimeter=self.ab+self.bc+self.ac
    # Метод area вычисляет площадь используя формулу Герона
     half_per=self.perimeter/2 # полупериметр
     self.area=(half_per*(half_per-self.ab)*(half_per-self.bc)\
     *(half_per-self.ac))**0.5
Points=[]
maxS=0

N=int(input("Введите количество точек"))

for i in range(N): # Заполняем список экземплярами объекта ТОЧКА

  x, y=input("Введите координаты точек: x,y").split(' ')
  Points.append(Point(x,y))
print('Версия для площади на основе объектов ТОЧКА, ОТРЕЗОК, ТРЕУГОЛЬНИК')

for i1 in range(0,N,1):
    for i2 in range (i1,N,1):
      for i3 in range (i2,N,1):
          if (i1!=i2) and (i2!=i3) and (i1!=i3):
                 sq = Triangle(Points[i1],Points[i2],Points[i3]).area

                 print(' ab={0:3.2f} bc={1:3.2f} ac={2:3.2f} per={3:3.2f} area={4:3.2f}'\
                 .format(Triangle(Points[i1],Points[i2],Points[i3]).ab,
                         Triangle(Points[i1],Points[i2],Points[i3]).bc,
                         Triangle(Points[i1],Points[i2],Points[i3]).ac,
                         Triangle(Points[i1],Points[i2],Points[i3]).perimeter,
                         sq))

                 if sq>maxS:
                     maxS= sq
                     i1m = i1
                     i2m = i2
                     i3m = i3


print ('Максимальная площадь:{0:3.2f}'.format(maxS))
print ("Точки треугольника:", Points[i1m], Points[i2m], Points[i3m] )

