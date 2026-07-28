import pygame

MUSIC_END = pygame.USEREVENT + 1

class MusicPlayer():

    instance = None

    @staticmethod
    def getInstance():
        if MusicPlayer.instance == None:
            MusicPlayer.instance = MusicPlayer()
        return MusicPlayer.instance

    def __init__(self) -> None:
        self.track_index = 0
        
        self.tracks = [
            "assets/music/Space Music.mp3",
            "assets/music/MyVeryOwnDeadShip.wav",
            "assets/music/sPACE.wav",
            "assets/music/Blind Shift.mp3",
            "assets/music/GalacticTemple.wav",
            "assets/music/Planetrise v1_0.wav"
        ]

        
        pygame.mixer.music.set_endevent(MUSIC_END)

    def handle_event(self, event: pygame.event.Event):
        if event.type == MUSIC_END:
            self.track_index += 1
            if self.track_index == len(self.tracks):
                self.track_index = 0

            track_name = self.tracks[self.track_index]
            pygame.mixer.music.load(track_name)
            pygame.mixer.music.play()




    def start(self):
        self.track_index = 0
        track_name = self.tracks[self.track_index]
        pygame.mixer.music.load(track_name)
        pygame.mixer.music.play()