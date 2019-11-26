import pygame,sys
from paddle import Paddle

class GameDisplay:
    pygame.init()
    

    def __init__(self,width,height):
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.pixle_size = 5
        self.window = pygame.display.set_mode((width*self.pixle_size, height*self.pixle_size))
        self.width = width
        self.height = height
        self.key_presses = {}
        self.key_releases = {}

    def translate_to_pygame(self,disp):
        self.window.fill(self.black)
        for i in range(len(disp)):
            if disp[i]:
                pygame.draw.rect(self.window,self.white,pygame.Rect(
                    self.pixle_size*((i)%self.width),self.pixle_size*int(i/self.width)
                    ,self.pixle_size,self.pixle_size))
        pygame.display.update()

    def add_key(self,key,press_func,rel_func):
        self.key_presses[key] = press_func
        self.key_releases[key] = rel_func

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.key_presses['w']()
                elif event.key == pygame.K_s:
                    self.key_presses['s']()
                elif event.key == pygame.K_UP:
                    self.key_presses['UP']()
                elif event.key == pygame.K_DOWN:
                    self.key_presses['DOWN']()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.key_releases['w']()
                elif event.key == pygame.K_s:
                    self.key_releases['s']()
                elif event.key == pygame.K_UP:
                    self.key_releases['UP']()
                elif event.key == pygame.K_DOWN:
                    self.key_releases['DOWN']()
    