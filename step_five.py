import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

def main():
    pygame.init()
    clock = pygame.time.Clock()
    bg = (255, 255, 255)
    size =[800, 600]

    screen = pygame.display.set_mode(size)

    player = Sprite([40, 50], (255, 0, 0))
    velocity = 2.5

    wall = Sprite([100, 60], (0, 0, 0))
    wall2 = Sprite([60, 100], (0, 0, 0))

    wall_group = pygame.sprite.Group()
    wall_group.add(wall, wall2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            player.rect.x += velocity * -1
        if key[pygame.K_RIGHT]:
            player.rect.x += velocity * 1
        if key[pygame.K_UP]:
            player.rect.y += velocity * -1
        if key[pygame.K_DOWN]:
            player.rect.y += velocity * 1

        screen.fill(bg)

        pygame.sprite.spritecollide(player, wall_group, True)

        player_group.draw(screen)
        wall_group.draw(screen)

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
