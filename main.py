import sys
import pygame as pg
import pygame.time
from snack import Snack
from food import Food
import pygame.font
from screen import Screen
pg.init()#检查
if __name__=='__main__':
    x=45  #宽度占多少个格子
    y=22  #高度占多少个格子
    re_width =35 #每个格子的宽度
    re_high = 40#每个格子的高度
    width = x*re_width#总宽度
    high = y*re_high#总高度
    screen_color=(255,255,255)
    screen_object=Screen(x,y, re_width, re_high) #创建一个屏幕对象
    screen=screen_object.create_screen(screen_color)
    head_color = (140, 150, 130)
    body_color = (0, 0, 0)
    food_color = (20, 56, 255)
    body = screen_object.create_snack(screen, head_color, body_color)#创建蛇身
    snack=Snack(width,high-2*re_high,re_width,re_high,body)#创建一个蛇对象
    food=Food(x,y-2,re_width,re_high)#创建一个食物对象
    direction = "right"#控制蛇的移动方向
    switch=[False,True]#第一个是游戏的开始和结束开关active，第二个是食物的生成开关switch
    clock=pygame.time.Clock()
    food_sum=[-1,0]
    text="Play"
    try:
        with open("max.txt", mode="r") as f: #读取历史最高分
            food_sum[1] = int(f.read())
    except Exception:
        with open("max.txt", mode='w') as f:
            f.write(str(food_sum[1]))
    while True:
       clock.tick(10)#调节游戏速度
       if switch[1] : #生成食物，当食物被吃后再重新产生
           re_food = food.create(screen, body)
           food_sum[0] += 1
           food_sum[1]=max(food_sum[0],food_sum[1])
           switch[1] = False
       for event in pg.event.get():  # 监听键盘和鼠标事件
           if event.type==pg.MOUSEBUTTONDOWN and switch[0]==False:
               n=pg.mouse.get_pos()
               switch[0]=play_button.collidepoint(n)
               food_sum[0] =0 #重置得分
               body = screen_object.create_snack(screen, head_color, body_color)
               snack = Snack(width, high-2*re_high, re_width, re_high, body)
               text="Try Again" #点击一次开始后，后面的按钮文本都变成这个
           if event.type == pg.KEYDOWN and switch[0]==True:#通过按键改变蛇的移动方向
               if (event.key == pg.K_UP or event.key == pg.K_w) and direction != "down" and direction !="up":
                   direction = "up"
               elif (event.key == pg.K_DOWN or event.key == pg.K_s) and direction != "up" and direction != "down":
                   direction = "down"
               elif (event.key == pg.K_LEFT or event.key == pg.K_a) and direction != "right" and direction != "left":
                   direction = "left"
               elif (event.key == pg.K_RIGHT or event.key == pg.K_d) and direction != "left" and direction != "right":
                   direction = "right"
           if event.type == pg.QUIT :  # 检查用户是否点击了关闭窗口按钮
               with open("max.txt",mode='w') as f:
                   f.write(str(food_sum[1]))#将历史最高分写入一个txt文件中保存下来
               pg.quit()  # 停止pygame库
               sys.exit()  # 退出程序
       if switch[0]:
           pg.mouse.set_visible(False)#隐藏鼠标
           wall =snack.move(direction, re_food,switch)  # 返回一个布尔值判断是否撞墙
           screen=snack.drow(screen_object,screen_color, head_color,food_color, body_color, wall, body,switch,re_food)
           screen_object.goal(screen,"goal :",food_sum[0],width/2,2*re_high,0,(y-2)*re_high)#显示得分
           screen_object.goal(screen,"Max :",food_sum[1],width/2,2*re_high,width/2,(y-2)*re_high)#显示最高得分
       else:
           play_button = screen_object.goal(screen,text,food_sum[0],6*re_width,1.5*re_high,width/2-3*re_width,(high-re_high)/2)
           pg.mouse.set_visible(True)#显示鼠标
       pg.display.flip()  # 更新画面
