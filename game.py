import pygame, sys, random
#initializing pygame
pygame.init()
clock=pygame.time.Clock()

#Screen setup
screen_width=500
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))


'''
- Infinite Scrolling Background
- Continuous Scrolling Background"

- Game Text 
- Game States"
'''
def create_screen():
    global screen
    return screen

def loadAnimations(path_list,scale=1):
    animation_surf_list=[]
    for img_path in path_list:
        surf=pygame.image.load(img_path).convert_alpha()
        if scale!=1:
            surf = pygame.transform.scale(surf,(int(surf.get_width()*scale),int(surf.get_height()*scale)))
        animation_surf_list.append(surf)
    return animation_surf_list;

def flipAnimations(surf_list):
    flip_surf_list=[]
    for surf in surf_list:
        surf=pygame.transform.flip(surf,True,False)
        flip_surf_list.append(surf)
    return flip_surf_list

#Images
bg=pygame.image.load("assets/blurbg3.png") 
bg= pygame.transform.scale(bg, (500, 1200))

bg_animation=loadAnimations(["assets/blurbg1.png","assets/background3.jpg","assets/blurbg2.png","assets/blurbg3.png","assets/background3.jpg","assets/blurbg1.png","assets/blurbg2.png","assets/blurbg3.png"],1.18)
bush_surf=pygame.image.load("assets/bush.png") 
stone_surf=pygame.image.load("assets/stone.png") 
flower_surf=pygame.image.load("assets/flower1.png") 
score_surf=pygame.image.load("assets/scoreimg.png") 
start_surf=pygame.image.load("assets/startpopup.png") 
platforms_animation=loadAnimations(["assets/platform7.png","assets/platform7.png","assets/platform7.png","assets/platform7.png","assets/platform7.png","assets/platform7.png"])
coin_animation=loadAnimations(["assets/Coins/image 1.png","assets/Coins/image 3.png","assets/Coins/image 5.png","assets/Coins/image 7.png","assets/Coins/image 9.png","assets/Coins/image 11.png","assets/Coins/image 13.png","assets/Coins/image 15.png"],0.18)
player_animation_right=loadAnimations(["assets/joe0.png","assets/joe1.png","assets/joe2.png","assets/joe3.png","assets/joe4.png"],0.7) 
player_animation_left=flipAnimations(player_animation_right)
player_animation=player_animation_right
bird_animation_right=loadAnimations(["assets/bird/1.png","assets/bird/2.png","assets/bird/3.png","assets/bird/4.png"])
bird_animation_left=flipAnimations(bird_animation_right)
enemy_animation=bird_animation_right
egg_surf=pygame.image.load("assets/bird/egg.png")
enery_ball_surf=pygame.image.load("assets/UFO/energyball.png")
ufo_animation_right=loadAnimations(["assets/UFO/ufo.png","assets/UFO/ufo.png","assets/UFO/ufo.png","assets/UFO/ufo.png"])

platforms=[]
coins=[]

player=pygame.Rect(200,120,25,10)
player.center=[250,300]

enemy=pygame.Rect(10,10,enemy_animation[0].get_width(),enemy_animation[0].get_height())

egg=pygame.Rect(10,10,egg_surf.get_width(),egg_surf.get_height())

#font
score_font=pygame.font.Font('freesansbold.ttf', 16)
over_font=pygame.font.Font('freesansbold.ttf', 25)
  
#Game variables
temp_dist=0
dy=0
dx=0
gravity=1
score=0
backY=0
gameState="initial"
coin_ani_index=0
coin_ani_speed=0
collected_coins=0
player_ani_index=0
can_jump=True
bg_index=0
enemy_ani_index=0
enemy_velocity=3

def shoot():
    egg.y+=7
    if egg.y>900:
        egg.top=enemy.bottom
        egg.x=enemy.x
        
def createPlatform(x,y):
    base=pygame.Rect(x,y,70,15)
    platforms.append([base,random.randint(1,4)])

def createCoins(x,y):
    base=pygame.Rect(x,y,70,15)
    coins.append(base)  
    
def initialPlatforms():
    createPlatform(80,-60)
    createPlatform(200,0)
    createPlatform(100,60)
    createPlatform(420,120)
    createPlatform(100,180)
    createPlatform(200,240)
    createPlatform(340,300)
    createPlatform(200,360)
    createPlatform(10,420)
    createPlatform(400,480)
    createPlatform(420,540)

initialPlatforms()    
    
#Creating platform event
NEW_PLATFORM= pygame.USEREVENT + 2
pygame.time.set_timer(NEW_PLATFORM, 1000)



