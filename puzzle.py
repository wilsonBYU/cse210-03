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
        unless the word_letter_list contains a character fron the current_word_letter_list.

    """

    def __init__(self, word=""):
        self._word_letter_list = []
        self._current_word_letter_list = []
        self._word_hidden_letter_list = []
        if word != "":
            self.generate_hidden_word_letter_list(word)

    def get_word_hidden_list(self):
        ''' Returns the hidden word list with only 
            the letters in the word letter list 
            revealed
        
        '''
        index = 0
        for i in self._current_word_letter_list:
            if i in self._word_letter_list:
                self._word_hidden_letter_list[index] = i
            else:
                self._word_hidden_letter_list[index] = "_"

            index += 1

        return self._word_hidden_letter_list

    def update_word_letter_list(self, letter):
        ''' Adds a new letter to the word list
        
        '''
        self._word_letter_list.append(letter.upper())
    

    def generate_hidden_word_letter_list(self, word):
        ''' Used to set the current word and generates
            the hidden word list with all "_"
            Clears all list 
        
        '''
        self._word_letter_list.clear()
        self._word_hidden_letter_list.clear()

        self._current_word_letter_list = list(word.upper())
        for i in self._current_word_letter_list:
            self._word_hidden_letter_list.append("_")
        