import pygame


class Scroller:
    '''
    Scroller responsible for scrolling the screen with RMB (Right Mouse Button).
    '''

    def __init__(self, main):
        ''' Construct a Scroller instance given access to the main class. '''
        self.main = main
        self.scrolling = False


    def enable(self):
        ''' Enable scroller - register it on the input system. '''
        self.main.input.addListener(self)

    def disable(self):
        ''' Disable scrolller - deregister it from the input system. '''
        self.main.input.removeListener(self)


    def onEvent(self, event):
        ''' Scroller event handling - for actuall scrolling. '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            self.scrolling = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            self.scrolling = False

        if event.type == pygame.MOUSEMOTION and self.scrolling:
            dx = event.rel[0] 
            dy = event.rel[1] 

            center = self.main.view.getCenter()
            center.x -= dx / 100
            center.y -= dy / 50
            self.main.view.setCenter(center)
        ''' Scroller event handling end '''