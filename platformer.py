# todo list
# add jump function
# add collision
# add gravity


import pygame

# color def
white = (255, 255, 255)
black = (0, 0, 0)
# class def
class player():

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.x_speed = 0
        self.y_speed = 0


# main loop
def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen_size = [screen_width, screen_height]

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Platformer')

    p1 = player(screen_width/2, screen_height/2, 30)

    # event processing
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # left
                if event.key == pygame.K_a:
                    p1.x_speed += -1
                # right
                elif event.key == pygame.K_d:
                    p1.x_speed += 1
                # up
                elif event.key == pygame.K_w:
                    p1.y_speed += -1
                # down
                elif event.key == pygame.K_s:
                    p1.y_speed += 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    p1.x_speed = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    p1.y_speed = 0
        p1.x += p1.x_speed
        p1.y += p1.y_speed


        screen.fill(white)

        pygame.draw.rect(screen, black, [p1.x, p1.y, p1.size, p1.size])
        pygame.display.flip()



# run main
if __name__ == "__main__":
    main()

quit()



