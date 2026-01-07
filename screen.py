# file: screen.py
# description: functions to draw different game screens
# author: chris frias

import pygame
from constants import *

def draw_center_text(screen, text, font, y_offset, color=(255, 255, 255)):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + y_offset))
    screen.blit(surface, rect)

def draw_start_screen(screen, font, small_font):
    screen.fill("black")
    draw_center_text(screen, "Asteroids", font, -50)
    draw_center_text(screen, "Press 's' to start", small_font, 50)

def draw_dead_screen(screen, font, small_font, final_score, high_scores):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((25, 0, 0))
    screen.blit(overlay, (0, 0))
    
    draw_center_text(screen, "Game Over", font, -150, (255, 0, 0))
    draw_center_text(screen, f"Your Score: {final_score}", small_font, -80)
    draw_center_text(screen, "Leaderboard", small_font, -20, (50, 215, 0))
    
    # print scores
    for i, score in enumerate(high_scores):
        y_pos = 20 + (i * 30) 
        draw_center_text(screen, f"{i+1}. {score}", small_font, y_pos)

    draw_center_text(screen, "press 'r' to restart", small_font, 200)