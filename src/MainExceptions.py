class Exit(Exception):

    def __init__(self):
        return

class ChangeGameMode(Exception):

    def __init__(self, newGameMode):
        self.newGameMode = newGameMode
        return

