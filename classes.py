import random

import pygame
import sqlite3

PAUSE = True
CHOSEN_ENTITY = None
all_sprites = pygame.sprite.Group()
PLAYER_UNITS = pygame.sprite.Group()
ENEMY_UNITS = pygame.sprite.Group()
PLAYER_BUILDINGS = pygame.sprite.Group()
ENEMY_BUILDINGS = pygame.sprite.Group()
PROJECTILES = pygame.sprite.Group()
ADDED = 0
METHACASH = 0
METHACASH_ADDED = 10
ENEMY_METHACASH = 50
ENEMY_METHACASH_ADDED = 0
PLAYER_COLOR = 1
ENEMY_COLOR = 2
SCORE = 0
running = True
edit_mode = True
CHOSEN_ENTITY = None


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
    def __init__(self, sheet, x, y, board, team, rows=1, columns=1):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.set_pos(board, x, y)
        self.board = board
        self.team = team

    def set_pos(self, board, x, y):
        self.coords = x, y
        self.rect.x = board.left + (x - 1) * board.tile_size
        self.rect.y = board.top + (y - 1) * board.tile_size

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))


class Building(Entity):
    def __init__(self, sheet, x, y, board, team, hp):
        super().__init__(sheet, x, y, board, team)
        self.hp = hp
        if self.team == 'player':
            PLAYER_BUILDINGS.add(self)
        else:
            ENEMY_BUILDINGS.add(self)

    def pattern(self):
        if self.team == 'enemy' and len(pygame.sprite.spritecollide(self, Projectile)) > 0:
            for k in pygame.sprite.spritecollide(self, Projectile):
                if k.team == 'player':
                    self.hp -= 1
                    if self.hp <= 0:
                        self.kill()
                        return None
        elif self.team == 'player' and len(pygame.sprite.spritecollide(self, Projectile)) > 0:
            for k in pygame.sprite.spritecollide(self, Projectile):
                if k.team == 'enemy':
                    self.hp -= 1
                    if self.hp <= 0:
                        self.kill()
                        return None


class Unit(Entity):
    def __init__(self, sheet, x, y, board, price, speed, hp, dmg, vision_radius, team):
        super().__init__(sheet, x, y, board, team)
        self.price = price
        self.speed = speed
        self.hp = hp
        self.dmg = dmg
        self.vision_radius = vision_radius
        self.destination = self.coords
        self.target = None
        if self.team == 'player':
            PLAYER_UNITS.add(self)
        else:
            ENEMY_UNITS.add(self)

    def move_on_vector(self, move_vector):
        self.board.tiles[self.coords[1]][self.coords[1]].drawn = None
        move_vector = move_vector[0] + self.coords[0], move_vector[1] + self.coords[1]
        self.set_pos(self.board, *move_vector)

    def pattern(self, near):
        if near[1] < 0:
            for h in range(near[1], 0, -1):
                if near[0] < 0:
                    for w in range(near[0], 0, -1):
                        if self.can_go_to((self.coords[0] + w, self.coords[1] + h)):
                            self.move_on_vector(w, h)
                            return None
                else:
                    for w in range(near[0], 0, -1):
                        if self.can_go_to((self.coords[0] + w, self.coords[1] + h)):
                            self.move_on_vector(w, h)
                            return None
        else:
            for h in range(near[1]):
                if near[0] < 0:
                    for w in range(near[0], 0, -1):
                        if self.can_go_to((self.coords[0] + w, self.coords[1] + h)):
                            self.move_on_vector(w, h)
                            return None
                else:
                    for w in range(near[0], 0, -1):
                        if self.can_go_to((self.coords[0] + w, self.coords[1] + h)):
                            self.move_on_vector(w, h)
                            return None
        self.second_pattern()

    def second_pattern(self):
        if self.team == 'enemy' and len(pygame.sprite.spritecollide(self, Projectile)) > 0:
            for k in pygame.sprite.spritecollide(self, Projectile):
                if k.team == 'player':
                    self.hp -= 1
                    if self.hp <= 0:
                        self.kill()
                        return None
        elif self.team == 'player' and len(pygame.sprite.spritecollide(self, Projectile)) > 0:
            for k in pygame.sprite.spritecollide(self, Projectile):
                if k.team == 'enemy':
                    self.hp -= 1
                    if self.hp <= 0:
                        self.kill()
                        return None

    def attack(self, enemy):
        pass

    def can_go_to(self, coords):
        for h in range(self.coords[0], self.coords[0] + coords[0]):
            for w in range(self.coords[1], self.coords[1] + coords[1]):
                if self.board.tiles[h][w].drawn is not None:
                    if self.board.tiles[h][w].drawn.team != self.team:
                        return False

    def move(self, move_coords):
        if self.target == None:
            self.destination = move_coords
        else:
            self.destination = self.target.coords
        if self.destination[0] != self.coords[0] or self.destination != self.coords[1]:
            vector = self.destination[0] - self.coords[0], self.destination[1] - self.coords[1]
            if vector[0] != 0:
                x = vector[0] // abs(vector[0])
            else:
                x = 0
            if vector[1] != 0:
                y = vector[1] // abs(vector[1])
            else:
                y = 0
            near = [vector[0] % self.speed, vector[1] % self.speed]
            for r in near:
                if r == 0 and near.index(r) == 0:
                    near[near.index(r)] = self.speed * x
                elif r == 0:
                    near[1] = self.speed * y
            if self.can_go_to(near):
                self.move_on_vector(tuple(near))
            else:
                self.pattern(near)


