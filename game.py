import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
GROUND_Y = WINDOW_HEIGHT - 100
FPS = 60
GRAVITY = 1
JUMP_SPEED = -20
GAME_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dinosaur Game")
clock = pygame.time.Clock()

class Dinosaur:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 100
        self.y = GROUND_Y - self.height
        self.velocity_y = 0
        self.is_jumping = False
        self.color = RED

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_SPEED
            self.is_jumping = True

    def update(self):
        # Apply gravity
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        # Check ground collision
        if self.y > GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.velocity_y = 0
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Obstacle:
    def __init__(self):
        self.width = 30
        self.height = 50
        self.x = WINDOW_WIDTH
        self.y = GROUND_Y - self.height
        self.color = BLACK

    def update(self):
        self.x -= GAME_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.x < -self.width

class Game:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.obstacle_timer = 0
        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.__init__()  # Reset game
                    else:
                        self.dinosaur.jump()
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self):
        if not self.game_over:
            self.dinosaur.update()

            # Update obstacles
            for obstacle in self.obstacles:
                obstacle.update()

            # Remove off-screen obstacles
            self.obstacles = [obs for obs in self.obstacles if not obs.off_screen()]

            # Spawn new obstacles
            self.obstacle_timer += 1
            if self.obstacle_timer > random.randint(60, 120):
                self.obstacles.append(Obstacle())
                self.obstacle_timer = 0

            # Check collisions
            for obstacle in self.obstacles:
                if self.check_collision(self.dinosaur, obstacle):
                    self.game_over = True

            # Update score
            self.score += 1

    def draw(self):
        screen.fill(WHITE)

        # Draw ground
        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WINDOW_WIDTH, GROUND_Y), 2)

        # Draw game objects
        self.dinosaur.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (20, 20))

        if self.game_over:
            game_over_text = self.font.render("Game Over! Press SPACE to restart", True, BLACK)
            screen.blit(game_over_text, (WINDOW_WIDTH // 2 - 180, WINDOW_HEIGHT // 2))

        pygame.display.flip()

    def check_collision(self, dino, obstacle):
        dino_rect = pygame.Rect(dino.x, dino.y, dino.width, dino.height)
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
        return dino_rect.colliderect(obstacle_rect)

def main():
    game = Game()
    running = True

    while running:
        running = game.handle_events()
        game.update()
        game.draw()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()