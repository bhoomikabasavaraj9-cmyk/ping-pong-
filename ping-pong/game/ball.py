# ping-pong/game/ball.py
import pygame
import random

WHITE = (255, 255, 255)

class Ball:
    def __init__(self, x, y, radius, speed_x=7, speed_y=7):
        self.rect = pygame.Rect(x - radius, y - radius, radius*2, radius*2)
        self.radius = radius
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))

    def move(self, player, ai, sounds, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
            if sounds: sounds["wall"].play()

        # Paddle collisions
        if self.rect.colliderect(player.rect) and self.speed_x < 0:
            self.speed_x *= -1
            if sounds: sounds["paddle"].play()
        elif self.rect.colliderect(ai.rect) and self.speed_x > 0:
            self.speed_x *= -1
            if sounds: sounds["paddle"].play()

    def reset(self, width, height):
        self.rect.center = (width//2, height//2)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)
