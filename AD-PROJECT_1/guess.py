class Guess:
    def __init__(self, word):
        self.word = word

    def getWord(self):
        return self.word

    def isAnswer(self, text):
        if self.word == text:
            return True
        else:
            return False

    def getLength(self):
        return len(self.word)
