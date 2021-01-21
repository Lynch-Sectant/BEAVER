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
    screen.blit(fon, (0 * a, 0 * a))
    font = pygame.font.Font(None, 55)
    text = font.render("SETTINGS", True, (255, 255, 100))
    text_x = width - text.get_width() * 2.6  * a
    text_y = height - text.get_height() * 16  * a
    screen.blit(text, (text_x, text_y))

    font = pygame.font.Font(None, 40)
    text = font.render("800 x 600", True, (255, 255, 100))
    text_x0 = width - text.get_width() * 4 * a
    text_y0 = height - text.get_height() * 14 * a
    screen.blit(text, (text_x0, text_y0))
    text_w0 = text.get_width()
    text_h0 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x0 - 10, text_y0 - 10, text_w0 + 20, text_h0 + 20),
                     5)

    font = pygame.font.Font(None, 40)
    text = font.render("30 FPS", True, (255, 255, 100))
    text_x3 = width - text.get_width() * 3 * a
    text_y3 = height - text.get_height() * 14 * a
    screen.blit(text, (text_x3, text_y3))
    text_w3 = text.get_width()
    text_h3 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x3 - 10, text_y3 - 10, text_w3 + 20, text_h3 + 20),
                     5)

    font = pygame.font.Font(None, 40)
    text = font.render("45 FPS", True, (255, 255, 100))
    text_x5 = width - text.get_width() * 3 * a
    text_y5 = height - text.get_height() * 11 * a
    screen.blit(text, (text_x5, text_y5))
    text_w5 = text.get_width()
    text_h5 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x5 - 10, text_y5 - 10, text_w5 + 20, text_h5 + 20),
                     5)

    font = pygame.font.Font(None, 40)
    text = font.render("1600 x 1200", True, (0, 0, 0))
    text_x1 = width - text.get_width() * 3.25 * a
    text_y1 = height - text.get_height() * 8 * a
    screen.blit(text, (text_x1, text_y1))
    text_w1 = text.get_width()
    text_h1 = text.get_height()
    pygame.draw.rect(screen, (255, 0, 0), (text_x1 - 10, text_y1 - 10, text_w1 + 20, text_h1 + 20),
                     5)

    font = pygame.font.Font(None, 40)
    text = font.render("60 FPS", True, (255, 255, 100))
    text_x2 = width - text.get_width() * 3 * a
    text_y2 = height - text.get_height() * 8 * a
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
    bool1 = True
    bool2 = True
    window_show = 0
    pygame.display.flip()
    running = True

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
                            print('play')
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

                        elif check(400, 400, 100, 100, event.pos[0], event.pos[1]):
                            window_show = 1

                    elif window_show == 4:
                        window_show = 3

                    elif window_show == 5:
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

                        elif check(400 * 2, 400 * 2, 100 * 2, 100 * 2, event.pos[0], event.pos[1]):
                            window_show = 1

                    elif window_show == 4:
                        window_show = 3

                    elif window_show == 5:
                        window_show = 3

        pygame.display.flip()
pygame.quit()