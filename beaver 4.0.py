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
    fon = pygame.transform.scale(load_image('start.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Player!", True, (255, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 1.2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 100), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 5)

    window_show = 1
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if flag == 1 and window_show == 1:
                    welcome(screen, 50, 3, 4.3)
                    fon = pygame.transform.scale(load_image('playbtn.jpg'), (100, 90))
                    screen.blit(fon, (690, 510))

                    fon = pygame.transform.scale(load_image('settingsbtn.jpg'), (100, 100))
                    screen.blit(fon, (10, 0))

                    fon = pygame.transform.scale(load_image('exit.jpg'), (100, 100))
                    screen.blit(fon, (10, 500))

                    fon = pygame.transform.scale(load_image('info.jpg'), (100, 100))
                    screen.blit(fon, (690, 0))

                    if check(10, 0, 100, 100, event.pos[0], event.pos[1]):
                        window_show = 2
                        screen.fill((0, 0, 0))
                        fon = pygame.transform.scale(load_image('set.jpg'), (width, height))
                        screen.blit(fon, (0, 0))
                        font = pygame.font.Font(None, 55)
                        text = font.render("SETTINGS", True, (255, 255, 100))
                        text_x = width - text.get_width() * 2.6
                        text_y = height - text.get_height() * 16
                        screen.blit(text, (text_x, text_y))

                        font = pygame.font.Font(None, 40)
                        text = font.render("800 x 600", True, (255, 255, 100))
                        text_x0 = width - text.get_width() * 5
                        text_y0 = height - text.get_height() * 14
                        screen.blit(text, (text_x0, text_y0))
                        text_w0 = text.get_width()
                        text_h0 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x0 - 10, text_y0 - 10, text_w0 + 20, text_h0 + 20),
                                         5)

                        font = pygame.font.Font(None, 40)
                        text = font.render("30 FPS", True, (255, 255, 100))
                        text_x3 = width - text.get_width() * 3
                        text_y3 = height - text.get_height() * 14
                        screen.blit(text, (text_x3, text_y3))
                        text_w3 = text.get_width()
                        text_h3 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x3 - 10, text_y3 - 10, text_w3 + 20, text_h3 + 20),
                                         5)

                        font = pygame.font.Font(None, 40)
                        text = font.render("45 FPS", True, (255, 255, 100))
                        text_x5 = width - text.get_width() * 3
                        text_y5 = height - text.get_height() * 11
                        screen.blit(text, (text_x5, text_y5))
                        text_w5 = text.get_width()
                        text_h5 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x5 - 10, text_y5 - 10, text_w5 + 20, text_h5 + 20),
                                         5)

                        font = pygame.font.Font(None, 40)
                        text = font.render("1600 x 1200", True, (0, 49, 83))
                        text_x1 = width - text.get_width() * 4.05
                        text_y1 = height - text.get_height() * 8
                        screen.blit(text, (text_x1, text_y1))
                        text_w1 = text.get_width()
                        text_h1 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x1 - 10, text_y1 - 10, text_w1 + 20, text_h1 + 20),
                                         5)

                        font = pygame.font.Font(None, 40)
                        text = font.render("60 FPS", True, (255, 255, 100))
                        text_x2 = width - text.get_width() * 3
                        text_y2 = height - text.get_height() * 8
                        screen.blit(text, (text_x2, text_y2))
                        text_w2 = text.get_width()
                        text_h2 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x2 - 10, text_y2 - 10, text_w2 + 20, text_h2 + 20),
                                         5)

                        font = pygame.font.Font(None, 50)
                        text = font.render("ACCEPT", True, (255, 255, 100))
                        text_x4 = width - text.get_width() * 1.5
                        text_y4 = height - text.get_height() * 4
                        screen.blit(text, (text_x4, text_y4))
                        text_w4 = text.get_width()
                        text_h4 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x4 - 10, text_y4 - 10, text_w4 + 20, text_h4 + 20),
                                         5)

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
                    elif check(text_x4 - 10, text_y4 - 10, text_w4 + 20, text_h4 + 20, event.pos[0],
                             event.pos[1]):
                        con = sqlite3.connect("settings.db")
                        cur = con.cursor()
                        cur.execute(
                            """INSERT INTO sett(view, FPS) VALUES('{}', '{}')""".format(vieww, fps))
                        con.commit()
                        window_show = 1


                if check(10, 500, 100, 100, event.pos[0], event.pos[1]) and window_show == 1:
                    running = False

                if check(690, 510, 100, 90, event.pos[0], event.pos[1]) and window_show == 1:
                    print('play')

                if check(690, 0, 100, 100, event.pos[0], event.pos[1]) and window_show == 1:
                    screen.fill((0, 0, 0))
                    font = pygame.font.Font(None, 50)
                    text1 = font.render("Developers:", True, (255, 255, 100))
                    text2 = font.render("Lynch-Sectant,", True, (255, 255, 100))
                    text3 = font.render("Menyanesuschestvuet,", True, (255, 255, 100))
                    text4 = font.render("Lesnichiy.", True, (255, 255, 100))
                    text_xt = width - text.get_width() * 3
                    text_yt = height - text.get_height() * 15
                    screen.blit(text1, (text_xt, text_yt))
                    screen.blit(text2, (text_xt, text_yt * 2))
                    screen.blit(text3, (text_xt, text_yt * 3))
                    screen.blit(text4, (text_xt, text_yt * 4))
                    fon = pygame.transform.scale(load_image('history.jpg'), (150, 150))
                    screen.blit(fon, (600, 200))
                    window_show = 3

                if check(600, 200, 150, 150, event.pos[0], event.pos[1]) and window_show == 3:
                    screen.fill((0, 0, 0))
                    fon = pygame.transform.scale(load_image('lor.jpg'), (800, 600))
                    screen.blit(fon, (0, 0))
                    window_show = 1

                if flag == 2 and window_show == 1:
                    welcome(screen, 70, 5, 5)
                    fon = pygame.transform.scale(load_image('playbtn.jpg'), (150, 140))
                    screen.blit(fon, (1420, 890))

                    fon = pygame.transform.scale(load_image('settingsbtn.jpg'), (150, 150))
                    screen.blit(fon, (50, 200))

                    fon = pygame.transform.scale(load_image('exit.jpg'), (150, 150))
                    screen.blit(fon, (50, 890))

                    fon = pygame.transform.scale(load_image('info.jpg'), (150, 150))
                    screen.blit(fon, (1420, 200))

                    if check(50, 200, 150, 150, event.pos[0], event.pos[1]):
                        window_show = 2
                        screen.fill((0, 0, 0))
                        fon = pygame.transform.scale(load_image('set.jpg'), (width, height))
                        screen.blit(fon, (0, 0))
                        font = pygame.font.Font(None, 70)
                        text = font.render("SETTINGS", True, (255, 255, 100))
                        text_x = width - text.get_width() * 3.9
                        text_y = height - text.get_height() * 21
                        screen.blit(text, (text_x, text_y))

                        font = pygame.font.Font(None, 60)
                        text = font.render("800 x 600", True, (255, 255, 100))
                        text_x0 = width - text.get_width() * 6
                        text_y0 = height - text.get_height() * 20
                        screen.blit(text, (text_x0, text_y0))
                        text_w0 = text.get_width()
                        text_h0 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x0 - 10, text_y0 - 10, text_w0 + 20, text_h0 + 20),
                                         5)

                        font = pygame.font.Font(None, 60)
                        text = font.render("1600 x 1200", True, (0, 0, 0))
                        text_x1 = width - text.get_width() * 4.82
                        text_y1 = height - text.get_height() * 10
                        screen.blit(text, (text_x1, text_y1))
                        text_w1 = text.get_width()
                        text_h1 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x1 - 10, text_y1 - 10, text_w1 + 20, text_h1 + 20),
                                         5)

                        font = pygame.font.Font(None, 60)
                        text = font.render("30 FPS", True, (255, 255, 100))
                        text_x3 = width - text.get_width() * 3
                        text_y3 = height - text.get_height() * 20
                        screen.blit(text, (text_x3, text_y3))
                        text_w3 = text.get_width()
                        text_h3 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x3 - 10, text_y3 - 10, text_w3 + 20, text_h3 + 20),
                                         5)

                        font = pygame.font.Font(None, 60)
                        text = font.render("45 FPS", True, (255, 255, 100))
                        text_x5 = width - text.get_width() * 3
                        text_y5 = height - text.get_height() * 15
                        screen.blit(text, (text_x5, text_y5))
                        text_w5 = text.get_width()
                        text_h5 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x5 - 10, text_y5 - 10, text_w5 + 20, text_h5 + 20),
                                         5)

                        font = pygame.font.Font(None, 60)
                        text = font.render("60 FPS", True, (255, 255, 100))
                        text_x2 = width - text.get_width() * 3
                        text_y2 = height - text.get_height() * 10
                        screen.blit(text, (text_x2, text_y2))
                        text_w2 = text.get_width()
                        text_h2 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x2 - 10, text_y2 - 10, text_w2 + 20, text_h2 + 20),
                                         5)

                        font = pygame.font.Font(None, 70)
                        text = font.render("ACCEPT", True, (255, 255, 100))
                        text_x4 = width - text.get_width() * 2
                        text_y4 = height - text.get_height() * 6
                        screen.blit(text, (text_x4, text_y4))
                        text_w4 = text.get_width()
                        text_h4 = text.get_height()
                        pygame.draw.rect(screen, (255, 0, 0), (text_x4 - 10, text_y4 - 10, text_w4 + 20, text_h4 + 20),
                                         5)

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

                    elif check(text_x4 - 10, text_y4 - 10, text_w4 + 20, text_h4 + 20, event.pos[0],
                         event.pos[1]):
                        con = sqlite3.connect("settings.db")
                        cur = con.cursor()
                        cur.execute(
                        """INSERT INTO sett(view, FPS) VALUES('{}', '{}')""".format(vieww, fps))
                        con.commit()
                        window_show = 1

                if check(50, 890, 150, 150, event.pos[0], event.pos[1]) and window_show == 1:
                    running = False

                if check(1420, 890, 150, 140, event.pos[0], event.pos[1]) and window_show == 1:
                    print('play')

                if check(1420, 200, 150, 150, event.pos[0], event.pos[1]) and window_show == 1:
                    screen.fill((0, 0, 0))
                    font = pygame.font.Font(None, 70)
                    text1 = font.render("Developers:", True, (255, 255, 100))
                    text2 = font.render("Lynch-Sectant,", True, (255, 255, 100))
                    text3 = font.render("Menyanesuschestvuet,", True, (255, 255, 100))
                    text4 = font.render("Lesnichiy.", True, (255, 255, 100))
                    text_xt = width - text.get_width() * 6
                    text_yt = height - text.get_height() * 28
                    screen.blit(text1, (text_xt, text_yt))
                    screen.blit(text2, (text_xt, text_yt * 2))
                    screen.blit(text3, (text_xt, text_yt * 3))
                    screen.blit(text4, (text_xt, text_yt * 4))
                    fon = pygame.transform.scale(load_image('history.jpg'), (250, 250))
                    screen.blit(fon, (1000, 400))
                    window_show = 3

                if check(1000, 400, 250, 250, event.pos[0], event.pos[1]) and window_show == 3:
                    screen.fill((0, 0, 0))
                    fon = pygame.transform.scale(load_image('lor.jpg'), (1600, 1200))
                    screen.blit(fon, (0, 50))
                    window_show = 1

        pygame.display.flip()
pygame.quit()
