import pygame, sys,time,random
from time import sleep

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction
snake_colour=(0,255,0)

#Parameters for food
food_pos = [0,0]
food_spawn = False
food_colour=(255,255,255)

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:  
                change_to='RIGHT'
             elif event.key == pygame.K_LEFT:  
                change_to='LEFT'
             elif event.key == pygame.K_UP:
                 change_to='UP'
             elif event.key == pygame.K_DOWN:
                 change_to='DOWN'















def update_snake(direction,snake_pos,food_pos,snake_colour,game_window,snake_body,change_to):
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction

    def detect_food(snake_pos,food_pos,score):
        if snake_pos==food_pos:
            score+=1
            if direction=='RIGHT':
                snake_body.append([snake_body[len(snake_body)-1]-10,snake_body[len(snake_body)-1]])
            if direction=='LEFT':
                snake_body.append([snake_body[len(snake_body)-1]+10,snake_body[len(snake_body)-1]])
            if direction=='UP':
                snake_body.append([snake_body[len(snake_body)-1],snake_body[len(snake_body)-1]+10])
            if direction=='DOWN':
                snake_body.append([snake_body[len(snake_body)-1],snake_body[len(snake_body)-1]-10])

            food_pos=create_food()
    
    def detect_collisions(snake_body,frame_size_x,frame_size_y):
        snake_head=pygame.Rect(snake_body[0][0],snake_body[0][1],10,10)
        if snake_head.top==0 or snake_head.bottom==frame_size_y or snake_head.left==0 or snake_head.right==frame_size_x:
            game_over()
        else:
            for i in range(1,len(snake_body)):
                if snake_head==pygame.Rect(snake_body[i][0],snake_body[i][1],10,10):
                    game_over()
        


    if direction==change_to:
        detect_food(snake_pos,food_pos,score)
        detect_collisions(snake_body,frame_size_x,frame_size_y)

        if direction=='RIGHT':
            for i in range(len(snake_body)):
                snake_body[i][0]+=10
        elif direction=='LEFT':
            for i in range(len(snake_body)):
                snake_body[i][0]-=10
        elif direction=='UP':
            for i in range(len(snake_body)):
                snake_body[i][1]-=10
        elif direction=='DOWN':
            for i in range(len(snake_body)):
                snake_body[i][1]+=10
        snake_pos=snake_body[0]

    elif direction=='RIGHT' and change_to=='UP':
        temp=snake_pos
        for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][1]-=10
                elif snake_body[j][1]<temp[1]:
                    snake_body[j][1]-=10
                else: 
                    snake_body[j][0]+=10
            snake_pos=snake_body[0]
        direction='UP'
        

    elif direction=='RIGHT' and change_to=='DOWN':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][1]+=10
                elif snake_body[j][1]>temp[1]:
                    snake_body[j][1]+=10
                else: 
                    snake_body[j][0]+=10
            snake_pos=snake_body[0]
         direction='DOWN'
        
    elif direction=='LEFT' and change_to=='UP':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][1]-=10
                elif snake_body[j][1]<temp[1]:
                    snake_body[j][1]-=10
                else: 
                    snake_body[j][0]-=10
            snake_pos=snake_body[0]
         direction='UP'
    
    elif direction=='LEFT' and change_to=='DOWN':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][1]+=10
                elif snake_body[j][1]>temp[1]:
                    snake_body[j][1]+=10
                else: 
                    snake_body[j][0]-=10
            snake_pos=snake_body[0]
         direction='DOWN'
        
    elif direction=='UP' and change_to=='RIGHT':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][0]+=10
                elif snake_body[j][0]>temp[0]:
                    snake_body[j][0]+=10
                else: 
                    snake_body[j][1]-=10
            snake_pos=snake_body[0]
         direction='RIGHT'
         
    elif direction=='UP' and change_to=='LEFT':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][0]-=10
                elif snake_body[j][0]<temp[0]:
                    snake_body[j][0]-=10
                else: 
                    snake_body[j][1]-=10
            snake_pos=snake_body[0]
         direction='LEFT'
        
    elif direction=='DOWN' and change_to=='RIGHT':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==temp:
                    snake_body[j][0]+=10
                elif snake_body[j][0]>temp[0]:
                    snake_body[j][0]+=10
                else: 
                    snake_body[j][1]+=10
            snake_pos=snake_body[0]
         direction='RIGHT'

    elif direction=='DOWN' and change_to=='LEFT':
         temp=snake_pos
         for i in range(len(snake_body)):
            detect_food(snake_pos,food_pos)
            detect_collisions(snake_body,frame_size_x,frame_size_y)
            for j in range(len(snake_body)):
                if snake_body[j]==snake_pos:
                    snake_body[j][0]-=10
                elif snake_body[j][0]<snake_pos[0]:
                    snake_body[j][0]-=10
                else: 
                    snake_body[j][1]+=10
            snake_pos=snake_body[0]
         direction='RIGHT'
    
    






    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    





    # End the game if the snake collides with the wall or with itself. 
    






def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    food_pos=[random.randrange(720),random.randrange(480)]
    pygame.draw.rect(game_window,food_colour,pygame.Rect(food_pos[0],food_pos[1],10,10))
    return food_pos



def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    score_img = pygame.font.SysFont(font,size).render("Score: %d"%score, True, color)
    score_rect = score_img.get_rect()
    score_rect.centerx = 50
    score_rect.top = 10
    game_window.blit(score_img, score_rect)






def update_screen(pos,color,font,size):
    """
    Draw the snake, food, background, score on the screen
    """
    for k in range(len(snake_body)):
                  pygame.draw.rect(game_window,snake_colour,pygame.Rect(snake_body[k][0],snake_body[k][1],10,10))
        
    show_score(pos, color, font, size)






def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    gameover_img = pygame.font.SysFont(None, 100).render("GAME OVER", True, (255,0,0))
    gameover_rect = gameover_img.get_rect()
    gameover_rect.centerx = frame_size_x/2
    gameover_rect.top = 200
    game_window.blit(gameover_img, gameover_rect)

    pygame.display.update()

    sleep(10)
    sys.exit(0)






# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    create_food()
    update_snake(direction,snake_pos,food_pos,snake_colour,game_window,snake_body,change_to)
    update_screen(1,(255,255,255),None,30)
    check_for_events()
    pygame.display.update()



    

    # To set the speed of the screen
    fps_controller.tick(25)