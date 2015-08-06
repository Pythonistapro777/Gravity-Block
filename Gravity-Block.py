'''
    The problem is that self.floor is None and in Python ALL numbers
    (even negative numbers!) are greater than None.

    >>> -200 > None
    True
    >>> 200 > None
    True
    
    Also you should use scene.Scene.bounds to know the screen size
    of the devices so that your games look great on all devices.
'''

import scene

class MyScene(scene.Scene):
    def __init__(self):
        scene.run(self)

    def setup(self):
        print('scene.Scene.bounds gives you the screen size:', self.bounds)
        self.x = 70
        self.y = 224
        self.g = 0.5  # gravity
        self.grav = True
        self.acel = 0
        self.pts = 0
        self.rtimer = 0
        self.dead = False
        self.ms = 6  # max speed

    def draw(self):
        scene.background(0, 0.5, 1.0)
        scene.fill(1, 1, 1)
        scene.rect(self.x,self.y,32,32)  # player
        scene.fill(0,0,0)
        scene.rect(self.x-70,self.y+75,700,32)  # roof
        self.floor = scene.rect(self.x-70,self.y-75,700,32)  # floor
        print('self.floor is always None:', self.floor)
        if not self.grav:
            self.acel += 1

  #text
        scene.tint(0,0,0,1)
        if self.dead:
            scene.text('You are DEAD', 'Arial', 12, 48, self.y+ 16)
        else:
            self.pts += 1
        scene.text('Points: %i' % self.pts, 'Arial', 12, self.x-48, self.y + 32)

  # Touch input:
        scene.fill(1,0,0)
        if not self.grav:
            self.acel += 1

  # Physics
        if not self.dead:
            self.y += self.acel
        if self.y < self.floor:
            self.y = self.floor
            self.acel = 0
        else:
            print('problem: {} > {}'.format(self.y, self.floor))
            self.acel -= self.g
        self.acel = max(min(self.acel, self.ms), -self.ms)

    def touch_began(self, touch):
        self.grav = not self.grav

    def touch_moved(self, touch):
        pass

    def touch_ended(self, touch):
        pass

print('=' * 36)
MyScene()
