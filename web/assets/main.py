import pygame
import asyncio
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
try:
    floor_tile = pygame.image.load("assets/tiles/floor.png")
except:
    try:
        floor_tile = pygame.image.load("assets/tiles/floor.png.jpeg")
    except:
        floor_tile = pygame.Surface((32, 32))
        floor_tile.fill((80, 80, 80))
floor_tile = pygame.transform.scale(floor_tile, (32, 32))

try:
    hit_sound = pygame.mixer.Sound("assets/sounds/hit.ogg")
except:
    hit_sound = None

font_big = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 30)

# ==================== GAME STATES ====================
GAME_START = "start"
GAME_PLAY = "play"
GAME_OVER = "over"
game_state = GAME_START

# ==================== OBJECTS ====================
player = Player()
enemies = [Enemy() for _ in range(3)]

player_health = 3
score = 0
level = 1

# ==================== TOUCH CONTROL ====================
touch_dx, touch_dy = 0, 0

# ==================== UI ====================
def draw_start_screen():
    screen.fill((20, 20, 40))
    title = font_big.render("AI ENEMY DUNGEON", True, (0, 255, 200))
    info = font_small.render("Tap or Press ENTER to Start", True, (255, 255, 255))
    screen.blit(title, (180, 220))
    screen.blit(info, (200, 300))

def draw_hud():
    screen.blit(font_small.render(f"Health: {player_health}", True, (255, 0, 0)), (10, 10))
    screen.blit(font_small.render(f"Score: {score}", True, (255, 255, 0)), (10, 40))
    screen.blit(font_small.render(f"Level: {level}", True, (255, 255, 255)), (10, 70))

def draw_game_over():
    screen.fill((10, 10, 30))
    screen.blit(font_big.render("GAME OVER", True, (255, 0, 0)), (230, 220))
    screen.blit(font_small.render("Tap or Press R to Restart", True, (255, 255, 255)), (200, 300))

# ==================== MAIN LOOP ====================
async def main():
    global game_state, player_health, score, level, enemies
    global touch_dx, touch_dy

    running = True

    while running:
        clock.tick(60)

        touch_dx, touch_dy = 0, 0  # reset every frame

        # -------- EVENTS --------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # KEYBOARD
            if event.type == pygame.KEYDOWN:
                if game_state == GAME_START and event.key == pygame.K_RETURN:
                    game_state = GAME_PLAY

                if game_state == GAME_OVER and event.key == pygame.K_r:
                    player_health = 3
                    score = 0
                    level = 1
                    enemies = [Enemy() for _ in range(3)]
                    game_state = GAME_PLAY

            # TOUCH (MOBILE)
            if event.type == pygame.FINGERDOWN:
                x = event.x * WIDTH
                y = event.y * HEIGHT

                # LEFT / RIGHT
                if x < WIDTH * 0.4:
                    touch_dx = -1
                elif x > WIDTH * 0.6:
                    touch_dx = 1

                # UP / DOWN
                if y < HEIGHT * 0.4:
                    touch_dy = -1
                elif y > HEIGHT * 0.6:
                    touch_dy = 1

                # Start / Restart with tap
                if game_state == GAME_START:
                    game_state = GAME_PLAY
                elif game_state == GAME_OVER:
                    player_health = 3
                    score = 0
                    level = 1
                    enemies = [Enemy() for _ in range(3)]
                    game_state = GAME_PLAY

        # -------- START --------
        if game_state == GAME_START:
            draw_start_screen()

        # -------- PLAY --------
        elif game_state == GAME_PLAY:
            keys = pygame.key.get_pressed()

            # Combine keyboard + touch
            move_x = 0
            move_y = 0

            if keys[pygame.K_LEFT]: move_x = -1
            if keys[pygame.K_RIGHT]: move_x = 1
            if keys[pygame.K_UP]: move_y = -1
            if keys[pygame.K_DOWN]: move_y = 1

            move_x += touch_dx
            move_y += touch_dy

            player.move_custom(move_x, move_y)  # you must support this

            screen.fill((30, 30, 40))

            for x in range(0, 800, 32):
                for y in range(120, 600, 32):
                    screen.blit(floor_tile, (x, y))

            for enemy in enemies:
                enemy.update(player)
                enemy.draw(screen)

                if pygame.Rect(player.x, player.y, 40, 40).colliderect(
                   pygame.Rect(enemy.x, enemy.y, 40, 40)):
                    player_health -= 1
                    if hit_sound:
                        hit_sound.play()

            player.draw(screen)
            draw_hud()

            if score >= level * 50:
                level += 1
                enemies.append(Enemy())

            if player_health <= 0:
                game_state = GAME_OVER

        # -------- GAME OVER --------
        elif game_state == GAME_OVER:
            draw_game_over()

        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())