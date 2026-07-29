import pygame

from gui.Widget import Widget


class AnimatedIcon(Widget):

    def __init__(self, animation_atlas, num_images, frame_width, frame_height):
        super().__init__()
        self.animation_atlas = animation_atlas
        self.num_images = num_images
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_index = 0  # <-- The current frame index.
        self.frame_time = 0  # <-- The time current frame is being displayed.
        self.frames_per_second = 10  # <-- Milliseconds per frame.

    def update(self, clock: pygame.time.Clock):
        self.frame_time += clock.get_time()
        ms_per_frame = 1 / self.frames_per_second * 1000
        if self.frame_time > ms_per_frame:  # <-- The frame has ended.
            self.frame_time = self.frame_time - ms_per_frame
            self.frame_index += 1
            if self.frame_index >= self.num_images:
                self.frame_index = 0

    def draw(self, window):
        total_slots = self.animation_atlas.get_size()[0] // self.frame_width
        row = self.frame_index // total_slots
        col = self.frame_index % total_slots

        draw_region = (
            col * self.frame_width,
            row * self.frame_height,
            self.frame_width,
            self.frame_height,
        )

        window.blit(self.animation_atlas, self.position, draw_region)
