import pygame

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
biggest = max(lst)

lst = [each / biggest for each in lst]
print(lst)

rectangles = {}
rect_width = width // len(lst)
for idx in range(0, len(lst)):
    left = width // len(lst) * idx
    top = height - (lst[idx] * height)
    rect_height = lst[idx] * height
    rectangles[idx] = {
        "left": left,
        "top": top,
        "rect_width": rect_width,
        "rect_height": rect_height,
    }

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for i in range(0, len(lst)):
        pygame.draw.rect(
            surface=screen,
            color="black",
            rect=pygame.Rect(
                rectangles[i]["left"],
                rectangles[i]["top"],
                rectangles[i]["rect_width"],
                rectangles[i]["rect_height"],
            ),
        )
        pygame.draw.rect(
            surface=screen,
            color="yellow",
            rect=pygame.Rect(
                rectangles[i]["left"],
                rectangles[i]["top"],
                rectangles[i]["rect_width"],
                rectangles[i]["rect_height"],
            ),
            width=2,
        )

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
