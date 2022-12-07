import pygame

from dino_runner.utils.constants import (FONT_STYLE, BLACK_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH)




def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE)

    text = font.render('Points: ' + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center - (1000, 50)
    return (text, text_rect)

def get_centered_message(message, width-SCREEN_HEIGHT // 2 height // 2):
    
