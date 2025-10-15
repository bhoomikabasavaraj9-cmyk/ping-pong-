# ping-pong/game/game_engine.py
import pygame
import os
from game.paddle import Paddle
from game.ball import Ball

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height//2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height//2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width//2, height//2, 10)

        self.player_score = 0
        self.ai_score = 0
        self.winning_score = 3  # default Best of 3
        self.game_over = False

        # Initialize mixer & load sounds
        pygame.mixer.init()
        self.sounds = self.load_sounds()

        # Fonts
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 74)
        self.small_font = pygame.font.SysFont(None, 36)

    def load_sounds(self):
        """Load MP3 sound files safely from the 'sound' folder."""
        sounds = {}
        try:
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sound_path = os.path.join(base_path, "sound")

            sounds["paddle"] = pygame.mixer.Sound(os.path.join(sound_path, "paddle_hit.mp3"))
            sounds["wall"] = pygame.mixer.Sound(os.path.join(sound_path, "wall_bounce.mp3"))
            sounds["score"] = pygame.mixer.Sound(os.path.join(sound_path, "score.mp3"))

        except Exception as e:
            print(f"⚠ Sounds not loaded: {e}")
            sounds = None
        return sounds

    def handle_input(self):
        self.player.move(screen_height=self.height)
        keys = pygame.key.get_pressed()
        if self.game_over:
            if keys[pygame.K_3]:
                self.set_best_of(3)
            elif keys[pygame.K_5]:
                self.set_best_of(5)
            elif keys[pygame.K_7]:
                self.set_best_of(7)
            elif keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

    def update(self):
        if self.game_over:
            return

        self.ball.move(self.player, self.ai, self.sounds, self.height)
        self.ai.ai_move(self.ball, self.height)

        # Scoring
        if self.ball.rect.left <= 0:
            self.ai_score += 1
            if self.sounds: self.sounds["score"].play()
            self.ball.reset(self.width, self.height)
        elif self.ball.rect.right >= self.width:
            self.player_score += 1
            if self.sounds: self.sounds["score"].play()
            self.ball.reset(self.width, self.height)

        # Game over check
        if self.player_score >= self.winning_score or self.ai_score >= self.winning_score:
            self.game_over = True

    def render(self, screen):
        screen.fill((0,0,0))
        pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

        self.player.draw(screen)
        self.ai.draw(screen)
        self.ball.draw(screen)

        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width//4, 20))
        screen.blit(ai_text, (self.width*3//4, 20))

        if self.game_over:
            winner = "Player" if self.player_score > self.ai_score else "AI"
            text = self.font.render(f"{winner} Wins!", True, WHITE)
            screen.blit(text, (self.width//2 - 150, self.height//2 - 30))
            sub_text = self.small_font.render("Press 3/5/7 for Best Of | ESC to Exit", True, WHITE)
            screen.blit(sub_text, (self.width//2 - 220, self.height//2 + 40))

    def reset_game(self):
    # Stop all sounds
        if self.sounds:
            for sound in self.sounds.values():
                sound.stop()
            
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset(self.width, self.height)
        self.game_over = False


    def set_best_of(self, n):
        self.winning_score = (n // 2) + 1
        self.reset_game()
