from Canard import Colvert,CouRouge,Canard

class DuckSimulator:

    def __init__(self, canard : Canard) -> None:
        self.__canard = canard

    @property
    def canard(self):
        return self.__canard

    def simulate(self):
        self.voler()
        self.voler()
        self.cancaner()
        self.voler()
        self.voler()
        self.voler()



if __name__ == "__main__" :

    test = Colvert("test")
    simulator = DuckSimulator.simulate(test)

