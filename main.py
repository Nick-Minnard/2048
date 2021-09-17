import pygame
import random
import os

pygame.init()

win = pygame.display.set_mode((450, 450))
pygame.display.set_caption("2048")


my_font = pygame.font.SysFont("arial", 25)

current_path = os.path.dirname(__file__)

start_image = pygame.image.load(os.path.join(current_path, 'images/start_image.png'))
end_image = pygame.image.load(os.path.join(current_path, 'images/end_image.png'))
tiles = [pygame.image.load(os.path.join(current_path, 'images/2.png')), pygame.image.load(os.path.join(current_path, 'images/4.png')),
         pygame.image.load(os.path.join(current_path, 'images/8.png')), pygame.image.load(os.path.join(current_path, 'images/16.png')),
         pygame.image.load(os.path.join(current_path, 'images/32.png')), pygame.image.load(os.path.join(current_path, 'images/64.png')),
         pygame.image.load(os.path.join(current_path, 'images/128.png')), pygame.image.load(os.path.join(current_path, 'images/256.png')),
         pygame.image.load(os.path.join(current_path, 'images/512.png')), pygame.image.load(os.path.join(current_path, 'images/1024.png')),
         pygame.image.load(os.path.join(current_path, 'images/2048.png')), pygame.image.load(os.path.join(current_path, 'images/4096.png')),
         pygame.image.load(os.path.join(current_path, 'images/8192.png')), pygame.image.load(os.path.join(current_path, 'images/16384.png')),
         pygame.image.load(os.path.join(current_path, 'images/32768.png')), pygame.image.load(os.path.join(current_path, 'images/65536.png'))]

grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]


def draw_board():
    pygame.draw.rect(win, (116, 194, 169), (0, 0, 450, 450))
    pygame.draw.rect(win, (220, 220, 220), (25, 25, 400, 400))

def draw_tiles():
    for idx, val in enumerate(grid):
        if -1 < idx < 4: x, y = idx * 100, 0
        elif 3 < idx < 8: x, y = (idx - 4) * 100, 100
        elif 7 < idx < 12: x, y = (idx - 8) * 100, 200
        else: x, y = (idx - 12) * 100, 300

        if val != 0: win.blit(tiles[nums.index(val)], (x + 25, y + 25))

def add_number():
    options = []
    for idx, val in enumerate(grid):
        if val == 0:
            options.append(idx)
    if len(options) > 0:
        spot = random.choice(options)
        r = random.choice([2, 4])
        grid.pop(spot)
        grid.insert(spot, r)


def rotate(direction):
    global grid
    new_grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if direction == "right": grid_order = [3, 7, 11, 15, 2, 6, 10, 14, 1, 5, 9, 13, 0, 4, 8, 12]
    else: grid_order = [12, 8, 4, 0, 13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3]
    for i in range(16): new_grid[i] = grid[grid_order[i]]
    grid = new_grid


def slide_up(col):
    if grid[col[2]] == 0:
        grid[col[2]] = grid[col[3]]
        grid[col[3]] = 0
    if grid[col[1]] == 0:
        grid[col[1]] = grid[col[2]]
        grid[col[2]] = grid[col[3]]
        grid[col[3]] = 0
    if grid[col[0]] == 0:
        grid[col[0]] = grid[col[1]]
        grid[col[1]] = grid[col[2]]
        grid[col[2]] = grid[col[3]]
        grid[col[3]] = 0


def combine_up(col):
    if grid[col[2]] == 0:
        if grid[col[0]] == grid[col[1]]:
            grid[col[0]] = grid[col[0]] * 2
            grid[col[1]] = 0
    if grid[col[3]] == 0:
        if grid[col[0]] == grid[col[1]]:
            grid[col[0]] = grid[col[0]] * 2
            grid[col[1]] = grid[col[2]]
            grid[col[2]] = 0
        elif grid[col[1]] == grid[col[2]]:
            grid[col[1]] = grid[col[1]] * 2
            grid[col[2]] = 0
    if grid[col[3]] != 0:
        if grid[col[0]] == grid[col[1]] and grid[col[2]] == grid[col[3]]:
            grid[col[0]] = grid[col[0]] * 2
            grid[col[1]] = grid[col[2]] * 2
            grid[col[2]] = 0
            grid[col[3]] = 0
        elif grid[col[0]] == grid[col[1]]:
            grid[col[0]] = grid[col[0]] * 2
            grid[col[1]] = grid[col[2]]
            grid[col[2]] = grid[col[3]]
            grid[col[3]] = 0
        elif grid[col[1]] == grid[col[2]]:
            grid[col[1]] = grid[col[1]] * 2
            grid[col[2]] = grid[col[3]]
            grid[col[3]] = 0
        elif grid[col[2]] == grid[col[3]]:
            grid[col[2]] = grid[col[2]] * 2
            grid[col[3]] = 0


def move():
    slide_up([0, 4, 8, 12])
    slide_up([1, 5, 9, 13])
    slide_up([2, 6, 10, 14])
    slide_up([3, 7, 11, 15])
    combine_up([0, 4, 8, 12])
    combine_up([1, 5, 9, 13])
    combine_up([2, 6, 10, 14])
    combine_up([3, 7, 11, 15])


def move_up():
    first_grid = grid.copy()
    move()
    if first_grid != grid:
        add_number()


def move_down():
    first_grid = grid.copy()
    grid.reverse()
    move()
    grid.reverse()
    if first_grid != grid:
        add_number()


def move_left():
    first_grid = grid.copy()
    rotate("left")
    move()
    rotate("right")
    if first_grid != grid:
        add_number()


def move_right():
    first_grid = grid.copy()
    rotate("right")
    move()
    rotate("left")
    if first_grid != grid:
        add_number()


def check_game_over():
    global grid, run, end
    copy = grid.copy()
    move_up()
    move_left()
    move_down()
    move_right()
    if grid == copy:
        end = True
        run = False
        score = str(sum(grid))
        label = my_font.render(score, 4, (0, 0, 0))

        while end:
            pygame.time.delay(100)

            for end_event in pygame.event.get():
                if end_event.type == pygame.QUIT:
                    end = False
                    run = False
                if end_event.type == pygame.KEYDOWN:
                    if end_event.key == pygame.K_RETURN:
                        grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        add_number()
                        add_number()
                        end = False
                        run = True

            draw_board()
            win.blit(end_image, (75, 75))
            win.blit(label, (225, 247.5))
            pygame.display.update()

    else:
        grid = copy


add_number()
add_number()
start = True
run = False
end = False


while start:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.KEYDOWN:
            start = False
            run = True

    draw_board()
    win.blit(start_image, (75, 75))
    pygame.display.update()


while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_up()
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_down()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_left()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_right()

    draw_board()
    draw_tiles()
    pygame.display.update()
    check_game_over()


pygame.quit()
