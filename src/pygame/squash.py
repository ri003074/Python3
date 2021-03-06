import pygame
from pygame.locals import Rect, QUIT, MOUSEBUTTONDOWN
import sys
import math

SCREEN = Rect((0, 0, 400, 600))


class Paddle:
    def __init__(self):
        self.image = pygame.Surface((50, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN.centerx, SCREEN.bottom - 50)

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(SCREEN)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Ball:
    def __init__(self, pad):
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.pad = pad
        self.rect = self.image.get_rect()
        self.rect.bottom = self.pad.rect.top
        self.rect.centerx = self.pad.rect.centerx
        self.dx, self.dy = 5, -6
        self.status = "INIT"

    def start(self):
        self.status = "RUNNING"

    def update(self):
        if self.status == "INIT":
            self.rect.centerx = self.pad.rect.centerx
            self.rect.bottom = self.pad.rect.top
            return

        old_rect = self.rect.copy()
        self.rect.move_ip(self.dx, self.dy)

        if self.rect.colliderect(self.pad.rect):  # 衝突判定
            # pad.rect -> pad, old_rect -> ball
            if self.pad.rect.left >= old_rect.right:  # padの左側の座標よりballの右側の座標が小さい時
                self.rect.right = self.pad.rect.left
                self.dx = -self.dx
            elif self.pad.rect.right <= old_rect.left:  # padの右側の座標よりballの左側の座標が大きい時
                self.rect.left = self.pad.rect.right
                self.dx = -self.dx
            elif self.pad.rect.top >= old_rect.bottom:  # 上から判定
                self.rect.bottom = self.pad.rect.top
                x = self.rect.centerx - self.pad.rect.left
                y = -100 * x / self.pad.rect.width + 145
                self.dx = 5 * math.cos(math.radians(y))
                self.dy = -5 * math.sin(math.radians(y))

        if self.rect.left < SCREEN.left or self.rect.right > SCREEN.right:
            self.dx = -self.dx
        if self.rect.top < SCREEN.top:
            self.dy = -self.dy
        if self.rect.bottom > SCREEN.bottom:
            self.status = "INIT"

        self.rect.clamp_ip(SCREEN)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    """ init """
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("SQUASH GAME")

    clock = pygame.time.Clock()

    pad = Paddle()
    ball = Ball(pad)

    """ create person/content/background """

    while True:
        """ clean up screen """
        screen.fill((0, 0, 0))

        """ person/content/background update """
        pad.update()
        ball.update()

        """ person/content/background draw """
        pad.draw(screen)
        ball.draw(screen)

        # pad_rect.clamp_ip(SCREEN)
        # ball_rect.centerx = pad_rect.centerx
        """ screen display """
        pygame.display.update()

        ball.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                ball.start()

        """ draw speed (FPS) """
        clock.tick(200)


if __name__ == "__main__":
    main()
