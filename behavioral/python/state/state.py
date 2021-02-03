import abc

class WritingState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, words):
        pass

class DefaultCaseState(WritingState):
    def write(self, words):
        print(words)

class UpperCaseState(WritingState):
    def write(self, words):
        print(words.upper())

class LowerCaseState(WritingState):
    def write(self, words):
        print(words.lower())

class TitleCaseState(WritingState):
    def write(self, words):
        print(words.title())

class TextEditor:
    def __init__(self, state):
        self._state = state
    
    def set_state(self, state):
        self._state = state

    def type_words(self, words):
        self._state.write(words)