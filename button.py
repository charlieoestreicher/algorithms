import pygame


class Button:
    def __init__(self, color, x, y, width, height, highlight_color, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.highlight_color = highlight_color
        self.text = text
        self.menu_active = False
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win, outline=True):
        # Call this method to draw the button on the screen
        pos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(pos)
        print(self.menu_active)
        if outline:
            pygame.draw.rect(
                win,
                outline,
                (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                0,
            )
        print(self.menu_active)
        pygame.draw.rect(
            win,
            self.highlight_color if self.menu_active else self.color,
            (self.x, self.y, self.width, self.height),
            0,
        )

        if self.text != "":
            font = pygame.font.SysFont(None, 30)

            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2),
                ),
            )

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.menu_active = True
        self.menu_active = False

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        # print(self.menu_active)

        # self.active_option = -1
        # for i in range(len(self.option_list)):
        #     rect = self.rect.copy()
        #     rect.y += (i + 1) * self.rect.height
        #     if rect.collidepoint(mpos):
        #         self.active_option = i
        #         break

        # for event in event_list:
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #         print("hello")
        #         return
        # return -1
