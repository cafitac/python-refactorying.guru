class Target:
    """
    클라이언트 코드에서 사용하는 인터페이스를 정의하여 구현된 클래스
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    기존 스팩과 다르게 개발되어 있는 클래스 + 작동함에 있어 정상적이지 않음
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    Adaptee 클래스를 정상적으로 사용할 수 있도록 변경
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objets:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
