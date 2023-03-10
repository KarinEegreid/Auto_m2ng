# Karl Paju IS22

# importime vajalikud packaged

import random

import pygame

# Define game constants
WINDOW_WIDTH = 640  # ekraani laius
WINDOW_HEIGHT = 480  # ekraani pikkus
CAR_WIDTH = 40  # auto laius
CAR_HEIGHT = 80  # auto pikkus

# Initialize Pygame
pygame.init()

# Defineerime pildid
background_image = pygame.image.load('bg_rally.jpg')  # anname background_image muutujale väärtuse
player_car_image = pygame.image.load('f1_red.png')  # anname player_car_image muutujale väärtuse
blue_car_image = pygame.image.load('f1_blue.png')  # anname blue_car_image muutujale väärtuse

# Seadistame ekraani
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Ekraani parameetrid
pygame.display.set_caption("Car Game")  # ekraani pealkiri

# Seadistame kella ehk siis kaadrisageduse
clock = pygame.time.Clock()

# Loome skoori
score = 0  # alg skoor
font = pygame.font.SysFont(None, 30)  # Teksti suuruse ning fondi lisamine mängu

# Loome mängija auto
player_car_rect = player_car_image.get_rect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100))  # Loome punase auto ning määrame selle ekraani keskele.

# Loome listi, mille sees on sinised autod
blue_cars = []
for i in range(5):
    blue_car_rect = blue_car_image.get_rect(
        center=(random.randint(0, WINDOW_WIDTH - CAR_WIDTH), random.randint(-WINDOW_HEIGHT, 0)))
    blue_cars.append(blue_car_rect)

# peamine loop mängu jaoks
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Et kasutaja saaks liigutada enda autot
    keys = pygame.key.get_pressed()  # muutujale andakse väärtus kui vajutatakse mingit nuppu
    if keys[pygame.K_LEFT] and player_car_rect.left > 0:  # kui vajutatakse vasakut klahvi läheb auto vasakule
        player_car_rect.move_ip(-5, 0)  # iga klahvi vajutusega liigub auto -5 võrra x teljes vasakule
    if keys[
        pygame.K_RIGHT] and player_car_rect.right < WINDOW_WIDTH:  # kui vajutakse paremat klahvi läheb auto paremale
        player_car_rect.move_ip(5, 0)  # # iga klahvi vajutusega liigub auto 5 võrra x teljes paremale

    # Liigutab siniseid autosi ning kontrollib kas kasutaja auto on kokku põrganud nendega
    for i, blue_car_rect in enumerate(blue_cars): # See rida käivitab tsükli, mis läbib iga sinise auto ja selle asukoha, mida hoitakse muutujas "blue_cars". Tsükkel kasutab funktsiooni "enumerate", et saada juurdepääs nii elementide indeksitele kui ka nende väärtustele. Seega muutuja "i" sisaldab indeksit ning "blue_car_rect" sisaldab konkreetse auto asukoha koordinaate.
        blue_car_rect.move_ip(0, 5) # liigutab sinise auto koordinaate alla poole, muutes nii selle asukohta ekraanil.
        if blue_car_rect.bottom >= WINDOW_HEIGHT: # Järgnevad read kontrollivad, kas auto on liikunud ekraanist välja, ja kui see on juhtunud, siis genereeritakse uued juhuslikud koordinaadid auto ümberpaigutamiseks ekraani ülaosale.
            blue_car_rect.top = random.randint(-WINDOW_HEIGHT, 0)
            blue_car_rect.centerx = random.randint(0, WINDOW_WIDTH - CAR_WIDTH)
            score += 1
        if blue_car_rect.colliderect(player_car_rect): # kontrollib, kas mängija auto (player_car_rect) ja sinine auto (blue_car_rect) ristuvad. Kui nad ristuvad, siis seatakse running muutuja väärtuseks False, mis paneb mängu lõppema.
            running = False
        blue_cars[i] = # blue_car_rect Teine tegevus rida blue_cars[i] = blue_car_rect määrab sinise auto (blue_car_rect) koordinaadid siniste autode listis (blue_cars) asukohaga i.

    # Joonistab mängu
    window.blit(background_image, (0, 0))  # Määrame tausta
    window.blit(player_car_image, player_car_rect)  # määrame punase auto asukoha
    for blue_car_rect in blue_cars: # käivitab tsükli kõikide siniste autode listi 
        window.blit(blue_car_image, blue_car_rect) # kuvab aknasse (window.blit()) sinise auto pildi (blue_car_image) antud koordinaatidega (blue_car_rect). See kuvab kõik sinised autod ekraanile.
    score_text = font.render("Score: " + str(score), True, #  loob tekstiobjekti (font.render()) skoori näitamiseks.
                             (255, 255, 255))  # renderime ekraanile sisestatud parameetrid
    window.blit(score_text, (WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 30))  # määrame skoori asukoha ekraanil
    pygame.display.flip()  # uuendame ekraani

    # seadistame fpsi
    clock.tick(60)  # määrame kaadrisageduse 60-ks

pygame.quit()
