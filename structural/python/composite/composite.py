from abc import ABC, abstractmethod

class GraphicalComponent(ABC):
    @abstractmethod
    def render(self):
        pass

class GraphicalLeaf(GraphicalComponent):
    def __init__(self, *args):
        self.name = args[0]

    def render(self):
        return self.name

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