#Game Loop
def gamePlay():
    global score,bg_animation,bg_index,backY,can_jump,coin_ani_speed,coin_ani_index,enemy_ani_index, dx,player_ani_index,enemy_animation,dy
    global gameState,collected_coins,enemy_velocity, player_animation,egg_surf,bird_animation_left,bird_animation_right
    
    try:
        from main import game_state 
        game_state=gameState
    except:
        pass
    #screen.fill((255,255,255))
    #screen.blit(bg_animation[int(bg_index+score/400)],[0,backY])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_animation=player_animation_left
                dx=-5
            if event.key == pygame.K_RIGHT:
                player_animation=player_animation_right
                dx=5
            if event.key == pygame.K_UP  and can_jump:
                player_ani_index=-1
                dy=-18
                can_jump=False
            if event.key == pygame.K_SPACE:
                gameState="play"
            if event.key == pygame.K_r and gameState=="end":
                player.center=[250,300]
                score=0
                gameState="play"
                collected_coins=0
                bg_index=0
                bird_animation_right=loadAnimations(["assets/bird/1.png","assets/bird/2.png","assets/bird/3.png","assets/bird/4.png"])
                bird_animation_left=flipAnimations(bird_animation_right)
                egg_surf=pygame.image.load("assets/bird/egg.png")
                enemy_animation=bird_animation_right
                platforms[5][0].x=220
                platforms[5][0].y=350
                enemy.x=-99
                enemy_velocity=-3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx=0
            if event.key == pygame.K_RIGHT:
                dx=0
        if event.type == NEW_PLATFORM:
            pass
            #createPlatform(random.randint(50,400),-20)
    coin_ani_speed+=1
    
    if coin_ani_speed==4:
        coin_ani_speed=1
        coin_ani_index+=1
        if coin_ani_index>=len(coin_animation):
            coin_ani_index=0
    if dx!=0 and can_jump:
        player_ani_index+=0.8
        
    if player_ani_index>=len(player_animation_left):
        player_ani_index=0
    
    enemy_ani_index+=0.4
    if enemy_ani_index>=len(enemy_animation):
        enemy_ani_index=0
   
    shoot()
    move=1  
    
    for platform in platforms:
        #pygame.draw.rect(screen,RED,platform[0])
        screen.blit(platforms_animation[platform[1]],platform[0])
        if  platform[1]==3:
            screen.blit(stone_surf,(platform[0].x,platform[0].y-20))
        if  platform[1]==2:
            screen.blit(flower_surf,(platform[0].x,platform[0].y-25))
        if  platform[1]==1:
            screen.blit(bush_surf,(platform[0].x,platform[0].y-25))
        if  platform[1]==4:
            if player.colliderect(platform[0].x+20,platform[0].y-25,coin_animation[coin_ani_index].get_width(),coin_animation[coin_ani_index].get_height()):
                  platform[1]=5
                  collected_coins+=1
                  score+=10
            else:  
                  screen.blit(coin_animation[coin_ani_index],(platform[0].x+20,platform[0].y-25))
           
        if platform[0].y>screen_height+100:
            platforms.remove(platform)
            createPlatform(random.randint(0,420), -10-score/5)
            #check collision with platform if moved by dy
        if player.colliderect(platform[0].x,platform[0].y-dy,platform[0].width,platform[0].height) and player.y < platform[0].y and dy>0:      
            dy=1+int(score/400)
            can_jump=True
            move=0    
            
            
    if gameState=="initial":  
        player.center=[250,300]
        score=0
    elif gameState=="play":   
        
        backY+=2
        if backY>=0:
            backY=-530
        dy+=gravity    
        
        for platform in platforms:
             platform[0].y+=2+int(score/400)
        
        #Calculating the score and increasing it only when player goes up
        if(dy<0):
            score+=1
           
        #Moving the player by dx and dy
        player.x+=dx
        player.y+=dy
        
        if player.y>700 or player.colliderect(enemy) or player.colliderect(egg):
            gameState="end"
            dy=0
        if player.x<-30:
            player.x=screen_width
        if player.x>screen_width:
            player.x=-30
            
        enemy.x+=enemy_velocity
       
        if enemy.x>600 :
           enemy_animation=bird_animation_left
           enemy_velocity*= -1
        elif enemy.x<-100:
           enemy_animation=bird_animation_right 
           enemy_velocity*= -1
        
        if score>50:
            bird_animation_left=ufo_animation_right
            bird_animation_right=ufo_animation_right
            if enemy_animation==ufo_animation_right:
                egg_surf=enery_ball_surf
            
        screen.blit(player_animation[int(player_ani_index)],[player.x,player.y-40]) 
        screen.blit(enemy_animation[int(enemy_ani_index)],enemy) 
        screen.blit(egg_surf,egg) 
        #pygame.draw.rect(screen,[200,0,0],player)
       
        
    elif gameState=="end":
        score_text=over_font.render(str(score), False, (255,255,255))     
        screen.blit(score_text,[240,250])  
       
    
        #pygame.draw.rect(screen,GREEN,player)  
    score_text=score_font.render("Score : "+ str(score), False, (3,3,3))   
    screen.blit(score_text,[10,10])  
    
    coin_text=score_font.render("X"+ str(collected_coins), False, (3,3,3))   
    screen.blit(coin_text,[460,15])  
    screen.blit(coin_animation[0],[430,10])
    return gameState
    pass

