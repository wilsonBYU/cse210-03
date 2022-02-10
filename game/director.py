from .terminal_service import TerminalService
from .puzzle import Puzzle
from .jumper import Jumper
from .instructions import Instructions
import random

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
    -----------
    _word_list (list): The list of random words.
    _word (string): The current word.
    _puzzle (Puzzle): The game's puzzle word.
    _jumper (Jumper): The game's jumper.
    _terminal_service (TerminalService): The game's terminal handler.
    _instructions (Instructions): The instructions class.
    _chosen_letter (char): The letter provided by the user.
    _is_playing (boolean): Whether or not to keep playing.
    """
    def __init__(self):
        """Initializes the director class.

            Args:
            -----
            self (Director): An instance of Director.
        """
        self._word_list = ["burrito", "quesadilla", "taco"]
        self._word = random.choice(self._word_list)
        self._puzzle = Puzzle(self._word)
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._instructions = Instructions()
        self._chosen_letter = ""
        self._is_playing = True

    def start_game(self):
        """Initializes the game life cycle.

            Args:
            -----
            self (Director): An instance of Director.
        """
        self._terminal_service.clear() # Clears the terminal
        self._terminal_service.print_reversed_animation([
            self._jumper.get_jumper_image()[:-1],
            self._instructions.get_instructions(),
            self._instructions.get_title()
        ]) # Will print the parachuter, the instructions and title like they are falling
        while self._is_playing: # Checks if the game is still playable
            self._do_outputs() # Prints on the screen life cycle
            self._get_inputs() # Gets input from client life cycle
            self._do_updates() # Do all the updates life cycle

    def _get_inputs(self):
        """Gets input life cycle.

            Args:
            -----
            self (Director): An instance of Director.
        """
        if self._is_playing: # Checks if the game is still playable
            self._chosen_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ") # Asks user for letter
            self._terminal_service.clear() # Clears the terminal window

    def _do_updates(self):
        """Performs update life cycle.

            Args:
            -----
            self (Director): An instance of Director.
        """
        if self._is_playing: # Checks if the game is still playable
            if self._puzzle.compare_letters(self._chosen_letter): # Checks if the user letter is correct or not and return true or false
                self._terminal_service.write_text(f"You guessed a letter! You have {self._jumper.remaining_attempts_count()} remaining attempts!") # If the letter is in the list then print that in the screen
                if not "_" in self._puzzle.get_hidden_letters(): # If there are no underscore in the hidden list means that the user guessed all of the letters
                    self._do_outputs() # Print the parachuter image
                    self._is_playing = False # Changes the is playing to false because the user guessed the word so the game is over
                    self._terminal_service.print_reversed_animation([
                    self._jumper.get_jumper_image()[:-1],
                    self._instructions.get_you_win()]) # Prints an animation for the you win message and the parachuter
                    self._terminal_service.write_text("\n".join(self._instructions.get_you_win())) # Keeps the title persistent since the animation clear the screen

                    self._terminal_service.write_text("\n"+"\n".join(self._jumper.get_jumper_image()[:-2])+
                                                      "\n"+"\n".join(self._jumper.get_jumper_image()[-1:])) # Prints the jumper image

                    self._terminal_service.write_text(f"\nThe word was: {self._word.upper()}\n") # Lets the user know what the word was


            else: # If the chosen letter is wrong then do the following
                self._terminal_service.write_text(f"Wrong letter! You have {self._jumper.remaining_attempts_count()} remaining attempts!") # Lets the user know the remaining attempts
                self._jumper.guessed_wrong() # Remove a line in the parachuter
                self._is_playing = self._jumper.remaining_attempts() # If there are no more remaining attempts the game is over

                if not self._is_playing: # If the game is over
                    self._jumper.guessed_wrong() # Updates the last jumper line (change the head to an x)
                    self._do_outputs() # Prints the jumper and the reamiaining word list
                    self._terminal_service.print_reversed_animation([
                    self._jumper.get_jumper_image()[:-1],
                    self._instructions.get_you_lose()]) # Prints an animation with the title you lose and parachuter image
                    self._terminal_service.write_text("\n".join(self._instructions.get_you_lose())) # Keeps the title persistent

                    self._terminal_service.write_text("\n"+"\n".join(self._jumper.get_jumper_image()[:-2])+
                                                      "\n"+"\n".join(self._jumper.get_jumper_image()[-1:])) # Prints the jumper image

                    self._terminal_service.write_text(f"\nThe word was: {self._word.upper()}\n") # Prints the correct word

    def _do_outputs(self):
        """Performs output life cycle.

            Args:
            -----
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text("\n".join(self._instructions.get_title())) # Keeps the title persistent
        self._terminal_service.write_text("\n"+"\n".join(self._instructions.get_instructions())) # Keeps the instructions persistent
        self._terminal_service.write_text(self._puzzle.get_hidden_letters()) # Prints the current hidden list no matter if it is guessed or not
        self._terminal_service.write_text("\n"+"\n".join(self._jumper.get_jumper_image())) # Prints the jumper image