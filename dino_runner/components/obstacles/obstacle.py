import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Obstacle(Sprite):
    def __init__(self, image, type, obstacle_type):
        self.obstacle_type = obstacle_type
        self.type = type
        self.image = image[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.obstacle_type == "bird":
            self.fly_bird()

        if self.step_index >= 10:
            self.step_index = 0

        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def fly_bird(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.dino_rect = self.image.get_rect()
        self.step_index += 1