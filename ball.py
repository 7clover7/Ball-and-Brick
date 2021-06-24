# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 20:38:45 2021

@author: 11872
"""

import pygame as p
from pygame.sprite import Sprite as s

class Ball(s):
    """管理弹球的类"""
    
    def __init__(self,ai_game):
        """初始化弹球并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bat_rect = ai_game.bat.rect
        self.screen_rect = ai_game.screen.get_rect()
        
        #加载弹球图像并获取其外界矩形
        self.image = p.image.load('ball.bmp')
        self.rect = self.image.get_rect()
        
        #将弹球放在弹板顶部中央
        self.rect.midbottom = self.bat_rect.midtop
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.moving_left_x = True
        self.moving_right_x = False
        self.moving_up_y = True
        self.moving_down_y = False
        self.flag = 0
        
    def draw(self):
        """绘制弹球的初始位置"""
        
        self.screen.blit(self.image,self.rect)
        
    def run(self):
        if self.moving_left_x and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_up_y:
                self.x -= self.settings.ball_speed
                self.y += self.settings.ball_speed
            elif self.moving_down_y:
                self.x -= self.settings.ball_speed
                self.y -= self.settings.ball_speed
            self.flag == 1
        if self.moving_right_x and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_up_y:
                self.x += self.settings.ball_speed
                self.y += self.settings.ball_speed
            elif self.moving_down_y:
                self.x += self.settings.ball_speed
                self.y -= self.settings.ball_speed
            self.flag == 1
                
        self.rect.x = self.x
        self.rect.y = self.y


