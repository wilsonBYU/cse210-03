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
        word_list (list): The list of random words
        word (string): The current word
        puzzle (Puzzle): The game's puzzle word.
        jumper (Jumper): The game's jumper.
        terminal_service (TerminalService): The game's terminal handler
        instructions (Instructions): The instructions class
        chosen_letter (char): The letter provided by the user
        is_playing (boolean): Wheter or not to keep playing.
    """
    def __init__(self):
        """Initialize the director class.

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
        """Initialize the game life cycle.
        
            Args:
            -----
            self (Director): An instance of Director. 
        """
        self._terminal_service.clear() #clear the terminal
        self._terminal_service.print_reversed_animation([
            self._jumper.get_jumper_image()[:-1], 
            self._instructions.get_instructions(), 
            self._instructions.get_title()
        ]) #will print the parachuter, the instructions and title like they are falling
        while self._is_playing: #check if the game is still playable
            self.do_outputs() #Print on the screen life cycle
            self.get_inputs() #Get inputs from client life cycle
            self.do_updates() #Do all the updates life cycle

    def get_inputs(self):
        """Get inputs life cycle.
        
            Args:
            -----
            self (Director): An instance of Director. 
        """
        if self._is_playing: #check if the game is still playable
            self._chosen_letter = self._terminal_service.read_text("Guess a letter [a-z]: ") #Ask for user letter
            self._terminal_service.clear() #clear the terminal window
        
    def do_updates(self):
        """Do updates life cycle.
        
            Args:
            -----
            self (Director): An instance of Director. 
        """
        if self._is_playing: #check if the game is still playable
            if self._puzzle.compare_letters(self._chosen_letter): #Check if the user leter is correct or not and return true or false
                self._terminal_service.write_text(f"You guessed a letter! You have {self._jumper.remaining_attempts_count()} remaining attemps!") #if the letter is in the list then print that in the screen
                if not "_" in self._puzzle.get_word_hidden_list(): #if there are no underscore in the hidden list means that the user guess all the letters
                    self.do_outputs() #print the parachuter image
                    self._is_playing = False #change the is playing to false becuase the user guessed the word so the game is over
                    self._terminal_service.print_reversed_animation([self._instructions.get_you_win()]) #print an animation for the you win message
                    self._terminal_service.write_text("\n".join(self._instructions.get_you_win())) #keep the title persistent since the animation clear the screen
                    self._terminal_service.write_text(f"The word was: {self._word}") #Let the user know what the word was
                        
                    
            else: #If the chosen letter is wrong then do the following
                self._terminal_service.write_text(f"Wrong letter! You have {self._jumper.remaining_attempts_count()} remaining attemps!") #Let the user know the remaining attemps
                self._jumper.guessed_wrong() #remove a line in the parachuter
                self._is_playing = self._jumper.remaining_attempts() #if there are no more remaining attempts the game is over
        
                if not self._is_playing: #if the game is over
                    self._jumper.guessed_wrong() #Update the last jumper line (change the head to an x)
                    self.do_outputs() #print the jumper and the reamiaining word list
                    self._terminal_service.print_reversed_animation([self._instructions.get_you_lose()]) #Print an animation with the title you lose
                    self._terminal_service.write_text("\n".join(self._instructions.get_you_lose())) #keeps the title persistent
                    self._terminal_service.write_text(f"The word was: {self._word.upper()}") #Print the correct word
                    
    def do_outputs(self):
        """Do outputs life cycle.
        
            Args:
            -----
            self (Director): An instance of Director. 
        """
        self._terminal_service.write_text("\n".join(self._instructions.get_title())) #keeps the title persistent
        self._terminal_service.write_text("\n"+"\n".join(self._instructions.get_instructions())) #keeps the instructions persistent
        self._terminal_service.write_text("\n"+"\n".join(self._jumper.get_jumper_image())) #Print the jumper image
        self._terminal_service.write_text(self._puzzle.get_word_hidden_list()) #Print the current hidden list no matter if it is guessed or not


