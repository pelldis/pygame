import sys
import pygame

def check_events():
    # Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
        # Отображение последнего прорисованного экрана.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.update()