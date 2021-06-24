# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:32:54 2021

@author: 11872
"""

import pygame as p
from pygame.sprite import Sprite as s

class Brick(s):
    """表示单个砖块的类"""
    
    def __init__(self,ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        
        #加载外星人图像并设置rect属性
        self.image = p.image.load('brick.bmp')
        self.rect = self.image.get_rect()
        
        #每个砖块最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #存储砖块的精确水平位置
        self.x = float(self.rect.x)