# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:18:52 2021

@author: 11872
"""

import pygame as p
from pygame.sprite import Sprite as s

class Bat(s):
    """管理弹板的类"""
    
    def __init__(self,ai_game):
        """初始化弹板并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #加载弹板图像并获取其外接矩形
        self.image = p.image.load('bat.bmp')
        self.rect = self.image.get_rect()
        
        #将弹板放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        #在弹板的属性x中存储小数值
        self.x = float(self.rect.x)
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        
    def draw(self):
        """在指定位置绘制弹板"""
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        """根据移动标志调整弹板位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.bat_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.bat_speed
            
        #根据self.x更新rect对象
        self.rect.x = self.x