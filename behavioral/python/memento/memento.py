class TextEditorMemento:
    def __init__(self, content: str):
        self.content = content
        
    def get_state(self):
        return self.content

class TextEditor:
    def __init__(self, content: str):
        self.content = content
    
    def get_content(self):
        return self.content
    
    def add_new_content(self, extra_content: str):
        self.content += f"\n{extra_content}"
        
    def save(self):
        return TextEditorMemento(self.content)
    
    def restore(self, m: TextEditorMemento):
        self.content = m.get_state()

class Caretaker:
    def __init__(self):
        self.history = []

    def push(self, m: TextEditorMemento):
        self.history.append(m)
    
    def pop(self):
        return self.history.pop()