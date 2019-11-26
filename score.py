class Score:
    def __init__(self,width,height):
        self.width = int(width/128)
        self.height = int(height/8)
        self.xpos = int(width/4)
        self.ypos = int(height/8)
        self.score = [0,0]
        self.screen_width = width

    def display(self,disp):
        return self.display_left(self.display_right(disp,self.score[1]),self.score[0])

    def display_left(self,disp,score):
        if score == 0:
            return disp
        return self.display_left(self.display_tally(disp,self.xpos+(score*self.width*2)),score-1)
    
    def display_right(self,disp,score):
        if score == 0:
            return disp
        return self.display_right(self.display_tally(disp,(self.xpos*3)+(score*self.width*2)),score-1)
        
    def display_tally(self,disp,xpos):
        for h in range(self.ypos,self.ypos+self.height):
            for w in range(xpos,xpos+self.width):
                disp[(h*self.screen_width)+w] = True
        return disp

    def incease_score(self,left):
        if left:
            self.score[0]+=1
        else:
            self.score[1]+=1