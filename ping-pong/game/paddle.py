# ping-pong/game/paddle.py
import pygame

WHITE = (255, 255, 255)

class Paddle:
    def __init__(self, x, y, width, height, speed=7):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, up=True, down=True, screen_height=600):
        keys = pygame.key.get_pressed()
        if up and (keys[pygame.K_w] or keys[pygame.K_UP]):
            if self.rect.top > 0:
                self.rect.y -= self.speed
        if down and (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            if self.rect.bottom < screen_height:
                self.rect.y += self.speed

    def ai_move(self, ball, screen_height):
        if ball.rect.centery < self.rect.centery and self.rect.top > 0:
            self.rect.y -= self.speed
        elif ball.rect.centery > self.rect.centery and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
