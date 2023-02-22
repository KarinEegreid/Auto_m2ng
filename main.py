import random

import pygame

# Define game constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CAR_WIDTH = 40
CAR_HEIGHT = 80

# Initialize Pygame
pygame.init()

# Load game images
background_image = pygame.image.load('bg_rally.jpg')
player_car_image = pygame.image.load('f1_red.png')
blue_car_image = pygame.image.load('f1_blue.png')

# Set up the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Car Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the starting score
score = 0
font = pygame.font.SysFont(None, 30)

# Create the player's car
player_car_rect = player_car_image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100))

# Create a list to hold the blue cars
blue_cars = []
for i in range(5):
    blue_car_rect = blue_car_image.get_rect(
        center=(random.randint(0, WINDOW_WIDTH - CAR_WIDTH), random.randint(-WINDOW_HEIGHT, 0)))
    blue_cars.append(blue_car_rect)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player's car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car_rect.left > 0:
        player_car_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player_car_rect.right < WINDOW_WIDTH:
        player_car_rect.move_ip(5, 0)

    # Move the blue cars and check for collisions
    for i, blue_car_rect in enumerate(blue_cars):
        blue_car_rect.move_ip(0, 5)
        if blue_car_rect.bottom >= WINDOW_HEIGHT:
            blue_car_rect.top = random.randint(-WINDOW_HEIGHT, 0)
            blue_car_rect.centerx = random.randint(0, WINDOW_WIDTH - CAR_WIDTH)
            score += 1
        if blue_car_rect.colliderect(player_car_rect):
            running = False
        blue_cars[i] = blue_car_rect

    # Draw the game
    window.blit(background_image, (0, 0))
    window.blit(player_car_image, player_car_rect)
    for blue_car_rect in blue_cars:
        window.blit(blue_car_image, blue_car_rect)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 30))
    pygame.display.flip()

    # Set the game's frame rate
    clock.tick(60)

# Clean up the game
pygame.quit()
