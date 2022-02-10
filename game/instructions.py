class Instructions:
    """Class that holds all the usefull text.

        Attributes:
        -----------
        _instructions list[str]: The games instructions.
        _title list[str]: The games title.
        _you_win list[str]: A message telling the player they won the game.
        _you_lose list[str]: A message telling the player they lost the game.
    """

    def __init__(self):
        """Initialize the Instructions class.

        Args:
        -----
        self (Instructions): An instance of Instructions.
        """
        self._instructions = [
            "The purpose of the game is simple: Try to guess the hidden word letter by letter.",
            "Every letter you guess will replace the underscores in the hidden word until it is completed",
            "If you don't guess the word you fail. But come on! There is always a chance you could win! I guess...",
            ""
        ]

        self._title = [
            " _____ ",
            "/\___ \ ",
            "\/__/\ \  __  __    ___ ___   _____      __   _ __  ",
            "   _\ \ \/\ \/\ \ /' __` __`\/\ '__`\  /'__`\/\`'__\ ",
            "  /\ \_\ \ \ \_\ \/\ \/\ \/\ \ \ \L\ \/\  __/\ \ \/",
            "  \ \____/\ \____/\ \_\ \_\ \_\ \ ,__/\ \____\\\ \_\ ",
            "   \/___/  \/___/  \/_/\/_/\/_/\ \ \/  \/____/ \/_/ ",
            "                                \ \_\    ",
            "                                 \/_/",
            ""
        ]

        self._you_win = [
            " __    __                    __      __ ",
            "/\ \  /\ \                  /\ \  __/\ \  __ ",
            "\ `\`\\\/'/ ___   __  __     \ \ \/\ \ \ \/\_\    ___  ",
            " `\ `\ /' / __`\/\ \/\ \     \\ \ \ \ \ \ \\/\ \ /' _ `\ ",
            "   `\ \ \/\ \L\ \ \ \_\ \     \\ \ \_/ \_\ \ \ \/\ \/\ \ ",
            "     \ \_\ \____/\ \____/      \ `\___x___/\ \_\ \_\ \_\ ",
            "      \/_/\/___/  \/___/        '\/__//__/  \/_/\/_/\/_/",
            ""
        ]

        self._you_lose = [
            " __    __                    __   ",
            "/\ \  /\ \                  /\ \ ",
            "\ `\`\\/'/  ___   __  __     \ \ \        ___     ____     __   ",
            " `\ `\ /' / __`\/\ \/\ \     \ \ \  __  / __`\  /',__\  /'__`\ ",
            "   `\ \ \/\ \L\ \ \ \_\ \     \ \ \L\ \/\ \L\ \/\__, `\/\  __/ ",
            "     \ \_\ \____/\ \____/      \ \____/\ \____/\/\____/\ \____\ ",
            "      \/_/\/___/  \/___/        \/___/  \/___/  \/___/  \/____/",
            ""
        ]

    def get_instructions(self):
        """Gets the instructions text.

            Args:
            -----
            self (Instructions): An instance of Instructions.

            Returns:
            --------
            list[str]: The instructions to the game.
        """
        return self._instructions

    def get_title(self):
        """Gets the title image.

            Args:
            -----
            self (Instructions): An instance of Instructions.

            Returns:
            --------
            list[str]: The game title.
        """
        return self._title

    def get_you_win(self):
        """Gets the you win image.

            Args:
            -----
            self (Instructions): An instance of Instructions.

            Returns:
            --------
            list[str]: A message telling the player they won the game.
        """
        return self._you_win

    def get_you_lose(self):
        """Gets the you lose image.

            Args:
            -----
            self (Instructions): An instance of Instructions.

            Returns:
            --------
            list[str]: A message telling the player they lost the game.
        """
        return self._you_lose
