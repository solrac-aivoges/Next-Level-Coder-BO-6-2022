import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
