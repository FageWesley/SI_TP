from abc import ABC, abstractmethod

#region Fly behavior
class FlyBehavior(ABC):

    @abstractmethod
    def voler(self):
        pass

class Fly2Wings(FlyBehavior):
    def voler(self):
        print("Je vole avec 2 ailes")

class FlyNone(FlyBehavior):
    def voler(self):
        print("Je vole sans ailes")
#endregion

#region Quack behavior

class QuackBehavior(ABC):

    @abstractmethod
    def cancaner(self):
        pass

class Quack(QuackBehavior):
    def cancaner(self):
        print("Je cancanne")

class Squeak(QuackBehavior):
    def cancaner(self):
        print("Je couine")


#endregion

#region Canard class
class Canard(ABC):
    def __init__(self,name,flyBehavior,quackBehavior) -> None:
        self.__name = name
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior

    @property
    def flyBehavior(self):
        return self.__flyBehavior

    @flyBehavior.setter
    def flyBehavior(self,value):
        if (isinstance(value,FlyBehavior)):
            self.__flyBehavior = value
        else:
            raise ValueError("flyBehavior must be FlyBehavior type")

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        return f"Canard name: {self.name}"
    
    def voler(self):
        self.flyBehavior.voler()

    def cancaner(self):
        self.quackBehavior.cancaner()
#endregion

#region Canard class children
class Colvert(Canard):
    def __init__(self,name) -> None:
        super().__init__(name,Fly2Wings(),Quack())


class CouRouge(Canard):
    def __init__(self,name) -> None:
        super().__init__(name,FlyNone(),Squeak())

#endregion

    



if __name__ == "__main__":
    colvert = Colvert("Colvert")
    print(colvert)
    colvert.voler()
    colvert.cancaner()

    couRouge = CouRouge("Cou Rouge")
    print(couRouge)
    couRouge.voler()
    couRouge.flyBehavior = Fly2Wings()
    couRouge.voler()
    couRouge.cancaner()