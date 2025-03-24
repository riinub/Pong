from settings import * 
from sprites import *
from math import pi
import json

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.running = True
        self.clock = pygame.time.Clock()
        #sprite groups
        # it creates a container for sprites objects that i will create using a sprite class
        self.all_sprites = pygame.sprite.Group() 
        self.paddle_sprite = pygame.sprite.Group()

        self.player = Player((self.all_sprites, self.paddle_sprite))
        self.ball = Ball(self.all_sprites, self.paddle_sprite, self.update_score)
        Opponent((self.all_sprites, self.paddle_sprite), self.ball)

        try:
            with open(join('data', 'score.txt' )) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player': 0, 'opponent': 0}

        self.font = pygame.font.Font(None, 120)

    def display_score(self):
        pygame.draw.circle(self.display_surface, COLORS['bg'], [WINDOW_WIDTH/2,WINDOW_HEIGHT/2], 160)
        pygame.draw.line(self.display_surface, COLORS['bg'], (WINDOW_WIDTH/ 2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 5)
        #player
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg'])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 370, 60))
        self.display_surface.blit(player_surf, player_rect)
        
        #opponent
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg'])
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH / 2 - 370, 60))
        self.display_surface.blit(opponent_surf, opponent_rect)

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def run(self):
        while self.running:
            dt = self.clock.tick() / 500
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)

            self.all_sprites.update(dt)

            self.display_surface.fill(COLORS['background'])
            self.display_score()
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

