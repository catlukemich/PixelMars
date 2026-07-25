from view.Sprite import Sprite
from view.Updateable import Updateable


class AnimatedSprite(Sprite, Updateable):
    def __init__(self, animation, repeat = True, frame_duration = 100):
        Sprite.__init__(self, animation.frames[0])
        self.animation = animation
        self.frame_duration = frame_duration
        self.repeat = repeat
        self.animation_listener = None
        self.frame = 0
        self.time = 0
        self.loop = 0

    def setAnimation(self, animation):
        self.animation = animation


    def setAnimationListener(self, animation_listener):
        self.animation_listener = animation_listener


    def update(self, clock):
        if self.loop > 0 and not self.repeat:
            return

        dt = clock.get_time()
        self.time += dt
        if self.time > self.frame_duration:
            self.time = 0
            self.frame += 1
            if self.frame < len(self.animation.frames):
                self.setImage(self.animation.frames[self.frame])
            else:
                if self.animation_listener is not None:
                    self.animation_listener.onAnimationEnd(self)
                self.frame = 0
                self.loop += 1
