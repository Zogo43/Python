import pygame
import random
pygame.font.init()

WIDTH, HEIGHT = 400, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

FPS = 15
VEL = 10

WHITE = (255, 255, 255)
RED = (255, 0, 0)

LOSE_FONT = pygame.font.SysFont("calibri", 50)

# def spawn_apple():
#     coords = genrate_coordinates()
#     coords_x = coords[0]
#     coords_y = coords[1]
#     pygame.draw.rect(WIN, RED, [coords_x, coords_y, 10, 10])
#     print(str(coords_x) + " " + str(coords_y))

def draw_window(player, apple):
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, WHITE, [player.x, player.y, 10, 10])
    pygame.draw.rect(WIN, RED, [apple.x, apple.y, 10, 10])

    

def lose():
    draw_text = LOSE_FONT.render("GAME OVER",1 , WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    rng_x = random.randrange(0, 401, 10)
    rng_y = random.randrange(0, 301, 10)
    player = pygame.Rect(200, 150, 10, 10)
    apple = pygame.Rect(rng_x, rng_y, 10, 10)
    health = 1
    x_change = 0
    y_change = 0
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    x_change = 0
                    y_change = -VEL
                if event.key == pygame.K_a:
                    x_change = -VEL
                    y_change = 0
                if event.key == pygame.K_s:
                    x_change = 0
                    y_change = VEL
                if event.key == pygame.K_d:
                    x_change = VEL
                    y_change = 0
        if player.y <= 0 or player.y >= HEIGHT or player.x <= 0 or player.x >= WIDTH:
            health -= 1
        
        if health == 0:
            lose()
            break


        player.x += x_change
        player.y += y_change
        draw_window(player, apple)

        # if not apple_spawn:
        #     spawn_apple()
        #     apple_spawn = True

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()