from renderer import Renderer
import pygame

renderer = Renderer()

class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("EcoPy")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(renderer.fill_color)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()