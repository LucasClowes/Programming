from Prac8.Taxi import Taxi
from Prac8.Taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose Taxi, d)rive"


def main():
    bill_to_date = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print_list(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            print("Bill to Date: ${:.2f}".format(bill_to_date))
        elif choice == 'd':
            distance = int(input("Drive how far? "))
            taxi = taxis[taxi_choice]
            bill_to_date += calculate_trip_cost(distance, taxi_choice, taxis)
            print("Bill to Date: ${:.2f}".format(bill_to_date))
        else:
            print('Invalid Menu Choice')
        print(MENU)
        choice = input(">>> ").lower()
    print("Total Trip Cost: ${:.2f}".format(bill_to_date))
    print_list(taxis)


def print_list(taxis):
    print("Taxis Available")
    for count, taxi in enumerate(taxis):
        print("{} - {}".format(count, taxi))


def calculate_trip_cost(distance, taxi_choice, taxis):
    taxi = taxis[taxi_choice]
    taxi.start_fare()
    taxi.drive(distance)
    cost = taxi.get_fare()
    print("Your {} trip cost you ${}".format(taxi.name, cost))
    return cost

main()
