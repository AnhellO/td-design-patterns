import abc

# Component
class TextComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self):
        pass
    
# Concrete Component
class NormalTextComponent(TextComponent):
    def __init__(self, text: str):
        self._text = text

    def render(self):
        return f"{self._text}"

# Decorator
class TextDecorator(TextComponent, metaclass=abc.ABCMeta):
    def __init__(self, text_component: TextComponent):
        self._text_component = text_component

    @abc.abstractmethod
    def render(self):
        pass

# Concrete Decorator A
class HighlightTextDecorator(TextDecorator):
    def render(self):
        return f"<b>{self._text_component.render()}</b>"

# Concrete Decorator B
class UnderlineTextDecorator(TextDecorator):
    def render(self):
        return f"<u>{self._text_component.render()}</u>"
    
# Concrete Decorator C
class ItalicTextDecorator(TextDecorator):
    def render(self):
        return f"<i>{self._text_component.render()}</i>"
