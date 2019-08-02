import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    bg = (255, 255, 255)
    size =[800, 600]

    screen = pygame.display.set_mode(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill(bg)

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
