from composite import *

def test_simple_nested_elements(capfd):
    # Creating components
    window = GraphicalComposite('Window')
    container = GraphicalComposite('Image')
    image = GraphicalLeaf('image.jpg')
    # Assembling composite tree
    window.add(container)
    container.add(image)
    window.render()
    out, _ = capfd.readouterr()
    assert out == "Component 'Window' has 'Image'\nComponent 'Image': 'image.jpg'\n"

def test_multiple_nested_elements(capfd):
    # Creating components
    window = GraphicalComposite('Window')
    container = GraphicalComposite('Image')
    image = GraphicalLeaf('image.jpg')
    panel = GraphicalComposite('Panel')
    label = GraphicalComposite('Label')
    text = GraphicalLeaf('Hello World!')
    # Assembling composite tree
    window.add(container)
    container.add(image)
    window.add(panel)
    panel.add(label)
    label.add(text)
    window.render()
    out, _ = capfd.readouterr()
    assert out == "Component 'Window' has 'Image'\nComponent 'Image': 'image.jpg'\nComponent 'Window' has 'Panel'\nComponent 'Panel' has 'Label'\nComponent 'Label': 'Hello World!'\n"
