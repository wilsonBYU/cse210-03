import random

class Jumper:
    """The players stats in the game.

    The responsibility of Jumper is to keep track of all of the letters guessed and display
    the remaining parachute.

    Attributes:
    -----------
        _jumper (dict[int, str]): The players remaining life.
        _word_list (list): The list of hidden words in the game.
        _current_word (str): The hidden word the player needs to guess.
        _guess_count (int): The remaining guesses the player has.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
        -----
            self (Jumper): An instance of Jumper.
        """

        self._jumper = [
                    "  ___",
                    " /___\\",
                    " \\   /",
                    "  \\ /",
                    "   O",
                    "  /|\\",
                    "  / \\",
                    "",
                    "^^^^^^^"
                ]

    def guessed_wrong(self):
        if len(self._jumper) <= 5:
            self._jumper.pop(0)
            self._jumper.insert(0, "   x")
        else:
            self._jumper.pop(0)
            
    def remaining_attempts_count(self):
        return len(self._jumper)-6
            
    def remaining_attempts(self):
        return (len(self._jumper) >= 6)

    def get_jumper_image(self):
        """Gets the image of the Jumper.

        Args:
        -----
            self (Jumper): An instance of Jumper.

        Returns:
        --------
            dictionary: An image of the remaining parachute."""
        return self._jumper