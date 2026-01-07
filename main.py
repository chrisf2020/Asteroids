# file: main.py
# main game loop for Asteroids
# author: chris frias

from constants import *
from player import *
from asteroid import *
from asteroidfields import *
from shot import *
from screen import * 
from scores import *
import sys
import pygame
import os

def main():
    
    # print system info and screen dimensions
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # force pulseaudio driver to resolve linux audio device 
    os.environ['SDL_AUDIODRIVER'] = 'pulseaudio'
    
    # initialize all pygame modules and the mixer for sound
    pygame.init()
    pygame.mixer.init()
    game_active = False
    score = 0
    font = pygame.font.SysFont("monospace", 35)
    small_font = pygame.font.SysFont("monospace", 30)
    
    # load sound files and set volume levels
    explosion_sound = pygame.mixer.Sound("explosion.mp3")
    explosion_sound.set_volume(0.1)
    music = pygame.mixer.Sound("asteroidmusic.mp3")
    music.set_volume(0.05)
    pygame.mixer.Sound.play(music, loops=-1) 

    # setup the internal clock and the display surface
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # will hold all the objects that can be updated
    updatable = pygame.sprite.Group()
    # will hold all the objects that can be drawn
    drawable = pygame.sprite.Group()
    # will hold all asteroid objects for collision checking
    asteroids = pygame.sprite.Group()
    # will hold all bullet objects fired by the player
    shots = pygame.sprite.Group()

    # assign containers to classes so instances auto join groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField() 

    Player.containers = (updatable, drawable)
    # create the player object in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    Shot.containers = (shots, updatable, drawable)
   
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            # handle menu inputs
            if event.type == pygame.KEYDOWN:
                if not game_active:
                    if event.key == pygame.K_s or event.key == pygame.K_r:
                        # reset everything for a new game
                        game_active = True
                        score = 0
                        for a in asteroids: 
                            a.kill() # clear old asteroids
                        for s in shots: 
                            s.kill() # clear old shots
                        player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

        if game_active:
            screen.fill("black")
            updatable.update(dt)

            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    game_active = False 
                    save_score(score)
                
                for shot in shots:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()
                        pygame.mixer.Sound.play(explosion_sound)
                        score += 10

            for objects in drawable:
                objects.draw(screen)
            
            # draw live score
            score_label = small_font.render(f"Score: {score}", 1, (255, 255, 255))
            screen.blit(score_label, (10, 10))

        else:
            #menu
            if score == 0:
                draw_start_screen(screen, font, small_font)
            else:
                top_scores = get_high_scores()
                draw_dead_screen(screen, font, small_font, score, top_scores)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()