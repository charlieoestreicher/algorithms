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
        if outline:
            pygame.draw.rect(
                win,
                outline,
                (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                0,
            )
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

    def update(self, event_list):
        pos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(pos)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.menu_active:
                if self.text == "run":
                    print("run button clicked")
                    return 1
                if self.text == "shuffle":
                    print("shuffle button clicked")
                    return 1
        return -1
