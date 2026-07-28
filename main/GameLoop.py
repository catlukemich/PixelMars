import pygame

from VDebugger.vdebugger import vd
from utils.MusicPlayer import MusicPlayer  # <-- Visual debugger


class GameLoop:

    def loop(self, the_game):
        from main.Game import Game

        game: Game = the_game
        done = False

        clock = pygame.time.Clock()

        old_width, old_height = game.window.get_size()  # <-- Old window width and size.
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                else:
                    consumed = game.input.dispatchEvent(event)
                    if consumed:
                        break
                    music_player = MusicPlayer.getInstance()
                    music_player.handle_event(event)

                if event.type == pygame.VIDEORESIZE:
                    new_width, new_height = event.size

                    delta_width = new_width - old_width
                    delta_height = new_height - old_height

                    game.toolbar.onResize(delta_width, delta_height)

                    old_width = new_width
                    old_height = new_height

            game.view.update(clock)
            # game.window.fill((0, 0, 0))
            game.window.fill((170, 66, 40))
            game.view.draw(game.window)

            for process in game.processes:
                process.draw(game.window)

                next_process = process.update(clock)
                if not next_process == None:
                    if next_process != process:
                        game.addProcess(process)

            game.gui.draw()
            game.tooltip.draw(game.window)

            pygame.display.update()

            clock.tick(60)
