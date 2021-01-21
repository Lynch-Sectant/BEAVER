import random

import pygame
import sqlite3
import sys


def check(x, y, w, h, posx, posy):
    if x <= posx <= w + x and y <= posy <= h + y:
        return True


def load_image(name, colorkey=None):
    fullname = name
    image = pygame.image.load(fullname)
    return image


text_x0, text_y0, text_w0, text_h0 = 0, 0, 0, 0
text_x1, text_y1, text_w1, text_h1 = 0, 0, 0, 0
text_x2, text_y2, text_w2, text_h2 = 0, 0, 0, 0
text_x3, text_y3, text_w3, text_h3 = 0, 0, 0, 0
text_x4, text_y4, text_w4, text_h4 = 0, 0, 0, 0
text_x5, text_y5, text_w5, text_h5 = 0, 0, 0, 0
playing = 0

def start(screen, a):
    fon = pygame.transform.scale(load_image('start.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Player!", True, (255, 255, 100))
    text_x = width // 2 - text.get_width() // (2 * a)
    text_y = height // 1.2 - text.get_height() // (2 * a)
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 100), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 5)

def show_menu(screen, a):
    welcome(screen, 50, 3, 4.3)
    fon = pygame.transform.scale(load_image('playbtn.jpg'), (100 * a, 90 * a))
    screen.blit(fon, (690 * a, 510 * a))

    fon = pygame.transform.scale(load_image('settingsbtn.jpg'), (100 * a, 100 * a))
    screen.blit(fon, (10 * a, 0 * a))

    fon = pygame.transform.scale(load_image('exit.jpg'), (100 * a, 100 * a))
    screen.blit(fon, (10 * a, 500 * a))

    fon = pygame.transform.scale(load_image('info.jpg'), (100 * a, 100 * a))
    screen.blit(fon, (690 * a, 0 * a))


def show_settings(screen, a):
    global text_x0, text_y0, text_w0, text_h0
    global text_x1, text_y1, text_w1, text_h1
    global text_x2, text_y2, text_w2, text_h2
    global text_x3, text_y3, text_w3, text_h3
    global text_x4, text_y4, text_w4, text_h4
    global text_x5, text_y5, text_w5, text_h5
    screen.fill((0, 0, 0))
    fon = pygame.transform.scale(load_image('set.jpg'), (width, height))
    screen.blit(fon, (0 , 0 ))
    font = pygame.font.Font(None, 55 * a)
    text = font.render("SETTINGS", True, (255, 255, 100))
    text_x = width - text.get_width() * 2.6
    text_y = height - text.get_height() * 16
    screen.blit(text, (text_x, text_y))

    font = pygame.font.Font(None, 40 * a)
    text = font.render("800 x 600", True, (255, 255, 100))
    text_x0 = width - text.get_width() * 4
    text_y0 = height - text.get_height() * 14
    screen.blit(text, (text_x0, text_y0))
    text_w0 = text.get_width()
    text_h0 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x0 - 10, text_y0 - 10, text_w0 + 20, text_h0 + 20),
                     5)

    font = pygame.font.Font(None, 40 * a)
    text = font.render("30 FPS", True, (255, 255, 100))
    text_x3 = width - text.get_width() * 3
    text_y3 = height - text.get_height() * 14
    screen.blit(text, (text_x3, text_y3))
    text_w3 = text.get_width()
    text_h3 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x3 - 10, text_y3 - 10, text_w3 + 20, text_h3 + 20),
                     5)

    font = pygame.font.Font(None, 40 * a)
    text = font.render("45 FPS", True, (255, 255, 100))
    text_x5 = width - text.get_width() * 3
    text_y5 = height - text.get_height() * 11
    screen.blit(text, (text_x5, text_y5))
    text_w5 = text.get_width()
    text_h5 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x5 - 10, text_y5 - 10, text_w5 + 20, text_h5 + 20),
                     5)

    font = pygame.font.Font(None, 40 * a)
    text = font.render("1600 x 1200", True, (0, 0, 0))
    text_x1 = width - text.get_width() * 3.25
    text_y1 = height - text.get_height() * 8
    screen.blit(text, (text_x1, text_y1))
    text_w1 = text.get_width()
    text_h1 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x1 - 10, text_y1 - 10, text_w1 + 20, text_h1 + 20),
                     5)

    font = pygame.font.Font(None, 40 * a)
    text = font.render("60 FPS", True, (255, 255, 100))
    text_x2 = width - text.get_width() * 3
    text_y2 = height - text.get_height() * 8
    screen.blit(text, (text_x2, text_y2))
    text_w2 = text.get_width()
    text_h2 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x2 - 10, text_y2 - 10, text_w2 + 20, text_h2 + 20),
                     5)

    fon = pygame.transform.scale(load_image('theme1.png'), (100 * a, 80 * a))
    screen.blit(fon, (100 * a, 170 * a))

    fon = pygame.transform.scale(load_image('theme2.png'), (100 * a, 80 * a))
    screen.blit(fon, (100 * a, 270 * a))

    fon = pygame.transform.scale(load_image('theme3.png'), (100 * a, 80 * a))
    screen.blit(fon, (100 * a, 370 * a))

    fon = pygame.transform.scale(load_image('accept.png'), (120 * a, 80 * a))
    screen.blit(fon, (550 * a, 500 * a))

    fon = pygame.transform.scale(load_image('back.png'), (120 * a, 80 * a))
    screen.blit(fon, (100 * a, 500 * a))


