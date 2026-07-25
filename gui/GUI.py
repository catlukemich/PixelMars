import pygame


class GUI:
    def __init__(self, main):
        self.main = main
        self.main.input.addListener(self)
        self.widgets = []
        self.hover_widget = None


    def addWidget(self, widget):
        self.widgets.append(widget)

    def removeWidget(self, widget):
        self.widgets.remove(widget)

    def draw(self):
        # Drawing a frame around the gui:
        window = self.main.window
        pygame.draw.rect(window, (0xbb,0x99,0x77), (0, 600, 800, 200), 2)
        window.fill((0xff,0xbb,0x77), (0, 600, 800, 200) )

        for widget in self.widgets:
            widget.draw(self.main.window)

    def onEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]

            hover_widget = None
            for widget in self.widgets:
                if widget.containsMouse(x, y):
                    hover_widget = widget
                    break

            if (self.hover_widget != None and self.hover_widget != hover_widget):
                self.hover_widget.onMouseOut(event)
            if (self.hover_widget != hover_widget):
                widget.onMouseOver(event)
            self.hover_widget = hover_widget


            return False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover_widget != None:
                self.hover_widget.onClick(event)