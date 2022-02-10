from os import name, system
import sys
from time import sleep

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)
        
    def clear(self):

        """Clear the screen

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        if name == "nt":
            system("cls")
        else:
            system("clear")
            
    def print_reversed_animation(self, lines_list):
        """Gets the list of lists and then print them in reverse order like if each line is falling down.

        Args: 
            self (TerminalService): An instance of TerminalService.
            lines_list (list): A list of lists that contains each line to be printed in the screen.

        """
        reversed_list = []
        for section in lines_list:
            section_copy = section.copy()
            section_copy.reverse()
            for line in section:
                reversed_list.insert(0,section_copy.pop(0))
                print("\n".join(reversed_list))
                sleep(0.1)    
                self.clear()    
        
