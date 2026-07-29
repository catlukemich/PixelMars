
import pygame


class Animation:

    def __init__(self, frames):
        self.frames = frames
        self.length = len(frames)
        self.frame_index = 0 # <-- The current frame index.
        self.frame_time = 0 # <-- The time current frame is being displayed.
        self.ms_per_frame = 50 # <-- Milliseconds per frame.

    def update(self, clock: pygame.time.Clock):
        self.frame_time += clock.get_time()
        if self.frame_time > self.ms_per_frame: # <-- The frame has ended.
            self.frame_time = self.frame_time - self.ms_per_frame
            self.frame_index += 1
            if self.frame_index >= self.length:
                self.frame_index = 0


    def draw(self, surface, position):
        frame = self.frames[self.frame_index]
        surface.blit(frame, position)