def show_info(screen, a):
    screen.fill((0, 0, 0))
    fon = pygame.transform.scale(load_image('developers.png'), (600 * a, 500 * a))
    screen.blit(fon, (0 * a, 0 * a))
    fon = pygame.transform.scale(load_image('history.jpg'), (150 * a, 150 * a))
    screen.blit(fon, (600 * a, 200 * a))
    fon = pygame.transform.scale(load_image('keys.png'), (150 * a, 150 * a))
    screen.blit(fon, (600 * a, 400 * a))
    fon = pygame.transform.scale(load_image('back.png'), (100 * a, 100 * a))
    screen.blit(fon, (400 * a, 400 * a))
    fon = pygame.transform.scale(load_image('records.png'), (150 * a, 150 * a))
    screen.blit(fon, (600 * a, 10 * a))


def welcome(screen, pp, bb, a):
    screen.fill((0, 0, 0))
    fon = pygame.transform.scale(load_image('beaver.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, pp)
    text = font.render("Welcome to the Beaver's War", True, (255, 255, 100))
    text_x00 = width // 2 - text.get_width() // 2
    text_y00 = height - text.get_height() * a
    text_w00 = text.get_width()
    text_h00 = text.get_height()
    screen.blit(text, (text_x00, text_y00))
    pygame.draw.rect(screen, (255, 255, 100), (text_x00 - 10, text_y00 - 10, text_w00 + 20, text_h00 + 20), bb)


if __name__ == '__main__':
    con = sqlite3.connect('settings.db')
    cur = con.cursor()
    result = cur.execute("""SELECT view FROM sett
                WHERE id = (SELECT MAX(id) 
                FROM sett)""").fetchall()
    result = str(result).split(', ')
    w = int(result[0].replace("[('", ''))
    h = int(result[1].replace("',)]", ''))

    result = cur.execute("""SELECT FPS FROM sett
                    WHERE id = (SELECT MAX(id) 
                    FROM sett)""").fetchall()
    result = str(result)
    fps = result.replace("[(", '')
    fps = int(str(fps).replace(',)]', ''))

    result = cur.execute("""SELECT view FROM sett
                           WHERE id = (SELECT MAX(id) 
                           FROM sett)""").fetchall()
    result = str(result)
    vieww = result.replace("[('", '')
    vieww = str(vieww).replace("',)]", '')

    if w == 800 and h == 600:
        flag = 1
    else:
        flag = 2

    pygame.init()
    size = width, height = w, h
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    result = cur.execute("""SELECT musicc FROM sett
                               WHERE id = (SELECT MAX(id) 
                               FROM sett)""").fetchall()
    music = str(result[0]).replace('(', '')
    music = music.replace(',)', '')
    music = music.strip("'")
    a = pygame.mixer.Sound(music)
    a.play(-1)

    con = sqlite3.connect('Records.db')
    cur = con.cursor()
    result = cur.execute("""SELECT Status, Score FROM Records
                    WHERE Run = (SELECT MIN(Run) 
                    FROM Records)""").fetchall()
    status1 = result[0][0]
    score1 = result[0][1]

    result = cur.execute("""SELECT Status, Score FROM Records
                        WHERE Run = (SELECT MAX(Run) 
                        FROM Records)""").fetchall()
    status2 = result[0][0]
    score2 = result[0][1]

    result = cur.execute("""SELECT Status, Score FROM Records
                        WHERE Score = (SELECT MAX(Score) 
                        FROM Records )AND Status = 'win' """).fetchall()
    status3 = result[0][0]
    score3 = result[0][1]


    def show_records(screen, a):
        global status1, status2, status3
        global score1, score2, score3

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 55 * a)

        text = font.render("First attemp", True, (255, 255, 100))
        text_x = width - text.get_width() * 3.5
        text_y = height - text.get_height() * 13
        screen.blit(text, (text_x, text_y))

        text = font.render("Last attemp", True, (255, 255, 100))
        text_x = width - text.get_width() * 3.55
        text_y = height - text.get_height() * 9
        screen.blit(text, (text_x, text_y))

        text = font.render("Best attemp", True, (255, 255, 100))
        text_x = width - text.get_width() * 3.5
        text_y = height - text.get_height() * 5
        screen.blit(text, (text_x, text_y))

        text = font.render("Status", True, (255, 255, 100))
        text_x = width - text.get_width() * 3.5
        text_y = height - text.get_height() * 16
        screen.blit(text, (text_x, text_y))

        text = font.render("Score", True, (255, 255, 100))
        text_x = width - text.get_width() * 1.5
        text_y = height - text.get_height() * 16
        screen.blit(text, (text_x, text_y))

        text = font.render(("{}").format(status1), True, (255, 255, 100))
        text_x = width - text.get_width() * 6
        text_y = height - text.get_height() * 13.3
        screen.blit(text, (text_x, text_y))

        text = font.render(("{}").format(status2), True, (255, 255, 100))
        text_x = width - text.get_width() * 6
        text_y = height - text.get_height() * 9.3
        screen.blit(text, (text_x, text_y))

        text = font.render(("{}").format(status3), True, (255, 255, 100))
        text_x = width - text.get_width() * 6
        text_y = height - text.get_height() * 5.3
        screen.blit(text, (text_x, text_y))

        text = font.render(("{}").format(score1), True, (255, 255, 100))
        text_x = width - text.get_width() * 1.5
        text_y = height - text.get_height() * 13.3
        screen.blit(text, (text_x, text_y))

        text = font.render(("{}").format(score2), True, (255, 255, 100))
        text_x = width - text.get_width() * 1.5
        text_y = height - text.get_height() * 9.3
        screen.blit(text, (text_x, text_y))

        text = font.render(("{}").format(score3), True, (255, 255, 100))
        text_x = width - text.get_width() * 1.5
        text_y = height - text.get_height() * 5.3
        screen.blit(text, (text_x, text_y))

        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (320 * a, 0), (320 * a, 600 * a), width=5 * a)

        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (580 * a, 0), (580 * a, 600 * a), width=5 * a)

        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (0, 200 * a), (800 * a, 200 * a), width=5 * a)

        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (0, 350 * a), (800 * a, 350 * a), width=5 * a)

    window_show = 0
    pygame.display.flip()
    running = True

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


