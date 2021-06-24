# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:43:41 2021

@author: 11872
"""

import sys
import pygame as p

from bat import Bat
from ball import Ball
from brick import Brick

class BallandBrick:
    """管理游戏资源和行为类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        p.init()
        self.settings = Settings()
        
        #设置窗口
        self.screen = p.display.set_mode((self.settings.screen_width,
                                         self.settings.screen_height))
        #设置标题
        p.display.set_caption("Ball and Brick")
        
        #绘制弹板
        self.bat = Bat(self)
        
        #绘制弹球
        self.ball = Ball(self)
        
        #绘制砖块
        self.bricks = p.sprite.Group()
        self._create_more()
        
        self.crash = Crash(self)
        
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.bat.update()
            self.ball.run()
            self._create_more()
            self.crash.crash()
            self._update_screen()
            
    def _check_events(self):
        #监视键盘事件
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == p.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == p.K_RIGHT:
        #向右移动弹板
            self.bat.moving_right = True
        #向左移动弹板
        elif event.key == p.K_LEFT:
            self.bat.moving_left = True
        elif event.key == p.K_q:
            p.quit()
            sys.exit()
            
    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == p.K_RIGHT:
            self.bat.moving_right = False
        elif event.key == p.K_LEFT:
            self.bat.moving_left = False
    
    def _update_screen(self):
        #每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ball.draw()
        self.bat.draw()
        self.bricks.draw(self.screen)
        #让最近绘制的屏幕可见
        p.display.flip()
        
    def _create_more(self):
        """创建更多砖块"""
        #创建一个砖块
        brick = Brick(self)
        brick_width,brick_height = brick.rect.size
        available_space_x = self.settings.screen_width - (2 * brick_width)
        number_brick_x = available_space_x // (2 * brick_width)
        
        #计算屏幕可容纳多少行砖块
        bat_height = self.bat.rect.height
        available_space_y = (self.settings.screen_height - (3 * brick_height)
                              - bat_height)
        number_rows = available_space_y // (2 * brick_height) - 1
        
        #创建砖块群
        for row_number in range(number_rows):
            #创建第一行砖块
            for number in range(number_brick_x):
                self. _create_brick(number,row_number)
            
    def _create_brick(self,number,row_number):
            """创建一个砖块并将其加入当前行"""
            brick = Brick(self)
            brick_width,brick_height = brick.rect.size
            brick.x = brick_width + 2 * brick_width * number
            brick.rect.x = brick.x
            brick.rect.y = brick.rect.height + 2 * brick.rect.height * row_number
            self.bricks.add(brick)
            
class Crash:
    """碰撞检测并删除"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.ball = ai_game.ball
        self.ball_rect = ai_game.ball.rect
        self.settings = ai_game.settings
        self.bat = ai_game.bat
        self.bat_rect = ai_game.bat.rect
        self.bricks = ai_game.bricks
        self.flag = ai_game.ball.flag
        self.balls = p.sprite.Group()
        
    def crash(self):
        #弹球与窗口的碰撞检测
        if self.ball_rect.top >= self.screen_rect.top:#and self.ball.moving_right_x:
            self.ball.moving_up_y = False
            self.ball.moving_down_y = True
            #self.ball.moving_right_x = False
            #self.ball.moving_left_x = True
        """if self.ball_rect.top >= self.screen.top and self.ball.moving_left_x:
            self.ball.moving_up_y = False
            self.ball.moving_down_y = True
            self.ball.moving_left_x = False
            self.ball.moving_right_x = True"""
        if self.ball_rect.left <= 0:
            self.ball.moving_left_x = False
            self.ball.moving_right_x = True
        if self.ball_rect.right >= self.screen_rect.right:
            self.ball.moving_right_x = False
            self.ball.moving_left_x = True
        
        #弹球与砖块的碰撞检测
        
        #消失
        """self.balls = p.sprite.Group()
        ball = self.ball
        self.balls.add(ball)
        self.collisions = p.sprite.groupcollide(self.bricks,self.balls,True,False)"""
        
        for i in self.bricks.sprites():
            #弹球从上方碰撞砖块
            if self.ball_rect.bottom <= i.rect.top:
                self.ball.moving_down_y = False
                self.ball.moving_up_y = True
                self.delete()
            #弹球从下方碰撞砖块
            if self.ball_rect.top >= i.rect.bottom:
                self.ball.moving_up_y = False
                self.ball.moving_down_y = True
                self.delete()
            #弹球从左面碰撞砖块
            if self.ball_rect.right >= i.rect.left:
                self.ball.moving_right_x = False
                self.ball.moving_left_x = True
                self.delete()
            #弹球从右面碰撞砖块
            if self.ball_rect.left >= i.rect.right:
                self.ball.moving_left_x = False
                self.ball.moving_right_x = True
                self.delete()
                
        #弹球与弹板的碰撞检测
        #从上方
        if self.ball_rect.bottom >= self.bat_rect.top and self.flag != 0:
            self.ball.moving_down_y = False
            self.ball.moving_up_y = True
        #从左方
        if self.ball_rect.right >= self.bat_rect.left:
            self.ball.moving_right_x = False
            self.ball.moving_left_x = True
        #从右方
        if self.ball_rect.left <= self.bat_rect.right:
            self.ball.moving_left_x = False
            self.ball.moving_right_x = True
            
    def delete(self):
        self.balls.add(self.ball)
        p.sprite.groupcollide(self.balls,self.bricks,False,True)

class Settings:
    """存储游戏中所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (255,255,255)
        
        #弹板设置
        self.bat_speed = 3
        
        #弹球设置
        self.ball_speed = 5

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = BallandBrick()
    ai.run_game()