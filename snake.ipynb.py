import pygame, sys, time, random

speed = 15 
#windows size 

frame_size_x = 720 
frame_size_y = 480


check_errors = pygame.int()

if(check_errors[1] > 0):
    print("error" + check_errors[1])
else:
    print("game succesfully initialized")

pygame.display.set.caption("SNAKE GAME")
game_window = pygame.display.set_model(frame_size_x, frame_size_y)

# Adding colors
black = pygame.color(0,0,0)
white = pygame.color(255,255,255)
red = pygame.color(255,0,0)
green = pygame.color(0,255,0)
blue = pygame.color(0,0,255)


fps_controler = pygame.time.Clock()
# one snke square size 
square_size = 20

#A função int() converte um dado string para um número inteiro.
def int_vars():
    #declarando as variaveis 
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    #definindo o valor pra cada variavel 
    direction = "RIGTH"
    head_pos = (120,60)
    snake_body = (120,60)
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, 
                random.randrange(1,(frame_size_y // square_size)) * square_size]
    food_spawn = True 
    score = 0 
    
    int_vars()     
    
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score: " + str(score), True, color )
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x / 10, 15)
        else 
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
        
        game_window.blit(surface, score_rect)
    #game laço de repetição
    
    while True:
        #true terminar com ":"
        # == serve como um teste para ver se duas coisas são iguais ou não
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #ordenação de funções por KEYS do teclado
            elif event.type == pygame.keydown:
                if ( event.key == pygame.K_UP or event.key == ord("w")
                   and direction != "DOWN"):
                    direction = "UP"
                elif ( event.key == pygame.K_DOWN or event.key == ord("S")
                   and direction != "UP"):
                    direction = "DOWN"
                elif ( event.key == pygame.K_RIGHT or event.key == ord("D")
                   and direction != "LEFT"):
                    direction = "RIGHT"
                elif ( event.key == pygame.K_LEFT or event.key == ord("A")
                   and direction != "RIGHT"):
                    direction = "LEFT"
        if direction == "UP": 
            # += é o mesmo que fazer, x=x + o valor, -= seria o mesmo que fazer, x=x - o valor? (perguntar//Professor)
            head_pos[1] -= square_size
        elif direction == "DOWN": 
            head_pos[1] += square_size
        elif direction == "LEFT":
            head_pos[0] -= square_size
        else:
             head_pos[0] += square_size
        
        if head_pos[0] < 0:
            head_pos[0] = frame_size_x - square_size
        elif head_pos[0] > frame_size_x - square_size                                                                                                                                                                                                 frame_size_x + square_size 
            head_pos[0] = 0
        elif head_pos [1] < 0: 
            head_pos[1] = frame_size_y - square_size
        elif head_pos[1] > frame_size_y - square_size
            head_pos[1] = 0 
        
        #eating apple
        
snake_body.insert(0, list(head_pos))
if head_pos[0] == food_pos[0] and head_pos[1] == food_pos:
    score += 1
    food_spawn = false 
else:
    snake_body.pop()

#spawn_food

if not food_spawn:
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, 
        random.randrange(1,(frame_size_y // square_size)) * square_size]

#gfx
game_window.fill(black)             
for pos in snake_body:
    pygame.draw.rect(game_window, green, pygame.rect(pos[0] + 2, pos[1] + 2, square_size - 2, square_size))
    
# game over conditions

for block in snake_body[1:]:
    if head_pos[0] == block[0] and head_pos[1] == block[1]:
        int_vars()
        
show_score(1, white 'consolas' 20)
pygame.display.update()                 
fps_controler.tick(speed)