'''
while True:
    screen.fill((255,255,255))
    screen.blit(bg_animation[int(bg_index+score/400)],[0,backY])
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_animation=player_animation_left
                dx=-5
            if event.key == pygame.K_RIGHT:
                player_animation=player_animation_right
                dx=5
            if event.key == pygame.K_UP  and can_jump:
                player_ani_index=-1
                dy=-18
                can_jump=False
            if event.key == pygame.K_SPACE:
                gameState="play"
            if event.key == pygame.K_r and gameState=="end":
                player.center=[250,300]
                score=0
                gameState="play"
                collected_coins=0
                bg_index=0
                bird_animation_right=loadAnimations(["assets/bird/1.png","assets/bird/2.png","assets/bird/3.png","assets/bird/4.png"])
                bird_animation_left=flipAnimations(bird_animation_right)
                egg_surf=pygame.image.load("assets/bird/egg.png")
                enemy_animation=bird_animation_right
                platforms[5][0].x=220
                platforms[5][0].y=350
                enemy.x=-99
                enemy_velocity=-3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx=0
            if event.key == pygame.K_RIGHT:
                dx=0
        if event.type == NEW_PLATFORM:
            pass
            #createPlatform(random.randint(50,400),-20)
    coin_ani_speed+=1
    
    if coin_ani_speed==4:
        coin_ani_speed=1
        coin_ani_index+=1
        if coin_ani_index>=len(coin_animation):
            coin_ani_index=0
    if dx!=0 and can_jump:
        player_ani_index+=0.8
        
    if player_ani_index>=len(player_animation_left):
        player_ani_index=0
    
    enemy_ani_index+=0.4
    if enemy_ani_index>=len(enemy_animation):
        enemy_ani_index=0
   
    shoot()
    move=1  
    
    for platform in platforms:
        #pygame.draw.rect(screen,RED,platform[0])
        screen.blit(platforms_animation[platform[1]],platform[0])
        if  platform[1]==3:
            screen.blit(stone_surf,(platform[0].x,platform[0].y-20))
        if  platform[1]==2:
            screen.blit(flower_surf,(platform[0].x,platform[0].y-25))
        if  platform[1]==1:
            screen.blit(bush_surf,(platform[0].x,platform[0].y-25))
        if  platform[1]==4:
            if player.colliderect(platform[0].x+20,platform[0].y-25,coin_animation[coin_ani_index].get_width(),coin_animation[coin_ani_index].get_height()):
                  platform[1]=5
                  collected_coins+=1
                  score+=10
            else:  
                  screen.blit(coin_animation[coin_ani_index],(platform[0].x+20,platform[0].y-25))
           
        if platform[0].y>screen_height+100:
            platforms.remove(platform)
            createPlatform(random.randint(0,420), -10-score/5)
            #check collision with platform if moved by dy
        if player.colliderect(platform[0].x,platform[0].y-dy,platform[0].width,platform[0].height) and player.y < platform[0].y and dy>0:      
            dy=1+int(score/400)
            can_jump=True
            move=0    
            
            
    if gameState=="initial":  
        screen.blit(start_surf,[70,120])  
        player.center=[250,300]
        score=0
    elif gameState=="play":   
        
        backY+=2
        if backY>=0:
            backY=-530
        dy+=gravity    
        
        for platform in platforms:
             platform[0].y+=2+int(score/400)
        
        #Calculating the score and increasing it only when player goes up
        if(dy<0):
            score+=1
           
        #Moving the player by dx and dy
        player.x+=dx
        player.y+=dy
        
        if player.y>700 or player.colliderect(enemy) or player.colliderect(egg):
            gameState="end"
            dy=0
        if player.x<-30:
            player.x=screen_width
        if player.x>screen_width:
            player.x=-30
            
        enemy.x+=enemy_velocity
       
        if enemy.x>600 :
           enemy_animation=bird_animation_left
           enemy_velocity*= -1
        elif enemy.x<-100:
           enemy_animation=bird_animation_right 
           enemy_velocity*= -1
        
        if score>50:
            bird_animation_left=ufo_animation_right
            bird_animation_right=ufo_animation_right
            if enemy_animation==ufo_animation_right:
                egg_surf=enery_ball_surf
            
        screen.blit(player_animation[int(player_ani_index)],[player.x,player.y-40]) 
        screen.blit(enemy_animation[int(enemy_ani_index)],enemy) 
        screen.blit(egg_surf,egg) 
        #pygame.draw.rect(screen,[200,0,0],player)
       
        
    elif gameState=="end":
        score_text=over_font.render(str(score), False, (255,255,255))     
        screen.blit(score_surf,[120,150])
        screen.blit(score_text,[240,250])  
       
    
        #pygame.draw.rect(screen,GREEN,player)  
    score_text=score_font.render("Score : "+ str(score), False, (3,3,3))   
    screen.blit(score_text,[10,10])  
    
    coin_text=score_font.render("X"+ str(collected_coins), False, (3,3,3))   
    screen.blit(coin_text,[460,15])  
    screen.blit(coin_animation[0],[430,10])
        
    pygame.display.flip()
    clock.tick(30)
'''
    