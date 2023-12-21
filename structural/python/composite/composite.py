from abc import ABC, abstractmethod

# Component
class GraphicalComponent(ABC):
    @abstractmethod
    def render(self):
        pass

# Leaf
class GraphicalLeaf(GraphicalComponent):
    def __init__(self, *args):
        self.name = args[0]

    def render(self):
        return self.name

# Composite
class GraphicalComposite(GraphicalComponent):
    def __init__(self, *args):
        self.name = args[0]
        self.children = []

    def add(self, child: GraphicalComponent):
        self.children.append(child)

    def remove(self, child: GraphicalComponent):
        self.children.remove(child)

    def render(self):
        for child in self.children:
            if isinstance(child, GraphicalLeaf):
                print(f"Component '{self.name}': '{child.render()}'")
            else:
                print(f"Component '{self.name}' has '{child.name}'")
                child.render()

def main():
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
    
if __name__ == "__main__":
    main()