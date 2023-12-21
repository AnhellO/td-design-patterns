import pytest

from decorator import NormalTextComponent, HighlightTextDecorator, ItalicTextDecorator, UnderlineTextDecorator

@pytest.mark.parametrize("input, expected", [
    (
        "Normal text",
        "Normal text"
    )
])
def test_default(input, expected):
    obj = NormalTextComponent(input)
    assert expected == obj.render()

@pytest.mark.parametrize("input, expected", [
    (
        "Highlighted text",
        "<b>Highlighted text</b>"
    )
])
def test_decorated(input, expected):
    obj = HighlightTextDecorator(NormalTextComponent('Highlighted text'))
    assert expected == obj.render()

@pytest.mark.parametrize("input, expected", [
    (
        "Normal text",
        "<b><u>Highlighted and underlined text</u></b>"
    )
])
def test_more_than_one_decorator(input, expected):
    obj = HighlightTextDecorator(UnderlineTextDecorator(NormalTextComponent('Highlighted and underlined text')))
    assert expected == obj.render()

@pytest.mark.parametrize("input, expected", [
    (
        "Normal text",
        "<b><i><u>Highlighted and underlined text</u></i></b>"
    )
])
def test_all_decorators(input, expected):
    obj = HighlightTextDecorator(ItalicTextDecorator(UnderlineTextDecorator(NormalTextComponent('Highlighted and underlined text'))))
    assert expected == obj.render()