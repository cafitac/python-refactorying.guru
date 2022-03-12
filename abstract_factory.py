from __future__ import annotations  # forward reference 가 가능하게 함
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Product 를 생성하는 Factory 추상화 클래스
    추상화 메서드인 (create_product_a, create_product_b) 를 선언해놓음
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Factory 에 대한 구현채 1
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Factory 에 대한 구현체 2
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    ProductA 에 대한 추상화 클래스
    추상화 메서드인 useful_function_a 를 선언해놓음
    """
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    """
    ProductA 에 대한 구현체 1
    """
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    """
    ProductA 에 대한 구현체 2
    """
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    ProductB 에 대한 추상화 클래스
    추상화 메서드인 (useful_function_b, another_useful_function_b) 를 선언해놓음
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    """
    ProductB 에 대한 구현체 1
    """
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the {result}"


class ConcreteProductB2(AbstractProductB):
    """
    ProductB 에 대한 구현체 2
    """
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the {result}"


def client_code(factory: AbstractFactory) -> None:
    """
    실제 Factory 구현체를 통해 로직을 실행할 수 있는 클라이언트 코드
    :param factory:
    :return: None
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())  # Factory1 에 대한 코드를 실행

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())  # Factory2 에 대한 코드를 실행
