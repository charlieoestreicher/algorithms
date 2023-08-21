import pygame
from bubblesort import bubbleSort
import random
import SelectMenu
import button

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0


def normalize_lst(lst):
    biggest = max(lst)
    lst = [each / biggest for each in lst]
    return lst


def make_rectangles(lst):
    rectangles = {}
    rect_width = width / len(lst)
    for idx in range(0, len(lst)):
        left = width / len(lst) * idx
        top = height - (lst[idx] * height)
        rect_height = lst[idx] * height
        rectangles[idx] = {
            "left": left,
            "top": top,
            "rect_width": rect_width,
            "rect_height": rect_height,
        }
    return rectangles


lst = list(range(1, 101))
random.shuffle(lst)

steps = bubbleSort(lst)
step = 0

option_box = SelectMenu.OptionBox(
    x=0,
    y=0,
    w=160,
    h=40,
    color=(150, 150, 150),
    highlight_color=(100, 200, 255),
    font=pygame.font.SysFont(None, 30),
    option_list=["option 1", "2nd option", "another option"],
)

visualize_button = button.Button(
    color=(150, 150, 150),
    x=160,
    y=0,
    width=160,
    height=40,
    highlight_color=(100, 200, 255),
    text="run",
)

shuffle_button = button.Button(
    color=(150, 150, 150),
    x=320,
    y=0,
    width=160,
    height=40,
    highlight_color=(100, 200, 255),
    text="shuffle",
)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    lst = normalize_lst(steps[step])
    rectangles = make_rectangles(lst)

    for i in range(0, len(lst)):
        pygame.draw.rect(
            surface=screen,
            color="gray",
            rect=pygame.Rect(
                rectangles[i]["left"],
                rectangles[i]["top"],
                rectangles[i]["rect_width"],
                rectangles[i]["rect_height"],
            ),
        )
        pygame.draw.rect(
            surface=screen,
            color="black",
            rect=pygame.Rect(
                rectangles[i]["left"],
                rectangles[i]["top"],
                rectangles[i]["rect_width"],
                rectangles[i]["rect_height"],
            ),
            width=1,
        )
    selected_option = option_box.update(event_list)
    option_box.draw(screen)
    visualize_button.draw(screen)
    shuffle_button.draw(screen)
    visualize_button.update(event_list)
    shuffle_button.update(event_list)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(10) / 1000
    if step < len(steps) - 1:
        step += 1

pygame.quit()
