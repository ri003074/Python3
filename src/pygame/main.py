import pygame

# from pygame.locals import *
# import sys


def main():
    """ init """
    pygame.init()

    clock = pygame.time.Clock()

    """ create person/content/background """

    while True:
        """ clean up screen """

        """ person/content/background update """

        """ screen display """

        """ event handling """

        for event in pygame.event.get():
            pass
            # if event.typ == QUIT:
            #     pygame.quit()
            #     sys.exit()

        """ draw speed (FPS) """
        clock.tick(60)


if __name__ == "__main__":
    main()
