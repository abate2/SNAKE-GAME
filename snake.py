import pygame, random, sys, time
pygame.init()

#Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

size = (800, 500)
run = False
change_direction = "right"
score = 0
font = pygame.font.SysFont("MathJax_Typewriter", 20)
fruit_color = RED
snake_color = GOLD

#Make the window
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
snake_head = [100, 0]
snake_body = [[100, 0], [110, 0]]

#functions
def food():
  random_x = (random.randint(0, 79)) * 10
  random_y = (random.randint(0, 49)) * 10
  fruit_pos = [random_x, random_y]
  return fruit_pos

def color():
  random_color = random.randint(1, 5)
  if random_color == 1:
    fruit_color = BLACK
  elif random_color == 2:
    fruit_color = RED
  elif  random_color == 3:
    fruit_color = GREEN
  elif  random_color == 4:
    fruit_color = BLUE
  elif random_color == 5:
    fruit_color = GOLD
  
  return fruit_color

fruit_pos = food() 


while not run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        change_direction = "down"
      if event.key == pygame.K_UP:
        change_direction = "up"
      if event.key == pygame.K_LEFT:
        change_direction = "left"
      if event.key == pygame.K_RIGHT:
        change_direction = "right"

  if change_direction == "down":
    snake_head[1] += 10
  elif change_direction == "up":
    snake_head[1] -= 10
  elif change_direction == "left":
    snake_head[0] -= 10
  elif change_direction == "right":
    snake_head[0] += 10
  #color de fondo
  screen.fill(WHITE)
  snake_body.insert(0, list(snake_head))

  if snake_head == fruit_pos:
    snake_color = fruit_color
    fruit_pos = food()
    fruit_color = color()
    score += 1
  else:
    snake_body.pop()

  driver = snake_head
  for i in range(1, len(snake_body)):
    #As we have a list  in a list, we need to save in a variable the position of the snake_body, which is a list too, and  then we can use the position of the coordinates ti make teh comparison
    section = snake_body[i]
    if driver[0] == section[0] and driver[1] == section[1]:
      run = True
      print("You have lost")
  if (snake_head[0] > (size[0])-10) or (snake_head[0] < 0) or (snake_head[1] > size[1]) or (snake_head[1] < 0) :
    run = True
    print("You have lost")
  
  text = font.render(f"Score = {score}", True, BLUE)
  #------DRAW ZONE
  for i in snake_body:
    pygame.draw.rect(screen, snake_color, pygame.Rect(i[0], i[1], 10, 10))
  
  pygame.draw.rect(screen, fruit_color, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))
  screen.blit(text,(690, 0)) 
    
  #------DRAW ZONE
  #actualizar pantalla
  pygame.display.flip()
  clock.tick(10)

pygame.quit()
