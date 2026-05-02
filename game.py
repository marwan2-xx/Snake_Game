from enum import Enum
import random
import sys
import pygame

class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

class snake:
    def __init__(self,body,direction):
        self.body = body # list of positions representing each segment of the sanke
        self.direction = direction #up,down,left,right
        self.length = len(body)
        self.growFlag = False
    def move(self):
        current_head = list(self.body[0])
        new_head = []
        if self.direction == Direction.RIGHT:
            new_head = [current_head[0], current_head[1]+1]
            
        elif self.direction == Direction.LEFT:
            new_head = [current_head[0], current_head[1]-1]
        elif self.direction == Direction.DOWN:
            new_head = [current_head[0]+1, current_head[1]]
        elif self.direction == Direction.UP:
            new_head = [current_head[0]-1, current_head[1]]
        new_head = tuple(new_head)
        self.body.insert(0,new_head)
        if(self.growFlag == False):
            self.body.pop()
        else:
            self.growFlag = False
            
        
        
        

            
    def change_direction(self,newDirection):
        opposites = {Direction.RIGHT : Direction.LEFT , 
                     Direction.LEFT : Direction.RIGHT , 
                     Direction.UP : Direction.DOWN , 
                     Direction.DOWN : Direction.UP
                     }
        if(opposites[self.direction] == newDirection):
            return
        else:
            self.direction = newDirection
    
    def grow(self):
        self.growFlag = True
    
    def check_self_collision(self):
        h = self.body[0]
        for i in range(1,len(self.body)):
            if self.body[i] == h:
                return True
        return False
    
    def get_head_position(self):
        return self.body[0]

class Food:
    def __init__(self , position):
        self.position = position
    
    def respawn(self , grid_width, grid_height, snake_body):
        
        while(True):
            counter = 0
            new_x = random.randint(0,grid_width-1)
            new_y = random.randint(0,grid_height-1)
            newPosition = (new_x , new_y)
            for i in range(0,len(snake_body)):
                segment = snake_body[i]
                if(newPosition != segment):
                    counter+=1
                else:
                    break

                
            
            if counter == len(snake_body):
                self.position = newPosition
                break
            else:
                continue
    


class Game:
    
    def __init__(self , snake , food  , grid_width , grid_height):
        self.snake = snake
        self.food = food
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.game_over = False
        self.cell_size = 20
        self.score = 0
        self.clock = pygame.time.Clock()
    
    def check_collision(self):
        headposition = self.snake.get_head_position()
        foodposition = self.food.position
        if(headposition == foodposition):
            self.score+=1
            self.snake.grow()
            self.food.respawn(self.grid_width, self.grid_height,self.snake.body)
        elif(headposition[0]<0 or headposition[0]>=self.grid_width or headposition[1]<0 or headposition[1]>=self.grid_height):
            self.game_over = True
        elif(self.snake.check_self_collision() == True):
            self.game_over = True
    
    def update(self):
        if(self.game_over == True):
            return
        self.snake.move()
        self.check_collision()
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicked the X button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # A key was pressed
                if event.key == pygame.K_UP:
                    self.snake.change_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(Direction.RIGHT)
    
    def draw(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        
        # Draw snake
        for i, segment in enumerate(self.snake.body):
            # Make rectangles slightly smaller to create gaps
            rect = pygame.Rect(segment[1] * self.cell_size + 2,  # +2 for gap
                            segment[0] * self.cell_size + 2,  # +2 for gap
                            self.cell_size - 4,  # -4 to make it smaller (2 on each side)
                            self.cell_size - 4)
            
            # Head is yellow, body is green
            if i == 0:  # First segment is the head
                pygame.draw.rect(screen, (255, 255, 0), rect)  # Yellow head
            else:
                pygame.draw.rect(screen, (0, 255, 0), rect)  # Green body
        
        # Draw food
        food_rect = pygame.Rect(self.food.position[1] * self.cell_size + 2,
                            self.food.position[0] * self.cell_size + 2,
                            self.cell_size - 4,
                            self.cell_size - 4)
        pygame.draw.rect(screen, (255, 0, 0), food_rect)  # Red food
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    


    
        
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.grid_width * self.cell_size, 
                                        self.grid_height * self.cell_size))
        pygame.display.set_caption('Snake Game')
        
        while not self.game_over:
            self.handle_input()
            self.update()
            self.draw(screen)
            self.clock.tick(10)  # 10 FPS (adjust for speed)
        
        # Game over - wait a bit then quit
        pygame.time.wait(2000)
        pygame.quit()





# Create initial snake
initial_snake_body = [(5, 5), (5, 4), (5, 3)]  # More centered
snake = snake(initial_snake_body, Direction.RIGHT)

# Create initial food at a random position
initial_food_position = (5, 5)  # You can start it anywhere
food = Food(initial_food_position)

# Create the game
game = Game(snake, food, grid_width=20, grid_height=20)

# Run the game
game.run()


        

    
        

        
            
            

                    
            


    