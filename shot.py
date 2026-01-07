# file: shot.py
# description: shot/bullet class fired by the player
# author: chris frias 


from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        self.angle = angle
        self.speed = PLAYER_SHOOT_SPEED
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.angle) * self.speed * dt