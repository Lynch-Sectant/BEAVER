import pygame

PAUSE = True
CHOSEN_ENTITY = None
all_sprites = pygame.sprite.Group()
player_units = pygame.sprite.Group()
enemy_units = pygame.sprite.Group()


class Tile:
    def __init__(self):
        self.color = pygame.Color('black')
        self.drawn = None
        self.is_alive_next_move = False


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tile() for _ in range(width)] for _ in range(height)]
        self.left = 10
        self.top = 10
        self.tile_size = 20

    def set_position(self, left, top, tile_size):
        self.left = left
        self.top = top
        self.tile_size = tile_size

    def render(self, screen):
        for h in range(self.top, self.top + self.height * self.tile_size, self.tile_size):
            for w in range(self.left, self.left + self.width * self.tile_size, self.tile_size):
                pygame.draw.rect(screen, pygame.Color('white'), (w, h, self.tile_size, self.tile_size))
                a = (h - self.top) // self.tile_size
                b = (w - self.left) // self.tile_size
                pygame.draw.rect(screen, self.tiles[a][b].color, (w + 1, h + 1, self.tile_size - 2, self.tile_size - 2))

    def get_tile(self, mouse_pos):
        if mouse_pos[0] > self.left + self.tile_size * self.width:
            return None
        elif mouse_pos[1] > self.top + self.tile_size * self.height:
            return None
        elif mouse_pos[0] < self.left or mouse_pos[1] < self.top:
            return None
        else:
            ans = (mouse_pos[0] - self.left) // self.tile_size, (mouse_pos[0] - self.top) // self.tile_size
            return (ans)

    def on_click(self, mouse_pos):
        if mouse_pos is not None and PAUSE is True:
            self.tiles[mouse_pos[0]][mouse_pos[1]].drawn = CHOSEN_ENTITY

    def get_click(self, mouse_pos):
        c = self.get_tile(mouse_pos)
        self.on_click(c)

    def next_move(self):
        for h in range(self.height):
            for w in range(self.width):
                self.tiles[h][w].is_alive_next_move = self.tiles[h][w].drawn.check_move()
        for h in range(self.height):
            for w in range(self.width):
                if not self.tiles[h][w].is_alive_next_move:
                    self.tiles[h][w].drawn = None


class Entity(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, board):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.set_pos(board, x, y)

    def set_pos(self, board, x, y):
        self.coords = x, y
        self.rect.x = board.left + x * board.tile_size
        self.rect.y = board.top + y * board.tile_size

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


class Building(Entity):
    pass


class Unit(Entity):
    pass


class Attacker(Unit):
    pass


class Supporter(Unit):
    pass


class Shooter(Unit):
    pass


class Base(Building):
    pass


class Defense_Tower(Building):
    pass


class Wall(Building):
    pass


class Farm(Building):
    pass
