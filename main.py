import pygame
from player import *
from constants import *
from asteroidfield import *
from asteroid import *

def main():
    print("Starting Asteroids!")
#    print(f"Screen width: {constants.SCREEN_WIDTH}")
 #   print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroids, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (shot_group, updateable_group, drawable_group)

    asteroid = AsteroidField()
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2
    player = Player(x, y)
    
    running = True
    while running:
        for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        #pygame.display.flip()
        dt = clock.tick(60)/1000

        updateable_group.update(dt)
        for rock in asteroids:
            if rock.is_colliding(player):
                print("Game over!")
                running = False
        for drawable in drawable_group:
            drawable.draw(screen)
        for rock in asteroids:
            for shot in shot_group:
                if rock.is_colliding(shot):
                    rock.split()
                    shot.kill()
        pygame.display.update()

    pygame.quit()
if __name__ == "__main__":
    main()
