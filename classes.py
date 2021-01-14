import pygame

PAUSE = True
CHOSEN_ENTITY = None
all_sprites = pygame.sprite.Group()
PLAYER_UNITS = pygame.sprite.Group()
ENEMY_UNITS = pygame.sprite.Group()
ADDED = 0
METHACASH = 0
METHACASH_ADDED = 0


class Tile:
    def __init__(self):
        self.color = pygame.Color('black')
        self.drawn = None


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
        all_sprites.draw(screen)

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


class Entity(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, board, team):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.set_pos(board, x, y)
        self.board = board
        if team == 'player':
            PLAYER_UNITS.add(self)
        else:
            ENEMY_UNITS.add(self)
            # add sprite into group

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
    def __init__(self, sheet, columns, rows, x, y, board, team, hp):
        super().__init__(sheet, columns, rows, x, y, board, team)
        self.hp = hp

    def pattern(self):
        pass


class Unit(Entity):
    def __init__(self, sheet, columns, rows, x, y, board, price, speed, hp, dmg, vision_radius, team):
        super().__init__(sheet, columns, rows, x, y, board, team)
        self.price = price
        self.speed = speed
        self.hp = hp
        self.dmg = dmg
        self.vision_radius = vision_radius

    def move(self, move_vector):
        self.board.tiles[self.coords[1]][self.coords[1]].drawn = None
        move_vector = move_vector[0] + self.coords[0], move_vector[1] + self.coords[1]
        self.set_pos(self.board, *move_vector)

    def pattern(self):
        pass

    def second_pattern(self):
        pass

    def attack(self):
        pass


class Warrior(Unit):
    def move(self, move_coords):
        self.direction = move_coords[0] - self.coords[0], move_coords[1] - self.coords[1]
        super().move((move_coords[0] // self.speed, move_coords[1] // self.speed))


class Archer(Unit):
    def move(self, move_coords):
        self.direction = move_coords[0] - self.coords[0], move_coords[1] - self.coords[1]
        super().move((move_coords[0] // self.speed, move_coords[1] // self.speed))


class GasFighter(Unit):
    def move(self, move_coords):
        self.direction = move_coords[0] - self.coords[0], move_coords[1] - self.coords[1]
        super().move((move_coords[0] // self.speed, move_coords[1] // self.speed))


class Main_Tower(Building):
    def pattern(self):
        METHACASH += METHACASH_ADDED


class Defense_Tower(Building):
    pass


# all code from here
class Wall(Building):
    def __init__(self, sheet, columns, rows, x, y, board, team, hp):
        super().__init__(sheet, columns, rows, x, y, board, team, hp)
        self.checked = False
        self.pattern()

    def pattern(self):
        for h in range(-1, 2):
            for w in range(-1, 2):
                if self.board.tiles[self.coords[0] + h][self.coords[1] + w].drawn.__class__ == Wall:
                    if self.board.tiles[self.coords[0] + h][self.coords[1] + w].drawn.checked is False:
                        self.hp += ADDED
                        self.board.tiles[self.coords[0] + w][self.coords[1] + h].drawn.checked = True
                    self.board.tiles[self.coords[0] + w][self.coords[1] + h].drawn.pattern


# to here needs testing!

class Farm(Building):
    def pattern(self):
        METHACASH += METHACASH_ADDED // 2


class Projectile(Entity):
    def __init__(self, sheet, columns, rows, x, y, board, team, vx, vy, st_coords):
        super().__init__(self, sheet, columns, rows, x, y, board, team)
        self.vx = vx
        self.vy = vy
        self.coords = st_coords

    def move(self):
        self.coords = self.coords[0] + self.vx, self.coords[1] + self.vy

    def pattern(self):
        pass


class Arrow(Projectile):
    def __init__(self, sheet, columns, rows, x, y, board, team, vx, vy, st_coords, piercing=0):
        super.__init__(sheet, columns, rows, x, y, board, team, vx, vy, st_coords)
        self.piercing = piercing

    def pattern(self):
        pass


class Cloud(Projectile):
    def pattern(self):
        pass
