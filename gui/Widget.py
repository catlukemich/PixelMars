class Widget:
    def __init__(self):
        self.position = (0,0)
        self.size = (10, 10)
        self.data = None
        self.click_listener = None
        self.hover_listener = None

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def containsMouse(self, x, y):
        x_inside = x > self.position[0] and x < self.position[0] + self.size[0]
        y_inside = y > self.position[1] and y < self.position[1] + self.size[1]
        return x_inside and y_inside


    def onMouseOver(self, event):
        if self.hover_listener == None: return False
        return self.hover_listener.onMouseOver(event, self)

    def onMouseOut(self, event):
        if self.hover_listener == None: return False
        return self.hover_listener.onMouseOut(event, self)

    def onClick(self, event):
        if self.click_listener == None: return False
        return self.click_listener.onClick(event, self)

    def draw(self, window):
        pass