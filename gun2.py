from random import randrange as rnd, choice
from tkinter import *
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600+600+100')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)

colors = ['blue','green','red','brown']

class ball():
    def __init__(self, balls, x=40,y=450):
        self.x = x
        self.y = y
        self.r = 8
        self.color = choice(colors)
        self.points = 3
        self.id = canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
        #self.id_points = canv.create_text(self.x,self.y,text = self.points)
        self.live = 70
        self.nature = 1
        self.balls = balls
        self.bum_time = 100
        self.bum_on = 0
        self.surprize = 0
        self.surprize_time = 0

    def paint(self):
        canv.coords(self.id,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)
        #canv.coords(self.id_points,self.x,self.y)
        #canv.itemconfig(self.id_points,text = self.points)

    def jump(self):
        if self.vx**2+self.vy**2 > 10:
            self.vy = -self.vy*0.7
            self.vx = self.vx*0.7
            self.y = 499

    def move(self):
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
        if not self.nature:
            self.live -= 0.1
            if self.r > 0.1:
                self.r -= 0.1
            else:
                self.kill()
            self.vy += 0.2
            if self.live < 0:
                self.kill()
        if self.surprize:
            self.surprize_time += 1
            if self.surprize_time > 13:
                self.surprize_time  = 0
                self.fire()



    def hittest(self,ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

    def ricochet(self,w):
        self.v = (self.vx**2 + self.vy**2)**0.5
        self.an = math.atan(self.vy/self.vx)

        if self.x == w.x:
            self.x += 1

        if w.x-(self.x+self.vx):
            an_rad = math.atan((w.y-(self.y+self.vy))/(w.x-(self.x+self.vx)))
            an_res = an_rad - (self.an - an_rad )

            vx2 = 0.8*self.v*math.cos(an_res)
            vy2 = 0.8*self.v*math.sin(an_res)
            if self.an > 0 and self.vx < 0 and self.vy < 0 or self.an < 0 and self.vx < 0:
                vx2 = -vx2
                vy2 = -vy2
            self.vx = -vx2
            self.vy = -vy2
            self.move()
            self.points += 1

    def kill(self):
        canv.delete(self.id)
        #canv.delete(self.id_points)
        try:
            self.balls.pop(self.balls.index(self))
        except:
            pass

    def fire(self):
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

    def bum(self):
        if self.nature:
            self.fire()
            self.kill()


class gun():
    def __init__(self):
        self.f2_power = 10
        self.x = 400
        self.y = 450
        self.f2_on = 0
        self.on = 1
        self.an = 1
        self.points = 0
        self.id = canv.create_line(self.x,self.y,self.x,self.y-20,width=7, smooth = 1)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')

        self.bullet = 0

        self.vx = 0

    def fire_start(self,event):
        if self.on:
            self.f2_on = 1

    def stop(self):
        self.f2_on = 0
        self.on = 0

    def fire_end(self,event):
        if self.on:
            self.bullet += 1
            new_ball = ball(self.balls)
            new_ball.r += 5
            new_ball.x = self.x
            new_ball.y = self.y
            new_ball.vx = self.f2_power*math.cos(self.an)/9
            new_ball.vy = self.f2_power*math.sin(self.an)/9
            if not rnd(5):
                new_ball.surprize = 1
            self.balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 35

    def move(self,event=0):
        if event:
            if event.keycode == 39 and self.vx < 4:
                self.vx += 1
            elif event.keycode == 37 and self.vx > -4:
                self.vx -= 1
        else:
            self.x += self.vx
            if self.x < 50:
                self.x = 50
                self.vx = 0
            elif self.x > 750:
                self.x = 750
                self.vx = 0
        self.aiming()

    def aiming (self,event=0):
        if event:
            if abs(event.x - self.x) < 0.0001:
                event.x += 0.1
            self.an = math.atan((event.y-self.y)/(event.x-self.x))
            if event.x < self.x:
                self.an += math.pi


        if self.f2_on:
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        canv.coords(self.id,self.x,self.y,self.x+max(self.f2_power,20)*math.cos(self.an),self.y+max(self.f2_power,20)*math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')

    def bum(self, event = 0):
        for b in self.balls[::-1]:
            if b.nature:
                b.bum()
                break



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

    def paint(self):
        x = self.x
        y = self.y
        r = self.r
        canv.coords(self.id, x-r,y-r,x+r,y+r)
        canv.coords(self.id_live,x,y)

    def hit(self, points = 1):
        self.live -= points
        canv.itemconfig(self.id_live,text=self.live)
        canv.itemconfig(self.id, fill = 'orange')
        self.change_color = 10
        if self.live < 1:
            self.kill()

    def move(self):
        self.y += 0.6
        self.paint()
        if self.y > 450:
            self.kill()

    def kill(self):
        self.targets.pop(self.targets.index(self))
        canv.delete(self.id)
        canv.delete(self.id_live)


class game():
    def __init__(self):
        self.moving = []
        self.gamer1 = gun()
        self.gamer2 = gun()
        self.gamer1.x = 30
        self.gamer2.x = 770
        self.gamer1.balls = self.moving
        self.gamer2.balls = self.moving
        self.active_gamer = self.gamer1

        canv.bind('<Button-1>',self.fire_start)
        canv.bind('<ButtonRelease-1>',self.fire_end)
        canv.bind('<Motion>',self.aiming)
        root.bind('<Key>',self.move)
        self.go = 1

    def fire_start(self,event):
        self.active_gamer.fire_start(event)

    def fire_end(self,event):
        self.active_gamer.fire_end(event)
        self.active_gamer.stop()

    def aiming(self,event):
        self.active_gamer.aiming(event)

    def power_up(self,event):
        self.active_gamer.power_up(event)

    def move(self,event):
        self.active_gamer.move(event)

    def round(self):
        if self.active_gamer == self.gamer1:
            self.active_gamer = self.gamer2
            print ('g1')
        else:
            self.active_gamer = self.gamer1
            print ('g2')

        self.active_gamer.on = 1

        while self.active_gamer.on or self.moving:
            for m in self.moving:
                m.move()
            self.active_gamer.aiming()
            self.active_gamer.power_up()
            canv.update()
            time.sleep(0.007)



game1 = game()
while 1:
    game1.round()





