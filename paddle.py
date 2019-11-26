class Paddle:
    def __init__(self,width,height,is_left=False):
        self.width = int(width/64)
        self.height = int(height/4)
        self.screen_hieght = height
        self.screen_width = width
        self.ypos = int(height/2)
        self.move_func = None
        if is_left:
            self.xpos = 0
        else:
            self.xpos = int(width-self.width)
        self.vol = 5

    def display(self,disp):
        for h in range(self.ypos,self.ypos+self.height):
            for w in range(self.xpos,self.xpos+self.width):
                disp[(h*self.screen_width)+w] = True
        return disp

    def abs_height(self,h):
        if h<0:
            return self.screen_hieght + h
        elif h>=self.screen_hieght-1:
            return (h % (self.abs_height-1))
        return h

    def top(self):
        return self.ypos

    def bottom(self):
        return self.ypos + self.height
    
    def left(self):
        return self.xpos
    
    def right(self):
        return self.xpos+self.width
    
    def move_up(self):
        if self.top() > self.vol:
            self.ypos -= self.vol

    def move_down(self):
        if self.bottom() < self.screen_hieght - self.vol:
            self.ypos += self.vol
    
    def move(self):
        if self.move_func != None:
            self.move_func()

    def move_set_up(self):
        self.move_func = self.move_up
    
    def move_set_down(self):
        self.move_func = self.move_down

    def move_set_still(self):
        self.move_func = None
