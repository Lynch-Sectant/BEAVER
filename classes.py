import pygame


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


class Worker(Unit):
    pass


class Supporter(Unit):
    pass


class Warrior(Unit):
    pass
