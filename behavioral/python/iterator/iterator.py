from collections.abc import Iterable, Iterator

class SimpleConcreteIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._position = 0
    
    def __next__(self):
        try:
            val = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return val

class ListConcreteCollection(Iterable):
    def __init__(self) -> None:
        self._collection = []
    
    def add_item(self, item: str) -> None:
        self._collection.append(item)
    
    def __iter__(self) -> SimpleConcreteIterator:
        return SimpleConcreteIterator(self._collection)