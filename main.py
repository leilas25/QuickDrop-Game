import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Objects")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 105, 180)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

catcher_width = 100
catcher_height = 20
catcher_x = (SCREEN_WIDTH - catcher_width) // 2
catcher_y = SCREEN_HEIGHT - catcher_height - 10 
catcher_speed = 5

object_size = 20
object_speed = 3
falling_objects = [] 

score = 0
missed_objects = 0
max_missed = 3
game_active = True

font = pygame.font.Font(None, 36) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_LEFT:
                    catcher_x -= catcher_speed * 2 
                if event.key == pygame.K_RIGHT:
                    catcher_x += catcher_speed * 2

    keys = pygame.key.get_pressed()
    if game_active:
        if keys[pygame.K_LEFT]:
            catcher_x -= catcher_speed
        if keys[pygame.K_RIGHT]:
            catcher_x += catcher_speed

    if catcher_x < 0:
        catcher_x = 0
    if catcher_x > SCREEN_WIDTH - catcher_width:
        catcher_x = SCREEN_WIDTH - catcher_width

    if game_active:
        if random.randint(1, 60) == 1: 
            new_object_x = random.randint(0, SCREEN_WIDTH - object_size)
            falling_objects.append(pygame.Rect(new_object_x, 0, object_size, object_size))

        for obj in falling_objects[:]:
            obj.y += object_speed
            
            if obj.colliderect(pygame.Rect(catcher_x, catcher_y, catcher_width, catcher_height)):
                falling_objects.remove(obj)
                score += 1

            elif obj.y > SCREEN_HEIGHT:
                falling_objects.remove(obj)
                missed_objects += 1
                if missed_objects >= max_missed:
                    game_active = False

    screen.fill(BLACK) 
    
    if game_active:

        pygame.draw.rect(screen, BLUE, (catcher_x, catcher_y, catcher_width, catcher_height))

        for obj in falling_objects:
            pygame.draw.circle(screen, PINK, (obj.x + obj.width // 2, obj.y + obj.height // 2), object_size // 2) 

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        missed_text = font.render(f"Missed: {missed_objects}/{max_missed}", True, WHITE)
        screen.blit(missed_text, (10, 50))
    else:

        game_over_text = font.render("GAME OVER! Final Score: " + str(score), True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score = 0
                    missed_objects = 0
                    falling_objects = []
                    catcher_x = (SCREEN_WIDTH - catcher_width) // 2
                    game_active = True
                elif event.key == pygame.K_q:
                    running = False


    pygame.display.flip()

    pygame.time.Clock().tick(60) 

pygame.quit()