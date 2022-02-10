# Puzzle Class
# CSE210 By Robert Odell


class Puzzle:
    """Generates a masked puzzle from a given word

    The purpose of Puzzle is to accept a random word
    then generate a masked list which is revealed as
    a list of guessed letters is updated.


    Attributes:
    -----------
    _guessed_letters (list[str]): A list that holds the selected letters from
    the user.

    _letters (list[str]): A list that holds each letter in order
    from the current word

    _hidden_letters (list[str]): A list that holds underscores as placeholders
    unless if the _guessed_letters list contains a character from the _letters list.

    """

    def __init__(self, word=""):
        """Constructs a new Puzzle.

            Args:
            -----
            self (Puzzle): An instance of Puzzle.
            word (str): A random word received from Director.
        """
        self._guessed_letters = []
        self._letters = []
        self._hidden_letters = []
        if word != "":
            self.generate_hidden_letters(word)

    def get_hidden_letters(self):
        """Returns the hidden letter list with only
        the letters in the guessed lettes list
        revealed.

        Args:
        -----
        self (Puzzle): An instance of Puzzle.

        Returns:
        --------
        list[str]: The _hidden_letter list joined with spaces.
        """

        index = 0
        for i in self._letters:
            if i in self._guessed_letters:
                self._hidden_letters[index] = i
            else:
                self._hidden_letters[index] = "_"

            index += 1

        return " ".join(self._hidden_letters)+"\n"

    def compare_letters(self, incoming_letter):
        """Finds out if the letter provided by the user is in the list.

        Returns True or False

        Args:
        -----
        self (Puzzle): An instance of Puzzle.
        incoming_letter (str): The letter guessed by the user.
        """

        incoming_letter = incoming_letter.upper()
        if incoming_letter in self._letters:
            self.update_guessed_letters(incoming_letter)
            return True
        else:
            return False

    def update_guessed_letters(self, letter):
        """Adds a new letter to the word list.

        Args:
        -----
        self (Puzzle): An instance of Puzzle.
        letter (str): The letter guessed by the user.
        """
        self._guessed_letters.append(letter.upper())

    def generate_hidden_letters(self, word):
        """Used to set the current word and generates
        the hidden word list with all "_"

        Clears each list

        Args:
        -----
        self (Puzzle): An instance of Puzzle.
        word (str): A random word received from Director.
        """
        self._guessed_letters.clear()
        self._hidden_letters.clear()

        self._letters = list(word.upper())
        for i in self._letters:
            self._hidden_letters.append("_")