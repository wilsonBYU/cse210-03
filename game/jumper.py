import random

class Jumper:
    """The players stats in the game.

    The responsibility of Jumper is to keep track of all of the letters guessed and display
    the remaining parachute.

    Attributes:
    -----------
    _jumper (list[str]): The players remaining life.
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
        """Removes part of the Jumpers parachute if the users guess is incorrect.

            Args:
            -----
            self (Jumper): An instance of Jumper.
        """

        if len(self._jumper) <= 5:
            self._jumper.pop(0)
            self._jumper.insert(0, "   x")
        else:
            self._jumper.pop(0)

    def remaining_attempts_count(self):
        """Counts the remaining attempts for the game.

            Args:
            -----
            self (Jumper): An instance of Jumper.

            Returns:
            --------
            int: The parachutes remaining life.
        """
        return len(self._jumper)-6

    def remaining_attempts(self):
        """Checks if there are any remaining attempts left.

            Args:
            -----
            self (Jumper): An instance of Jumper.

            Returns:
            --------
            bool: True if the length of Jumper is greater than or equal to 6 else False.
        """
        return (len(self._jumper) >= 6)

    def get_jumper_image(self):
        """Gets the image of the Jumper.

            Args:
            -----
            self (Jumper): An instance of Jumper.

            Returns:
            --------
            list[str]: An image of the Jumper."""
        return self._jumper