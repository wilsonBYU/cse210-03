from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper
import random

class Director:
    """A person who directs the game.
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
    -----------
        puzzle (Puzzle): The game's puzzle word.
        is_playing (boolean): Wheter or not to keep playing.
        jumper (Jumper): The game's jumper.
    
    """
    def __init__(self):

        # generate the word to be guessed
        word_list = ["burrito", "quesadilla", "taco"]
        word = random.choice(word_list)

        self._puzzle = Puzzle(word)
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()

    def start_game(self):

        while self._is_playing:
            letter = self._get_inputs()
            self._do_updates(letter)
            self._do_outputs()
            # check win/loss condition XXXXXXXXXX (to determine whether to continue looping)

    
    def _get_inputs(self):
        letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        return letter
        


    def _do_updates(self,letter):

        keep = self._puzzle.compare_letters(letter) # true result indicates correct guess
        if keep == False:
            self._jumper.guessed_wrong()
        #self._jumper.parachute(keep)
        
        

    def _do_outputs(self):

        # print letter-puzzle
        print(" ".join(self._puzzle.get_word_hidden_list()))

        # print the jumper
        # if you have __str__() method, you can just write print(self._jumper) OR print(self._jumper.get_jumper_image())
        print(self._jumper.get_jumper_image())




