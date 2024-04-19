from Canard import Colvert,CouRouge,Canard
from Oies import CanardAdapter

class DuckSimulator:

  def simulate(canard: Canard):
     for _ in range(2):
        canard.voler()
     canard.cancaner()
     for _ in range(2):
        canard.voler()
    
  



if __name__ == "__main__" :

    simulator = DuckSimulator.simulate(Colvert("test"))
    simulator = DuckSimulator.simulate(CanardAdapter("ok"))

