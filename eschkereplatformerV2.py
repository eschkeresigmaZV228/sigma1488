import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 600
FPS = 60
PLAYER_SPEED = 5
GRAVITY = 0.5
JUMP_HEIGHT = -10

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

bg = pygame.image.load("img_15.png")

BLACK = (0, 0, 0)
WHITE = (165,42,42)
BLUE = (0, 255, 0)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = PLAYER_SPEED
        self.vel_y = 0

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
        if pressed_keys[pygame.K_SPACE] and self.vel_y == 0:
            self.jump()

        self.vel_y += GRAVITY
        self.rect.move_ip(0, self.vel_y)

        if self.rect.left < 0:
            self.rect.right = SCREEN_WIDTH
        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 0

    def jump(self):
        self.vel_y = JUMP_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center=(x, y))

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

platform = Platform(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 20)
all_sprites.add(platform)
platforms.add(platform)

platform1 = Platform(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150, SCREEN_WIDTH //2, 25)
all_sprites.add(platform1)
platforms.add(platform1)

platform2 = Platform(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 450, SCREEN_WIDTH //4, 25)
all_sprites.add(platform2)
platforms.add(platform2)

platform3 = Platform(SCREEN_WIDTH // 100, SCREEN_HEIGHT - 300, SCREEN_WIDTH //2, 25)
all_sprites.add(platform3)
platforms.add(platform3)

platform4 = Platform(SCREEN_WIDTH // 3, SCREEN_HEIGHT - 250, SCREEN_WIDTH //5, 50)
all_sprites.add(platform4)
platforms.add(platform4)

running = True
while running:

    for platform in platforms:
        platform.rect.y += 2
        platform.rect.y = platform.rect.y % SCREEN_HEIGHT


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    collisions = pygame.sprite.spritecollide(player, platforms, False)
    if collisions:
        player.rect.bottom = collisions[0].rect.top
        player.vel_y = 0

    screen.blit(bg, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
