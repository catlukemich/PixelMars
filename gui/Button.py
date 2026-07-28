import pygame

from gui.Widget import Widget


class Button(Widget):

    def __init__(self, image):
        Widget.__init__(self)
        self.image = image
        rect = image.get_rect()
        self.size = (rect.width, rect.height)

    def draw(self, window):
        x = self.position[0]
        y = self.position[1]
        width = self.size[0]
        height = self.size[1]
        window.fill((255, 255, 255), (x, y, width, height))
        window.blit(self.image, self.position)
        pygame.draw.rect(window, (0, 0, 0), (x, y, width, height), 1)

    def onMouseOver(self, event):
        print("On mouse over " + str(self))
        from gui.Tooltip import Tooltip

        if self.tooltip_text:
            tooltip = Tooltip.getInstance()
            tooltip.setVisible(True)   

            offseted_position = (self.position[0], self.position[1] + self.size[1])
            tooltip.setPosition(offseted_position)

            tooltip.setText(self.tooltip_text)
        return super().onMouseOver(event)

    def onMouseOut(self, event):
        from gui.Tooltip import Tooltip
        tooltip = Tooltip.getInstance()
        tooltip.setVisible(False)

        return super().onMouseOut(event)

    def setTooltipText(self, text):
        self.tooltip_text = text

    