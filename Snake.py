import pygame
import random
import os
pygame.init()
pygame.mixer.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width=600
screen_height=400


# snake_x=45
# snake_y=100

snake_size=10
#
# food_size=8
# velocity_x=0
# velocity_y=0
#
# food_x=random.randint(20,screen_width/2)
# food_y=random.randint(20,screen_height/2)
#
# score=0
# init_velocity=5


gameWindow=pygame.display.set_mode((screen_width,screen_height))
bgImg=pygame.image.load("snake.jpg")
bgImg=pygame.transform.scale(bgImg,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("Snake Game")
pygame.display.update()

# exit_game=False
# game_over=False
# clock=pygame.time.Clock()
# fps=30
clock = pygame.time.Clock()

font=pygame.font.SysFont(None,30)
def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def screen_score2(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot(gameWindow,color,snake_list,snake_ysize):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, black, [x,y, snake_size, snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgImg, (0, 0))
        screen_score("Welcome!", white, 100, 70)
        screen_score("Press SpaceBar To Start", white, 40, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("bg.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    pygame.mixer.music.load("bg.mp3")
    pygame.mixer.music.play()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 100

    food_size = 8
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    score = 0
    init_velocity = 5

    fps = 30

    snake_list = []
    snake_length = 1
    if (not os.path.exists("Game.txt")):
        with open("Game.txt","w") as f:
            f.write("0")
    with open("Game.txt",'r') as f:
        highscore=f.read()

    while not exit_game:


        if game_over:
            with open("Game.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            screen_score("Game Over!Press Enter To Continue",black,130,170)
            screen_score("Press q to Quit!",black,210,195)

            screen_score2("Your Score : " + str(score) +" HighScore :" +str(highscore), black, 5, 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                        pygame.mixer.music.load("bg.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_q:
                        quit()


        else:

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    elif event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    elif event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    elif event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
                score+=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length+=5
                if score>int(highscore):
                    highscore=score

            if snake_y>screen_height or snake_x>screen_width or snake_x<0 or snake_y<0:
                game_over=True
                pygame.mixer.music.load("SmashITup.mpeg")
                pygame.mixer.music.play()
                # print("game over")
            gameWindow.fill(white)

            screen_score("Your Score : " + str(score)+" HighScore :" +str(highscore), black, 5, 5)



            head = []

            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load("SmashITup.mpeg")
                pygame.mixer.music.play()
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_xsize,snake_ysize])
            plot(gameWindow,white,snake_list,snake_size)

            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
        pygame.display.update()
        clock.tick(fps)

# gameloop()
welcome()
pygame.quit()
quit()

