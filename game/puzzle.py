# Puzzle Class
# CSE210 By Robert Odell


class Puzzle:
    """Generates a masked puzzle from a given word

    The purpose of Puzzle is to accept a random word
    then generate a masked list which is revealed as
    a list of guessed letters is updated.


    Attributes:
        word_letter_list (list[str]): A list that holds the selected letters from
        the user.

        current_word_letter_list (list[str]): A list that holds each letter in order
        from the current word

        word_hidden_letter_list (list[str]): A list that holds underscores as placeholders
        unless the word_letter_list contains a character from the current_word_letter_list.

    """

    def __init__(self, word=""):
        self._guessed_letters = [] # This doesn't need to be a list.
        self._letters = [] 
        self._hidden_letters = [] # Gets display to player
        if word != "":
            self.generate_hidden_word_letter_list(word)

    def get_word_hidden_list(self):
        ''' Returns the hidden word list with only
            the letters in the word letter list
            revealed

        '''
        index = 0
        for i in self._letters:
            if i in self._guessed_letters:
                self._hidden_letters[index] = i
            else:
                self._hidden_letters[index] = "_"

            index += 1

        return " ".join(self._hidden_letters)+"\n"

    def compare_letters(self,incoming_letter):
        """Find out if guessed letter is in list.
        Returns True or False"""
        incoming_letter = incoming_letter.upper()
        if incoming_letter in self._letters:
            self.update_word_letter_list(incoming_letter)
            return True
        else:
            return False   

    def update_word_letter_list(self, letter):
        ''' Adds a new letter to the word list

        '''
        self._guessed_letters.append(letter.upper())

    def generate_hidden_word_letter_list(self, word):
        ''' Used to set the current word and generates
            the hidden word list with all "_"
            Clears all list

        '''
        self._guessed_letters.clear()
        self._hidden_letters.clear()

        self._letters = list(word.upper())
        for i in self._letters:
            self._hidden_letters.append("_")