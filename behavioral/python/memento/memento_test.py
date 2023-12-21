import unittest

from memento import TextEditor, TextEditorMemento, Caretaker

class MementoTest(unittest.TestCase):
    def test_simple_restore(self):
        caretaker = Caretaker()
        editor = TextEditor("content!")
        self.assertEqual("content!", editor.get_content())
        
        caretaker.push(editor.save())
        editor.add_new_content("more content!")
        self.assertEqual("content!\nmore content!", editor.get_content())
        
        caretaker.push(editor.save())
        editor.add_new_content("more contenttttttt!")
        self.assertEqual("content!\nmore content!\nmore contenttttttt!", editor.get_content())
        
        editor.restore(caretaker.pop())
        self.assertEqual("content!\nmore content!", editor.get_content())
        
        editor.restore(caretaker.pop())
        self.assertEqual("content!", editor.get_content())


if __name__ == "__main__":
    unittest.main()
