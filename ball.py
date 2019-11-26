from score import Score
import random
class Ball:
    def __init__(self,width,height,score):
        self.width = int((width*height)/2048)
        self.height = self.width
        self.screen_width = width
        self.screen_height = height
        self.xpos = int(width/2)
        self.ypos = int(height/2)
        self.xvol = random.randint(1,2)
        self.yvol = 1
        self.score = score

    def reset(self):
        self.xpos = int(self.screen_width/2)
        self.ypos = int(self.screen_height/2)
        self.xvol = random.randint(1,2)
        self.yvol = 1

    def display(self,disp):
        for h in range(self.ypos,self.ypos+self.height):
            for w in range(self.xpos,self.xpos+self.width):
                disp[(h*self.screen_width)+w] = True
        return disp

    def move_xaxis(self):
        self.xpos += self.xvol
    
    def move_yaxis(self):
        self.ypos += self.yvol

    def move(self):
        if self.is_at_ylimit():
            self.y_bounce()
        if self.is_at_xlimit():
            if self.xpos < self.screen_width/2:
                self.score.incease_score(False)
            else:
                self.score.incease_score(True)
            self.reset()
        self.move_xaxis()
        self.move_yaxis()

    def top(self):
        return self.ypos

    def bottom(self):
        return self.ypos + self.height
    
    def left(self):
        return self.xpos
    
    def right(self):
        return self.xpos+self.width
    
    def y_bounce(self):
        self.yvol *= -1
        self.move_yaxis()
        self.move_yaxis()   
    
    def x_bounce(self):
        self.xvol *= -1
        self.move_xaxis()
        self.move_xaxis()
    
    def is_at_ylimit(self):
        return not (self.bottom() < self.screen_height-self.yvol and self.top() > self.yvol)
    
    def is_at_xlimit(self):
        return not (self.right() < self.screen_width-self.xvol and self.left() > self.xvol)