def methacash(width, height):
    global life_board, METHACASH_ADDED, METHACASH, ENEMY_METHACASH, ENEMY_METHACASH_ADDED, edit_mode, SCORE
    added = 0
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
        added += METHACASH
        SCORE += added
        added = 0


def record(win):
    global SCORE
    con = sqlite3.connect('Records.db')
    cur = con.cursor()
    if win:
        SCORE += 50
        cur.execute(f'''INSERT INTO Records (Status, Score) VALUES ('VICTORY',{SCORE})''')
    else:
        SCORE -= 100
        cur.execute(f'''INSERT INTO Records VALUES ('DEFEAT',{SCORE})''')
    con.commit()

def play():
    size = width, height = (1000, 1000)
screen = pygame.display.set_mode(size)

NEXT_MOVE = pygame.USEREVENT + 1
pygame.time.set_timer(NEXT_MOVE, 100)

while running:
    x, y = event.pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and edit_mode:
            life_board.get_click(event.pos)
        while edit_mode:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_e:
                    CHOSEN_ENTITY = Trooper(life_board, x, y, 3, 5, 5, 1, 8, 'player')
                elif event.type == pygame.K_r:
                    CHOSEN_ENTITY = Sniper(life_board, x, y, 3, 5, 3, 2, 12, 'player')
                elif event.type == pygame.K_w:
                    CHOSEN_ENTITY = GasFighter(life_board, x, y, 7, 3, 7, 3, 12, 'player')
                elif event.type == pygame.K_a:
                    CHOSEN_ENTITY = Farm(life_board, x, y, 10, 'player')
                elif event.type == pygame.K_s:
                    CHOSEN_ENTITY = Attack_Tower(life_board, x, y, 10, 'player')
                elif event.type == pygame.K_i:
                    CHOSEN_ENTITY = Wall(life_board, x, y, 5, 'player')
                elif event.type == pygame.K_KP_ENTER:
                    edit_mode = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos()
                    life_board.get_tile([x, y]) = CHOSEN_ENTITY
            for i in range(height):
                for j in range(width):
                    if life_board.get_tile([j, i]) is None and METHACASH >= 5 and random.randint(0, 100) >= 75:
                        light = random.choise(Trooper(life_board, x, y, 3, 5, 5, 1, 8, 'enemy'), Sniper(life_board, x, y, 3, 5, 3, 2, 12, 'enemy'))
                        life_board.get_tile([x, y]) = light
                    if life_board.get_tile([j, i]) is None and METHACASH >= 20 and random.randint(0, 100) >= 75:
                        heavy = GasFighter(life_board, x, y, 7, 3, 7, 3, 12, 'enemy')
                        life_board.get_tile([x, y]) = heavy

        while not edit_mode:
            methacash(49, 49)
            for i in range(height):
                for j in range(width):
                    if life_board.tiles[j][i].drawn() is Unit:
                        life_board.move(ENEMY_COORDS)
                        life_board.tiles[j][i].pattern()
                    if life_board.tiles[j][i].drawn() is Building:
                        life_board.tiles[j][i].pattern()
                    if life_board.tiles[j][i].drawn() is Projectile:
                        life_board.tiles[j][i].pattern()


    screen.fill((0, 0, 0))
    life_board.render(screen)

    
    while running:
        # Что отрисовываем
        if window_show == 0:
            if flag == 1:
                start(screen, 1)
            else:
                start(screen, 2)
        elif window_show == 1:
            if flag == 1:
                show_menu(screen, 1)
            else:
                show_menu(screen, 2)
        elif window_show == 2:
            if flag == 1:
                show_settings(screen, 1)
            else:
                show_settings(screen, 2)
        elif window_show == 3:
            if flag == 1:
                show_info(screen, 1)
            else:
                show_info(screen, 2)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag == 1:
                    # Проверка кнопок
                    if window_show == 0:
                        window_show = 1

                    elif window_show == 1:
                        if check(10, 0, 100, 100, event.pos[0], event.pos[1]):
                            window_show = 2
                        if check(10, 500, 100, 100, event.pos[0], event.pos[1]):
                            running = False
                        if check(690, 510, 100, 90, event.pos[0], event.pos[1]):
                            playing = 1
                        if check(690, 0, 100, 100, event.pos[0], event.pos[1]):
                            window_show = 3

                    elif window_show == 2:
                        if check(text_x0 - 10, text_y0 - 10, text_w0 + 20, text_h0 + 20, event.pos[0],
                                 event.pos[1]):
                            vieww = '800, 600'
                        elif check(text_x1 - 10, text_y1 - 10, text_w1 + 20, text_h1 + 20, event.pos[0],
                                   event.pos[1]):
                            vieww = '1600, 1200'
                        elif check(text_x3 - 10, text_y3 - 10, text_w3 + 20, text_h3 + 20, event.pos[0],
                                   event.pos[1]):
                            fps = 30
                        elif check(text_x2 - 10, text_y2 - 10, text_w2 + 20, text_h2 + 20, event.pos[0],
                                   event.pos[1]):
                            fps = 60
                        elif check(text_x5 - 10, text_y5 - 10, text_w5 + 20, text_h5 + 20, event.pos[0],
                                   event.pos[1]):
                            fps = 45
                        elif check(100, 170, 100, 80, event.pos[0],
                               event.pos[1]):
                            music = 'Axis_Theme.mp3'
                        elif check(100, 270, 100, 80, event.pos[0],
                               event.pos[1]):
                            music = 'Comintern_Theme.mp3'
                        elif check(100, 370, 100, 80, event.pos[0],
                               event.pos[1]):
                            music = 'Krakow.mp3'
                        elif check(550, 500, 120, 80, event.pos[0],
                                 event.pos[1]):
                            con = sqlite3.connect("settings.db")
                            cur = con.cursor()
                            cur.execute(
                                """INSERT INTO sett(view, FPS, musicc) VALUES('{}', '{}', '{}')""".format(vieww, fps, music))
                            con.commit()
                            window_show = 1
                        elif check(100, 500, 120, 80, event.pos[0], event.pos[1]):
                            window_show = 1

                    elif window_show == 3:

                        if check(600, 400, 150, 150, event.pos[0], event.pos[1]):
                            screen.fill((0, 0, 0))
                            fon = pygame.transform.scale(load_image('keys_text.png'), (800, 600))
                            screen.blit(fon, (0, 0))
                            if check(0, 0, 800, 600, event.pos[0], event.pos[1]):
                                window_show = 4

                        elif check(600, 200, 150, 150, event.pos[0], event.pos[1]):
                            screen.fill((0, 0, 0))
                            fon = pygame.transform.scale(load_image('lor.jpg'), (800, 600))
                            screen.blit(fon, (0, 0))
                            if check(0, 0, 800, 600, event.pos[0], event.pos[1]):
                                window_show = 5

                        elif check(600, 10, 150, 150, event.pos[0], event.pos[1]):
                            show_records(screen, 1)
                            if check(0, 0, 800, 600, event.pos[0], event.pos[1]):
                                window_show = 7

                        elif check(400, 400, 100, 100, event.pos[0], event.pos[1]):
                            window_show = 1

                    elif window_show == 4:
                        window_show = 3

                    elif window_show == 5:
                        window_show = 3

                    elif window_show == 7:
                        window_show = 3

                elif flag == 2:
                    if window_show == 0:
                        window_show = 1

                    elif window_show == 1:
                        if check(10 * 2, 0 * 2, 100 * 2, 100 * 2, event.pos[0], event.pos[1]):
                            window_show = 2
                        if check(10 * 2, 500 * 2, 100 * 2, 100 * 2, event.pos[0], event.pos[1]):
                            running = False
                        if check(690 * 2, 510 * 2, 100 * 2, 90 * 2, event.pos[0], event.pos[1]):
                            print('play')
                        if check(690 * 2, 0 * 2, 100 * 2, 100 * 2, event.pos[0], event.pos[1]):
                            window_show = 3

                    elif window_show == 2:
                        if check(text_x0 - 10, text_y0 - 10, text_w0 + 20, text_h0 + 20, event.pos[0],
                                 event.pos[1]):
                            vieww = '800, 600'
                        elif check(text_x1 - 10, text_y1 - 10, text_w1 + 20, text_h1 + 20, event.pos[0],
                                   event.pos[1]):
                            vieww = '1600, 1200'
                        elif check(text_x3 - 10, text_y3 - 10, text_w3 + 20, text_h3 + 20, event.pos[0],
                                   event.pos[1]):
                            fps = 30
                        elif check(text_x2 - 10, text_y2 - 10, text_w2 + 20, text_h2 + 20, event.pos[0],
                                   event.pos[1]):
                            fps = 60
                        elif check(text_x5 - 10, text_y5 - 10, text_w5 + 20, text_h5 + 20, event.pos[0],
                                   event.pos[1]):
                            fps = 45
                        elif check(100 * 2, 170 * 2, 100 * 2, 80 * 2, event.pos[0],
                               event.pos[1]):
                            music = 'Axis_Theme.mp3'
                        elif check(100 * 2, 270 * 2, 100 * 2, 80 * 2, event.pos[0],
                               event.pos[1]):
                            music = 'Comintern_Theme.mp3'
                        elif check(100 * 2, 370 * 2, 100 * 2, 80 * 2, event.pos[0],
                               event.pos[1]):
                            music = 'Krakow.mp3'
                        elif check(550 * 2, 500 * 2, 120 * 2, 80 * 2, event.pos[0],
                                 event.pos[1]):
                            con = sqlite3.connect("settings.db")
                            cur = con.cursor()
                            cur.execute(
                                """INSERT INTO sett(view, FPS, musicc) VALUES('{}', '{}', '{}')""".format(vieww, fps, music))
                            con.commit()
                            window_show = 1
                        elif check(100 * 2, 500 * 2, 120 * 2, 80 * 2, event.pos[0], event.pos[1]):
                            window_show = 1

                    elif window_show == 3:

                        if check(600 * 2, 400 * 2, 150 * 2, 150 * 2, event.pos[0], event.pos[1]):
                            screen.fill((0, 0, 0))
                            fon = pygame.transform.scale(load_image('keys_text.png'), (800 * 2, 600 * 2))
                            screen.blit(fon, (0 * 2, 0 * 2))
                            if check(0 * 2, 0 * 2, 800 * 2, 600 * 2, event.pos[0], event.pos[1]):
                                window_show = 4

                        elif check(600 * 2, 200 * 2, 150 * 2, 150 * 2, event.pos[0], event.pos[1]):
                            screen.fill((0, 0, 0))
                            fon = pygame.transform.scale(load_image('lor.jpg'), (800 * 2, 600 * 2))
                            screen.blit(fon, (0 * 2, 0 * 2))
                            if check(0 * 2, 0 * 2, 800 * 2, 600 * 2, event.pos[0], event.pos[1]):
                                window_show = 5

                        elif check(600 * 2, 10 * 2, 150 * 2, 150 * 2, event.pos[0], event.pos[1]):
                            show_records(screen, 2)
                            if check(0, 0, 800 * 2, 600 * 2, event.pos[0], event.pos[1]):
                                window_show = 7

                        elif check(600 * 2, 10 * 2, 150 * 2, 150 * 2, event.pos[0], event.pos[1]):
                            print(0)

                        elif check(400 * 2, 400 * 2, 100 * 2, 100 * 2, event.pos[0], event.pos[1]):
                            window_show = 1

                    elif window_show == 7:
                        window_show = 3

                    elif window_show == 4:
                        window_show = 3

                    elif window_show == 5:
                        window_show = 3

               elif playing == 1:
                play()
                
        pygame.display.flip()
pygame.quit()
