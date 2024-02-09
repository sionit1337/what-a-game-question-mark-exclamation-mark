import pygame

res = (1280, 720)

fps = 60

black = pygame.Color(1, 1, 1)
white = pygame.Color(240, 240, 240)

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

yellow = pygame.Color(255, 255, 0)
magenta = pygame.Color(255, 0, 255)
cyan = pygame.Color(0, 255, 255)


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Test")
        self.clock = pygame.time.Clock()

        self.objects = []


    def run(self):
        running = True

        self.objects.append(Player(res[0] / 2, res[1] / 2, 0, 0, 15, 3, 0.2, 15, red))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            self.screen.fill(black)

            for obj in self.objects:
                obj.main(self.screen)

            self.clock.tick(fps)

            pygame.display.flip()


class Player:
    def __init__(self, x: float, y: float, vx: float, vy: float, size: float, speed: float, friction: float, weight: float, color: pygame.Color):
        super().__init__()

        self.x = x
        self.y = y

        self.vx = vx
        self.vy = vy

        self.speed = speed
        self.friction = friction

        self.size = size
        self.weight = weight

        self.color = color
        self.tag = "#player"


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)


    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.vx *= (1 - self.friction)
        self.vy *= (1 - self.friction)

        if self.x - self.size <= 0:
            self.x = self.size
            self.vx *= -1

        elif self.x + self.size >= res[0]:
            self.x = res[0] - self.size
            self.vx *= -1

        if self.y - self.size <= 0:
            self.y = self.size
            self.vy *= -1

        elif self.y + self.size >= res[1]:
            self.y = res[1] - self.size
            self.vy *= -1


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.apply_force(0, self.speed)

        if keys[pygame.K_s]:
            self.apply_force(0, self.speed * -1)

        if keys[pygame.K_a]:
            self.apply_force(self.speed, 0)

        if keys[pygame.K_d]:
            self.apply_force(self.speed * -1, 0)


    def apply_force(self, vx: float, vy: float):
        self.vx -= vx
        self.vy -= vy


    def main(self, surface):
        self.draw(surface)
        self.update()
        self.move()


Game().run()
