import pygame

from gui.Widget import Widget


class GUI:
    def __init__(self, main):
        self.main = main
        self.main.input.addListener(self)
        self.widgets: list[Widget] = []
        self.hover_widget = None

    def addWidget(self, widget):
        self.widgets.append(widget)

    def removeWidget(self, widget):
        self.widgets.remove(widget)

    def containsWidget(self, widget):
        return widget in self.widgets

    def draw(self):
        for widget in self.widgets:
            widget.draw(self.main.window)

    def onEvent(self, event):
        reversed_widgets = reversed(self.widgets)
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]

            hover_widget = None
            for widget in reversed_widgets:
                if widget.containsMouse(x, y):
                    hover_widget = widget
                    break

            if hover_widget != self.hover_widget:
                if self.hover_widget != None:
                    self.hover_widget.onMouseOut(event)
                if hover_widget != None:
                    hover_widget.onMouseOver(event)

            self.hover_widget = hover_widget

            return False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover_widget != None:
                self.hover_widget.onClick(event)

    def update(self, clock: pygame.time.Clock):
        for widget in self.widgets:
            widget.update(clock)
        
