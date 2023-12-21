import abc

class WritingState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, words):
        pass

class DefaultCaseConcreteState(WritingState):
    def write(self, words):
        print(words)

class UpperCaseConcreteState(WritingState):
    def write(self, words):
        print(words.upper())

class LowerCaseConcreteState(WritingState):
    def write(self, words):
        print(words.lower())

class TitleCaseConcreteState(WritingState):
    def write(self, words):
        print(words.title())

class TextEditorContext:
    def __init__(self, state):
        self._state = state
    
    def set_state(self, state):
        self._state = state

    def write(self, words):
        self._state.write(words)