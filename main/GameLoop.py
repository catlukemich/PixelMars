import pygame

from VDebugger.vdebugger import vd # <-- Visual debugger

class GameLoop():

    def loop(self, game):
        done = False

      
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                else:
                    consumed = game.input.dispatchEvent(event)
                    if consumed: break

            game.view.update(clock)
            # game.window.fill((0, 0, 0))
            game.window.fill((170,66,40))
            game.view.draw(game.window)

            for state in game.states:
                state.draw(game.window)
                
                next_state = state.update(clock)
                if not next_state == None:
                    if next_state != state:
                        game.addState(state)

                vd(state, state)

            game.gui.draw()
            pygame.display.update()

            clock.tick(60)