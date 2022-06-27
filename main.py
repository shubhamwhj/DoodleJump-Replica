import pygame, sys
from game import gamePlay,create_screen
#initializing pygame
pygame.init()
clock=pygame.time.Clock()

#Screen setup
screen=create_screen()

'''
- Infinite Scrolling Background-done
- Continuous Scrolling Background- done

- Game Text -done
- Game States-done
'''

#loading bakcground images
bg_animation=pygame.image.load("assets/background3.jpg") 
bg_animation= pygame.transform.scale(bg_animation, (500, 1200))

#initial and end screen
start_surf=pygame.image.load("assets/startpopup.png")
score_surf=pygame.image.load("assets/scoreimg.png") 

#variable controlling y-axis value for the background
backY=-600

#variable controlling the state of the game
game_state="initial"

#Game Loop
while True:
    screen.fill((255,255,255))
    screen.blit(bg_animation,[0,backY])
     
    game_state=gamePlay()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    if game_state=="initial":
        screen.blit(start_surf,[70,120])  
    if game_state=="play":
        #moving the background
        backY+=1
        #resetting the background to -500
        if backY==0:
            backY=-600
    if game_state=="end":
       screen.blit(score_surf,[120,150])
    pygame.display.flip()
    clock.tick(30)