from scene import *
from random import random

class MyScene (Scene):
    def setup(self):
        self.x=70
        self.y=224
        self.g = 0.5 #gravity
        self.acel = 0
        self.grav = True
        self.pts = 0
        self.rtimer = 0
        self.dead=False
        self.ms = 6 #max speed

    def draw(self):
        background(0, 0.5, 1.0)
        fill(1, 1, 1)
        self.player=rect(self.x,self.y,32,32)
        fill(0,0,0)
        self.roof=rect(self.x-70,self.y+75,700,32)
        self.floor=rect(self.x-70,self.y-75,700,32)
        if not self.grav:
            self.acel += 1

  #text
        tint(0,0,0,1)
        if self.dead == True:
            text('You are DEAD', 'Arial', 12, 48, self.y+ 16, 5)

        if self.dead == False:
            self.pts += 1

        text('Points: ' + str(self.pts), 'Arial', 12, self.x-48, self.y + 32, 5)

  # Touch input:
        fill(1,0,0)
        if not self.grav:
            self.acel += 1


  # Physics
        if self.dead == False:
            self.y += self.acel

        if self.y < self.floor:
            self.y = self.floor
            self.acel = 0
        else:
            self.acel -= self.g

        if self.acel > self.ms:
            self.acel = self.ms
        if self.acel < -self.ms:
            self.acel = -self.ms

    def touch_began(self, touch):
        self.grav = not self.grav

    def touch_moved(self, touch):
        pass

    def touch_ended(self, touch):
        pass

run(MyScene())
