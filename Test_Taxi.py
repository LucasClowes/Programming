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

    unreliable_car = UnreliableCar('Ford', 100, 40)
    unreliable_car.drive(40)
    print(unreliable_car)

    silver_service_taxi = SilverServiceTaxi('Hummer', 200, 2)
    silver_service_taxi.start_fare()
    silver_service_taxi.drive(10)
    print(silver_service_taxi)
    print("Current Fare ${:.2f}".format(silver_service_taxi.get_fare()))


main()