class Trooper(Unit):
    def second_pattern(self):
        super().second_pattern()
        minim = (self.vision_radius + 1, None)
        for i in range(-self.vision_radius, self.vision_radius):
            for j in range(-self.vision_radius, self.vision_radius):
                if self.board.tiles[i][j].drawn is not None:
                    if ENEMY_UNITS in self.board.tiles[i][j].drawn.groups() or ENEMY_BUILDINGS in self.board.tiles[i][
                        j].drawn.groups() and self.team == 'player':
                        if ((i + j) / 2 + 0.5) // 1 == 1:
                            self.target = self.board.tiles[i][j].drawn
                            self.attack(self.target)
                            return None
                        elif ((i + j) / 2 + 0.5) // 1 < minim[0]:
                            minim = (((i + j) / 2 + 0.5) // 1 == 1, self.board.tiles[i][j].drawn)
        self.target = minim[1]
        self.move(minim[1].coords)

    def attack(self, enemy):
        if enemy is None:
            return None
        else:
            enemy.hp -= self.dmg
            if enemy.hp <= 0:
                self.target == None


class Sniper(Unit):
    def second_pattern(self):
        super().second_pattern()
        minim = (self.vision_radius + 1, None)
        for i in range(-self.vision_radius, self.vision_radius):
            for j in range(-self.vision_radius, self.vision_radius):
                if self.board.tiles[i][j].drawn is not None:
                    if ENEMY_UNITS in self.board.tiles[i][j].drawn.groups() or ENEMY_BUILDINGS in self.board.tiles[i][
                        j].drawn.groups() and self.team == 'player':
                        if ((i + j) / 2 + 0.5) // 1 == 1:
                            self.move(self.coords[0] - i, self.coords[1] - j)
                            self.target = self.board.tiles[i][j].drawn
                            self.attack(self.target)
                            return None
                        elif ((i + j) / 2 + 0.5) // 1 < minim[0]:
                            minim = (((i + j) / 2 + 0.5) // 1 == 1, self.board.tiles[i][j].drawn)
        self.target = minim[1]
        self.move(minim[1].coords)

    def move(self, move_coords):
        self.destination = move_coords
        if self.destination[0] != self.coords[0] or self.destination != self.coords[1]:
            vector = self.destination[0] - self.coords[0], self.destination[1] - self.coords[1]
            if vector[0] != 0:
                x = vector[0] // abs(vector[0])
            else:
                x = 0
            if vector[1] != 0:
                y = vector[1] // abs(vector[1])
            else:
                y = 0
            near = [vector[0] % self.speed, vector[1] % self.speed]
            for r in near:
                if r == 0 and near.index(r) == 0:
                    near[near.index(r)] = self.speed * x
                elif r == 0:
                    near[1] = self.speed * y
            if self.can_go_to(near):
                self.move_on_vector(tuple(near))
            else:
                self.pattern(near)

    def attack(self, target):
        bullet = Bullet("bullet.png", 0, 0, self.board, self.team,
                        (self.coords[0] - target.coords[0]) * self.board.tile_size,
                        (self.coords[1] - target.coords[1]) * self.board.tile_size,
                        (self.rect.x * self.board.tile_size + self.board.left,
                         self.rect.y * self.board.tile_size + self.board.top))
        bullet.move()
        bullet.kill()


class GasFighter(Unit):
    def second_pattern(self):
        super().second_pattern()
        minim = (self.vision_radius + 1, None)
        for i in range(-self.vision_radius, self.vision_radius):
            for j in range(-self.vision_radius, self.vision_radius):
                if self.board.tiles[i][j].drawn is not None:
                    if ENEMY_UNITS in self.board.tiles[i][j].drawn.groups() or ENEMY_BUILDINGS in self.board.tiles[i][
                        j].drawn.groups() and self.team == 'player':
                        if ((i + j) / 2 + 0.5) // 1 == 1:
                            self.target = self.board.tiles[i][j].drawn
                            self.attack(self.board.tiles[i][j].drawn)
                            return None
                        elif ((i + j) / 2 + 0.5) // 1 < minim[0]:
                            minim = (((i + j) / 2 + 0.5) // 1 == 1, self.board.tiles[i][j].drawn)
        self.target = minim[1]
        self.move(minim[1].coords)

    def attack(self, target):
        bullet = Cloud("gas.jpeg", 0, 0, self.board, self.team,
                       (self.coords[0] - self.target.coords[0]) * self.board.tile_size,
                       (self.coords[1] - self.target.coords[1]) * self.board.tile_size, (self.rect.x, self.rect.y))
        bullet.move()


class Main_Tower(Building):
    def pattern(self):
        super().pattern()
        global METHACASH
        METHACASH += METHACASH_ADDED


class Defense_Tower(Building):
    def __init__(self, sheet, x, y, board, team, hp):
        super().__init__(sheet, x, y, board, team)
        self.hp = hp
        if self.team == 'player':
            PLAYER_BUILDINGS.add(self)
        else:
            ENEMY_BUILDINGS.add(self)
        self.target = None

    def pattern(self, v_radius):
        super().pattern()
        lens = {}
        if self.target is None:
            for h in range(-v_radius, v_radius):
                for w in range(-v_radius, v_radius):
                    lens[self.board.tiles[self.coords[1] + h][self.coords[0] + w].drawn] = ((w + h) / 2 + 0.5) // 1
        elif not self.target.is_alive():
            for h in range(-v_radius, v_radius):
                for w in range(-v_radius, v_radius):
                    lens[self.board.tiles[self.coords[1] + h][self.coords[0] + w].drawn] = ((w + h) / 2 + 0.5) // 1
        for k in lens.keys():
            if lens[k] == min(lens.values()):
                self.target = k
                self.attack()
                return None

    def attack(self):
        bullet = Bullet("bullet.png", 0, 0, self.board, self.team,
                        (self.coords[0] - self.target.coords[0]) * self.board.tile_size,
                        (self.coords[1] - self.target.coords[1]) * self.board.tile_size, (self.rect.x, self.rect.y))
        bullet.move()
        bullet.kill()


# all code from here
class Wall(Building):
    def __init__(self, sheet, x, y, board, team, hp):
        super().__init__(sheet, x, y, board, team, hp)
        self.checked = False
        self.pattern()

    def pattern(self):
        super.pattern()
        for h in range(-1, 2):
            for w in range(-1, 2):
                if self.board.tiles[self.coords[0] + h][self.coords[1] + w].drawn.__class__ == Wall:
                    if self.board.tiles[self.coords[0] + h][self.coords[1] + w].drawn.checked is False:
                        self.hp += ADDED
                        if h != 0 and w != 0:
                            self.board.tiles[self.coords[0] + w][self.coords[1] + h].drawn.pattern()
                        self.board.tiles[self.coords[0] + h][self.coords[1] + w].drawn.checked = True


# to here needs testing!

class Farm(Building):
    def pattern(self):
        global METHACASH
        METHACASH += METHACASH_ADDED // 2


class Projectile(Entity):
    def __init__(self, sheet, x, y, board, team, vx, vy, st_coords):
        super().__init__(self, sheet, x, y, board, team)
        self.vx = vx
        self.vy = vy
        self.coords = st_coords
        PROJECTILES.add(self)

    def move(self):
        for i in range(4):
            self.coords = self.coords[0] + self.vx // 4, self.coords[1] + self.vy // 4
            self.set_pos(self.coords[1], self.coords[0])
            pygame.display.flip()

    def pattern(self):
        pass


class Bullet(Projectile):
    def __init__(self, sheet, columns, rows, x, y, board, team, vx, vy, st_coords, piercing=0):
        super.__init__(sheet, columns, rows, x, y, board, team, vx, vy, st_coords)
        self.piercing = piercing

    def pattern(self):
        if self.team == 'player' and len(pygame.sprite.spritecollide(self, ENEMY_UNITS)) > 0:
            ENEMY_UNITS.second_pattern()
            if self.piercing == 0:
                self.kill()
            else:
                self.piercing -= 1
        elif self.team == 'enemy' and len(pygame.sprite.spritecollide(self, PLAYER_UNITS)) > 0:
            PLAYER_UNITS.second_pattern()
            if self.piercing == 0:
                self.kill()
            else:
                self.piercing -= 1
        if pygame.sprite.spritecollideany(self, ENEMY_BUILDINGS) or pygame.sprite.spritecollideany(self,
                                                                                                   ENEMY_BUILDINGS):
            self.kill()


class Cloud(Projectile):
    def pattern(self):
        if pygame.sprite.spritecollideany(self, ENEMY_BUILDINGS) or pygame.sprite.spritecollideany(self,
                                                                                                   ENEMY_BUILDINGS):
            self.kill()
        elif self.team == 'player' and len(pygame.sprite.spritecollide(self, ENEMY_UNITS)) > 0:
            ENEMY_UNITS.second_pattern()
        elif self.team == 'enemy' and len(pygame.sprite.spritecollide(self, PLAYER_UNITS)) > 0:
            PLAYER_UNITS.second_pattern()


life_board = Board(49, 49)


def methacash(width, height, color):
    global life_board, METHACASH_ADDED, METHACASH, ENEMY_METHACASH, ENEMY_METHACASH_ADDED, edit_mode, SCORE
    pygame.time.wait(20000)
    for i in range(height):
        for j in (width):
            if life_board.get_tile(j, i) is Building():
                if Building.get_color == PLAYER_COLOR:
                    if life_board.get_tile(j, i) is Farm():
                        life_board.get_tile(j, i).pattern()
                    elif life_board.get_tile(j, i) is Main_Tower():
                        life_board.get_tile(j, i).pattern()
                elif Building.get_color == ENEMY_COLOR:
                    if life_board.get_tile(j, i) is Farm():
                        life_board.get_tile(j, i).pattern()
                    elif life_board.get_tile(j, i) is Main_Tower():
                        life_board.get_tile(j, i).pattern()
        edit_mode = True
        METHACASH += METHACASH_ADDED
        ENEMY_METHACASH += ENEMY_METHACASH_ADDED
        SCORE += METHACASH_ADDED
        METHACASH_ADDED = 0


def record(win):
    global SCORE
    con = sqlite3.connect('Records.db')
    cur = con.cursor()
    if win:
        cur.execute(f'''INSERT INTO Records (Status, Score) VALUES ('VICTORY',{SCORE})''')
    else:
        cur.execute(f'''INSERT INTO Records VALUES ('DEFEAT',{SCORE})''')
    con.commit()


pygame.init()

size = width, height = (1000, 1000)
screen = pygame.display.set_mode(size)

NEXT_MOVE = pygame.USEREVENT + 1
pygame.time.set_timer(NEXT_MOVE, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and edit_mode:
            life_board.get_click(event.pos)
        while edit_mode:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_e:
                    CHOSEN_ENTITY = Trooper()
                elif event.type == pygame.K_r:
                    CHOSEN_ENTITY = Sniper()
                elif event.type == pygame.K_w:
                    CHOSEN_ENTITY = Gasfighter()
                elif event.type == pygame.K_a:
                    CHOSEN_ENTITY = Farm()
                elif event.type == pygame.K_s:
                    CHOSEN_ENTITY = Attack_Tower()
                elif event.type == pygame.K_i:
                    CHOSEN_ENTITY = Wall()
                elif event.type == pygame.K_KP_ENTER:
                    edit_mode = False
                if event.type == pygame.MOUSEBUTTONUP:
                    CHOSEN_ENTITY.spawn(event.pos, PLAYER_COLOR)
            for i in range(height):
                for j in range(width):
                    if life_board.get_tile([j, i]) is None and METHACASH >= 5 and random.randint(0, 100) >= 75:
                        random.choise(Warrior(), Archer()).spawn(i, j, ENEMY_COLOR)
                    if life_board.get_tile([j, i]) is None and METHACASH >= 20 and random.randint(0, 100) >= 75:
                        Gasfighter().spawn([i, j], ENEMY_COLOR)

        while not edit_mode:
            for i in range(height):
                for j in range(width):
                    if life_board.tiles[j][i].drawn() is Unit():
                        life_board.move(ENEMY_COORDS)
                        life_board.tiles[j][i].pattern()
                    if life_board.tiles[j][i].drawn() is Building():
                        life_board.tiles[j][i].pattern()
                    if life_board.tiles[j][i].drawn() is Projectile():
                        life_board.tiles[j][i].pattern()


    screen.fill((0, 0, 0))
    life_board.render(screen)
    pygame.display.flip()

pygame.quit()
