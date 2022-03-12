from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Creator 추상화 클래스
    """
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    """
    Product1 구현체를 생성하는 Creator 구현체
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
    Product2 구현체를 생성하는 Creator 구현체
    """
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    Product 추상화 클래스
    """
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    """
    Product1 구현체
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    """
    Product2 구현체
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
