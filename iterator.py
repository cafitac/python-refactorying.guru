from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    """
    이터레이터 선언
    """

    _position: int = None

    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        """
        :param collection: Iterate 할 collection class
        :param reverse: 역정렬 여부
        """
        self._collection = collection
        self._reverse = reverse
        # list index 의 시작 위치를 초기화
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        _position 에 대한 값을 뽑아내다가 IndexError 갑 발생하면 iterate 중지
        :return:
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")

