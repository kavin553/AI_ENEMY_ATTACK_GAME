import pygame

class Player:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed = 4
        try:
            self.image = pygame.image.load("assets/player/player.png")
        except FileNotFoundError:
            try:
                self.image = pygame.image.load("assets/player/player.png.jpeg")
            except FileNotFoundError:
                self.image = pygame.Surface((40, 40))
                self.image.fill((200, 200, 50))
        self.image = pygame.transform.scale(self.image, (40, 40))

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        # keep player inside map
        self.x = max(0, min(self.x, 760))
        self.y = max(100, min(self.y, 560))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
