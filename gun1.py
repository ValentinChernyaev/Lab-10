from random import randrange as rnd, choice
from tkinter import *
import math

print (dir(math))

import time
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)


class ball():
    """ Класс ball описывает мяч. """

    def __init__(self,x=40,y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue','green','red','brown'])
        self.id = canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
        self.live = 30
        self.nature = 1
        self.balls = balls
        self.bum_time = 100
        self.bum_on = 0
        self.surprize = 0
        self.surprize_time = 0

         # Взято из two-guns
    def fire(self): # Взрыв шара?
        n = 5
        for z in range(1,n+1):
            new_ball = ball(self.balls)
            new_ball.r = 5
            v = 5+rnd(5)
            an = z*2*math.pi/n+rnd(-2,3)/7
            new_ball.vx = v*math.cos(an)
            new_ball.vy = v*math.sin(an)
            new_ball.x = self.x + new_ball.vx*3
            new_ball.y = self.y + new_ball.vy*3
            new_ball.nature = 0
            new_ball.points = 1
            new_ball.live = rnd(10)+30
            new_ball.color = choice(colors)
            self.balls += [new_ball]

    #def set_coords(self):
     #   canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
    def paint(self):
        canv.coords(self.id,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)

    def move(self):
        """ Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """
                #Взято из two-guns
        if self.y <= 500:
            self.vy += 0.07
            self.y += self.vy
            self.x += self.vx
            self.vx *= 0.999
            self.v = (self.vx**2+self.vy**2)**0.5
            self.an = math.atan(self.vy/self.vx)
            self.paint()
        else:
            self.live -= 1
            if self.live < 0:
                self.bum()
                #self.kill()
        if self.x > 780:
            self.vx = - self.vx/2
            self.x = 779
        elif self.x < 20:
            self.vx = - self.vx/2
            self.x = 21
        if self.bum_on and self.nature:
            self.bum_time -= 1
            if self.bum_time <= 0:
                self.bum()

    def bum(self):
            self.fire()
            self.kill()

    def hittest(self,ob):
        """ Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте ob.

        Args:
            ob: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if abs(ob.x - self.x) <= (self.r + ob.r) \
          and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

class gun():
    """ Класс gun описывает пушку. """
    def __init__(self):
       self.f2_power = 10
       self.f2_on = 0
       self.an = 1
       self.x = 400
       self.y = 450
       self.points = 0
    #self.id = canv.create_line(20,450,50,420,width=7)
    # FIXME: don't know how to set it...
       self.id = canv.create_line(self.x,self.y,self.x,
              self.y-20,width=10, smooth = 1)





    def fire2_start(self,event):
        self.f2_on = 1

    def fire2_end(self,event):
        """ Выстрел мячом происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и
        vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y)/(event.x-new_ball.x))
        new_ball.vx = self.f2_power*math.cos(self.an)
        new_ball.vy = -self.f2_power*math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10


    def targetting (self,event=0):
        """ Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan((event.y-450)/(event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an))


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')

class target():
  def __init__(self, targets):
        self.points = 1
        self.targets = targets
        x = self.x = rnd(50,750)
        y  = self.y = rnd(-250,150)
        r= self.r = rnd(10,40)
        self.live = 5 + rnd(5)
        self.change_color = 0
        color = self.color = 'red'
        self.id = canv.create_oval(x-r,y-r,x+r,y+r, fill = self.color)
        self.id_live = canv.create_text(x,y,text=self.live)

  def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600,780)
        y = self.y = rnd(300,550)
        r = self.r = rnd(2,50)
        color = self.color = 'red'
        canv.coords(self.id, x-r,y-r,x+r,y+r)
        canv.itemconfig(self.id, fill = color)

  def hit(self,points = 1):
        """ Попадание шарика в цель. """
        canv.coords(self.id,-10,-10,-10,-10)
        self.points += points
        canv.itemconfig(self.id_points, text = self.points)





def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text = 'Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text = '')
    canv.delete(gun)
    root.after(750,new_game)



t1 = target(1)
screen1 = canv.create_text(400,300, text = '',font = '28')
g1 = gun()
bullet = 0
balls = []
new_game()

mainloop()

