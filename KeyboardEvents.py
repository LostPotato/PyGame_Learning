import pygame
import os
# Centering the video frame
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Making an instance of the clock object
clock = pygame.time.Clock()
# telling the clock object to clock every 1/60

# initalize the game
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tank Game")
# sets the position of the inital x and y
x = 120
y = 120

running = True
while running:

    for event in pygame.event.get():
        # looking for the quit event
        if event.type == pygame.QUIT:
            running = False
            break

        # handling the key press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 8
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 8
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 8
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 8

    # filling the window with a black background
    window.fill((0,0,0))
    pygame.draw.rect(window,(0,0,255), (x,y,400,240))
    pygame.display.update()
    clock.tick(60)


pygame.quit()