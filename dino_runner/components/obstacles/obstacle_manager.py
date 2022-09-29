from random import randint
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager(Obstacle):
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            aleatory_obstacles = 0
            if aleatory_obstacles == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS + LARGE_CACTUS))
            #elif aleatory_obstacles == 1:    (ainda não conseguir desbugar o bird)
               # self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []