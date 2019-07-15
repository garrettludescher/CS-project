import pygame
from pygame.locals import *
from random import randrange
import time


class Board:
    """Board

    The board object contains the internal state,
    including whether a square is filled and by whom.
    """
    def __init__(self, blockSize=40):
        self.blockSize = blockSize
        self.squares = [[0] * 6 for _ in range(7)]
        self._complete = False
        self._win = None
        self._player = 1
        self._win_font = None
        self._restart_font = None
        self._empty = 42

    def on_init(self):
        self._win_font = pygame.font.SysFont("Times New Roman", 100)
        self._restart_font = pygame.font.SysFont("Times New Roman", 30)
        # TODO: You need to set all the relative variables to the correct values.
        #       The squares need to be all zeros
        #       _win should be None
        #       _player should be 1
        #       _empty should be 7 * 6 = 42
        pass

    def click(self, x):
        """When a player clicks on square (x, y)"""
        if self._complete:
            return
        if (not 0 <= x <= 6) or (self.squares[x][-1] != 0):
            return

        # TODO: Find the lowest that is still empty and mark it as occupied by this player
        pass

        # TODO: If this player wins change _complete and _win variables
        pass

        # TODO: If there are no more empty squares mark it as a tie by setting _complete to True
        pass

        # TODO: Change the player to its negative
        pass

    def check_win(self, player):
        # TODO: Check if the player has marked four in a row. You can break this up to horizontal, vertical and diagonal
        return False

    def draw(self, surface):
        """Draws the board on the surface"""
        colors = [(255, 255, 255), (255, 255, 0), (255, 0, 0)]
        for x in range(7):
            for y in range(6):
                pygame.draw.circle(surface, colors[self.squares[x][y]], (int((x + 0.5) * self.blockSize), int((5.5 - y) * self.blockSize)), self.blockSize // 3)
        if self._complete:
            win_text = ""
            if self._win is None:
                win_text = "TIE!"
            elif self._win == 1:
                win_text = "YELLOW WINS!"
            elif self._win == -1:
                win_text = "RED WINS!"
            win_text_surf = self._win_font.render(win_text, True, (255, 0, 0), (255, 255, 255))
            text_rect = win_text_surf.get_rect()
            text_rect.center = ((7 * self.blockSize) // 2, (6 * self.blockSize) // 2)
            surface.blit(win_text_surf, text_rect)

            restart_surf = self._restart_font.render("Press Space to start again", True, (0, 0, 255), (255, 255, 255))
            text_rect = restart_surf.get_rect()
            text_rect.center = ((7 * self.blockSize) // 2, (6 * self.blockSize) // 2 + 40)
            surface.blit(restart_surf, text_rect)


class Game:
    """Game

    The game module is responsible for running the game.
    """
    def __init__(self, blockSize=100):
        """This is the initializing function of the Model object

        windowWidth:  windowWidth of the board in tiles
        windowHeight: windowHeight of the board in tiles
        blockSize:    size of each tile
        speed:  number of iterations in each second
        """
        self.blockSize = blockSize
        self.board = Board(blockSize=self.blockSize)
        self._running = False

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((7 * self.blockSize, 6 * self.blockSize), pygame.HWSURFACE)
        pygame.display.set_caption('BU Summer Challenge Tic Tac Toe')
        self.board.on_init()
        self._running = True

    def on_render(self):
        self._display_surf.fill((0, 0, 255))
        self.board.draw(self._display_surf)
        pygame.display.flip()

    def quit(self):
        self._running = False
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_SPACE] and self.board._complete:
                self.on_init()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    self.board.click(x // self.blockSize)

            self.on_render()

            if (keys[K_ESCAPE]):
                self.quit()

            time.sleep(1 / 20)
        self.quit()


if __name__ == '__main__':
    game = Game()
    game.on_execute()
