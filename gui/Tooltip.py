import pygame

from VDebugger.vdebugger import vd
from gui.Widget import Widget


class Tooltip(Widget):
    """
    Tooltip is a black text on white background displayed text widget. It allows for displaying short messages
    about user interface functionalities and features. It follows singleton design pattern, so don't initialize
    it by yourself, instead use the getInstance static method.
    """

    instance = None

    @staticmethod
    def getInstance():
        if Tooltip.instance == None:
            Tooltip.instance = Tooltip()
        return Tooltip.instance

    def __init__(self):
        super().__init__()
        self.text = ""
        self.text_surface = None
        self.setText("Tooltip")
        self.visible = False

    def setText(self, text):
        """
        Set the text for the tooltip.
        Beyond setting the text in order for tooltip to display correctly
        it must be set visible with setVisible(True) method call.
        """
        self.text = text
        font = pygame.font.Font("assets/fonts/DejaVuSans.ttf", 12)
        w, h = font.size(text)
        w += 4  # <-- Add horizontal margins around the tooltip..
        h += 4  # <-- .. and vertical.

        final_surface = pygame.surface.Surface(
            (w, h), pygame.SRCALPHA
        )  # <-- The final surface used as a tooltip - with alpha component (SRCALPHA arg).
        pygame.draw.rect(  # <-- Draw background rounded corner white rectangle.
            final_surface, pygame.color.Color(255, 255, 255), (0, 0, w, h), 0, 3
        )
        pygame.draw.rect(  # <-- Draw rounded black border.
            final_surface, pygame.color.Color(0, 0, 0), (0, 0, w, h), 1, 3
        )
        text_surface = font.render(
            text, antialias=True, color=pygame.color.Color(0, 0, 0)
        )
        final_surface.blit(text_surface, (2, 2))
        self.text_surface = final_surface

    def setVisible(self, visible):
        """Call this function to actually show/hide the tooltip."""
        self.visible = visible

    def draw(self, window):
        if not self.visible:
            return
        window.blit(self.text_surface, self.position)

    def containsMouse(self, x, y):
        """
        The tooltip should never be considered as containing mouse,
        since this is a ghost-like widget that doesn't follow any interactions with user,
        other than being displayed when the user moves mouse over any other widget.
        """
        return False
