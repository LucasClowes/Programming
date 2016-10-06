from Prac8.Taxi import UnreliableCar
from Prac8.Taxi import Taxi
from Prac8.Taxi import SilverServiceTaxi

def main():
    taxi = Taxi("Prius", 100)
    taxi.start_fare()
    taxi.drive(40)
    print(taxi)
    print("Current Fare ${:.2f}".format(taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Current Fare ${:.2f}".format(taxi.get_fare()))

    unreliablecar = UnreliableCar('Ford', 100, 40)
    unreliablecar.drive(40)
    print(unreliablecar)

    silverservicetaxi = SilverServiceTaxi('Hummer', 200, 2)
    silverservicetaxi.start_fare()
    silverservicetaxi.drive(10)
    print(silverservicetaxi)
    print("Current Fare ${:.2f}".format(silverservicetaxi.get_fare()))
main()
