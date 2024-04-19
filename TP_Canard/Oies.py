from Canard import Canard, Quack, Fly2Wings


class Oie():

    def honk(self):
        print("Je cacarde")



class CanardAdapter(Canard):
    def __init__(self, goose) -> None:
        self.__oie = goose
        super().__init__("goose", Fly2Wings(), Quack())

    def quack(self):
        self.__oie.honk()

