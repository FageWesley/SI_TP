from abc import ABC, abstractmethod

class Canard(ABC):
    def __init__(self,name) -> None:
        name = name

    def __str__(self) -> str:
        return f"Canard name: {self.name}"

    @abstractmethod
    def voler(self):
        pass

    @abstractmethod
    def cancaner():
        pass


class Colvert(Canard):
    def __init__(self,name) -> None:
        super().__init__(name)

    def voler(self):
        print("Je vole comme un colvert")

    def cancaner(self):
        print("Je cancanne comme un colvert")

class CouRouge(Canard):
    def __init__(self,name) -> None:
        super().__init__(name)

    def voler(self):
        print("Je vole comme un cou rouge")

    def cancaner(self):
        print("Je cancanne comme un cou rouge")