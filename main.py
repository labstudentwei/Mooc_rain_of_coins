import pygame
import random
 
class Rain_of_coins:
    def __init__(self):
        pygame.init()
 
        self.load_images()
        self.screen = pygame.display.set_mode((800,600))
        self.robot_position = [0, 600 - self.images[3].get_height()]
        self.font = pygame.font.Font(None, 36)
        self.run_game()
        self.game_over = False
 
        
        pygame.display.set_caption("A Rain of Coins")
 
    
    def load_images(self):
        self.images = []
        for name in ["coin","door","monster","robot"]:
            self.images.append(pygame.image.load(name + ".png"))
 
 
    def run_game(self):
 
        
        clock = pygame.time.Clock()
        coins = []
        monsters = []
        frame_count = 0
        movement = 5
        coin_count = 0
        monster_count = 0
        self.game_over = False
 
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.robot_position[0] -= movement
            if keys[pygame.K_RIGHT]:
                self.robot_position[0] += movement
 
            self.screen.blit(self.images[3], self.robot_position)
            
            if self.game_over == False:
                frame_count += 1
 
            if frame_count % 80 == 0:
                coins.append([random.randint(0, 800-self.images[0].get_width()), -self.images[0].get_height()])
            
            for coin in coins:
                coin[1] += 2  
                self.screen.blit(self.images[0], (coin[0], coin[1]))
            
            if frame_count % 200 == 0:
                monsters.append([random.randint(0, 800-self.images[2].get_width()), -self.images[2].get_height()])
            
            for monster in monsters:
                monster[1] += 1  
                self.screen.blit(self.images[2], (monster[0], monster[1]))
 
            for coin in coins:
                if coin[0]-self.images[0].get_width()/2 <self.robot_position[0]< coin[0]+self.images[0].get_width()/2 and self.robot_position[1]< coin[1] + self.images[0].get_height():
                    coin_count += 1
                    coins.remove(coin)
            for monster in monsters:
                if monster[0]-self.images[2].get_width()/2 <self.robot_position[0]< monster[0]+self.images[2].get_width()/2 and self.robot_position[1]< monster[1] + self.images[2].get_height():
                    monster_count += 1
                    monsters.remove(monster)
 
            game_points = coin_count - monster_count
 
            if game_points > 0: 
                self.game_over = True
                game_passed_text = self.font.render("You Win!", True, (0, 0, 0))
                self.screen.blit(game_passed_text, (350, 300))
            else:
                game_points_text = self.font.render("Game Points: " + str(game_points), True, (0, 0, 0))
                self.screen.blit(game_points_text, (10, 70))
 
            game_intro_text = self.font.render("Collect coins and avoid monsters! Reach 5 points to win!", True, (0, 0, 0))
            self.screen.blit(game_intro_text, (10, 10))
            game_intro_text2 = self.font.render("Use LEFT and RIGHT arrow keys to move:)", True, (0, 0, 0))
            self.screen.blit(game_intro_text2, (10, 40))
 
 
 
 
            pygame.display.flip()
            clock.tick(60)  
 
        pygame.quit()

    

 
 
if __name__ == "__main__":
    Rain_of_coins()
    
 