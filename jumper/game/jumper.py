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
                    "",
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

        self._jumper.pop(1)
        if len(self._jumper) <= 6:
            self._jumper.pop(1)
            self._jumper.insert(1, "   x")


    def remaining_attempts(self):

        return (len(self._jumper) <= 5)


    def get_jumper_image(self):
        """Gets the image of the Jumper.

        Args:
        -----
            self (Jumper): An instance of Jumper.

        Returns:
        --------
            dictionary: An image of the remaining parachute."""
        return "\n".join(self._jumper)