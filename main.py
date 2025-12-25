import pygame
from player import Player
from enemy import Enemy

# ==================== INIT ====================
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Enemy Dungeon Game")
clock = pygame.time.Clock()

# ==================== LOAD ASSETS ====================
# Floor tile
try:
    floor_tile = pygame.image.load("assets/tiles/floor.png")
except FileNotFoundError:
    try:
        floor_tile = pygame.image.load("assets/tiles/floor.png.jpeg")
    except FileNotFoundError:
        floor_tile = pygame.Surface((32, 32))
        floor_tile.fill((80, 80, 80))
floor_tile = pygame.transform.scale(floor_tile, (32, 32))

# Sound
try:
    hit_sound = pygame.mixer.Sound("assets/sounds/hit.wav")
except Exception:
    hit_sound = None

# Fonts
font_big = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 30)

# ==================== GAME STATES ====================
GAME_START = "start"
GAME_PLAY = "play"
GAME_OVER = "over"
game_state = GAME_START

# ==================== GAME OBJECTS ====================
player = Player()
enemies = [Enemy() for _ in range(3)]

player_health = 3
score = 0
level = 1

# ==================== UI FUNCTIONS ====================
def draw_start_screen():
    screen.fill((20, 20, 40))
    title = font_big.render("AI ENEMY DUNGEON", True, (0, 255, 200))
    info = font_small.render("Press ENTER to Start", True, (255, 255, 255))
    screen.blit(title, (180, 220))
    screen.blit(info, (240, 300))

def draw_hud():
    h = font_small.render(f"Health: {player_health}", True, (255, 0, 0))
    s = font_small.render(f"Score: {score}", True, (255, 255, 0))
    l = font_small.render(f"Level: {level}", True, (255, 255, 255))
    a = font_small.render("Enemy Learning...", True, (0, 255, 255))

    screen.blit(h, (10, 10))
    screen.blit(s, (10, 40))
    screen.blit(l, (10, 70))
    screen.blit(a, (10, 100))

def draw_game_over():
    screen.fill((10, 10, 30))
    over = font_big.render("GAME OVER", True, (255, 0, 0))
    retry = font_small.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(over, (230, 220))
    screen.blit(retry, (240, 300))

# ==================== MAIN LOOP ====================
running = True
while running:
    clock.tick(60)

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Start game
            if game_state == GAME_START and event.key == pygame.K_RETURN:
                game_state = GAME_PLAY

            # Restart game
            if game_state == GAME_OVER and event.key == pygame.K_r:
                player_health = 3
                score = 0
                level = 1
                enemies = [Enemy() for _ in range(3)]
                game_state = GAME_PLAY

    # -------- START MENU --------
    if game_state == GAME_START:
        draw_start_screen()

    # -------- GAME PLAY --------
    elif game_state == GAME_PLAY:
        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((30, 30, 40))

        # Draw dungeon floor (below HUD area)
        for x in range(0, 800, 32):
            for y in range(120, 600, 32):
                screen.blit(floor_tile, (x, y))

        # Enemy logic
        for enemy in enemies:
            enemy.update(player)
            enemy.draw(screen)

            # Collision detection
            if pygame.Rect(player.x, player.y, 40, 40).colliderect(
               pygame.Rect(enemy.x, enemy.y, 40, 40)):
                player_health -= 1
                if hit_sound:
                    hit_sound.play()

        player.draw(screen)
        draw_hud()

        # Level progression
        if score >= level * 50:
            level += 1
            enemies.append(Enemy())

        # Game over condition
        if player_health <= 0:
            game_state = GAME_OVER

    # -------- GAME OVER --------
    elif game_state == GAME_OVER:
        draw_game_over()

    pygame.display.update()

pygame.quit()
