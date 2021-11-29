import random
import pygame as pg
class Food:
    def __init__(self,x,y,re_weight,re_hight):
        self.x_max=x-1        #29
        self.y_max=y-1        #19
        self.re_weight=re_weight         #食物的宽度
        self.re_hight=re_hight
    def create(self,screen,body): #随机生成食物
        x=random.randint(0,self.x_max)
        y=random.randint(0,self.y_max)
        food = pg.Rect(x * self.re_weight, y * self.re_hight, self.re_weight, self.re_hight)#随机数生成食物
        while food in body:#如果食物在蛇身中再次随机生成，直到不在蛇的身体中
            x = random.randint(0, self.x_max)
            y = random.randint(0, self.y_max)
            food = pg.Rect(x * self.re_weight, y * self.re_hight, self.re_weight, self.re_hight)
        return food #返回食物Rect
