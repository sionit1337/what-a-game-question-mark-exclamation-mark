import pygame

res = (1280, 720)

fps = 60

black = pygame.Color(10, 5, 10)
white = pygame.Color(240, 240, 240)
yellow = pygame.Color(255, 160, 0)
red = pygame.Color(255, 0, 0)


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Test")
        self.clock = pygame.time.Clock()

        self.player = Player()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            self.screen.fill(black)

            self.player.main(self.screen)

            self.clock.tick(fps)

            pygame.display.flip()


class Player:
    def __init__(self, x_pos=res[0] / 2, y_pos=res[1] / 2, x_vel=0, y_vel=0, size=15):
        self.x = x_pos
        self.y = y_pos

        self.dx = x_vel
        self.dy = y_vel

        self.size = size
        self.weight = size / 1.5

        self.velocity = pygame.math.Vector2()

        self.gravity = 0.93
        self.terminal_velocity = self.weight * self.gravity

        self.type = "player"

    def draw(self, surface):
        pygame.draw.circle(surface=surface, color=red, radius=self.size, center=(self.x, self.y))

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.size <= 0:
            self.x = self.size
            self.dx *= -1

        elif self.x + self.size >= res[0]:
            self.x = res[0] - self.size
            self.dx *= -1

        if self.y - self.size <= 0:
            self.y = self.size
            self.dy *= -1

        elif self.y + self.size >= res[1]:
            self.y = res[1] - self.size
            self.dy *= -1

    def move(self):
        keys = pygame.key.get_pressed()

        self.dy *= 0.9
        self.dx *= 0.9

        if keys[pygame.K_w]:
            self.dy -= 2

        if keys[pygame.K_s]:
            self.dy += 2

        if keys[pygame.K_a]:
            self.dx -= 2

        if keys[pygame.K_d]:
            self.dx += 2


    def main(self, surf_for_draw):
        self.draw(surf_for_draw)
        self.update()
        self.move()


Game().run()
