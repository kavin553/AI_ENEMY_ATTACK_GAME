import pygame
from qlearning import get_state, choose_action, update_q

class Enemy:
    def __init__(self):
        self.x = 100
        self.y = 150
        self.speed = 2
        try:
            self.image = pygame.image.load("assets/enemy/enemy.png")
        except FileNotFoundError:
            try:
                self.image = pygame.image.load("assets/enemy/enemy.png.jpeg")
            except FileNotFoundError:
                self.image = pygame.Surface((40, 40))
                self.image.fill((200, 50, 50))
        self.image = pygame.transform.scale(self.image, (40, 40))

    def update(self, player):
        state = get_state(self, player)
        action = choose_action(state)

        reward = 0

        if action == "CHASE":
            if self.x < player.x: self.x += self.speed
            if self.x > player.x: self.x -= self.speed
            if self.y < player.y: self.y += self.speed
            if self.y > player.y: self.y -= self.speed
            reward = 1

        elif action == "RUN":
            self.x -= self.speed
            self.y -= self.speed
            reward = -1

        update_q(state, action, reward, get_state(self, player))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
