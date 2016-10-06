from Prac8.Taxi import Taxi
from Prac8.Taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose Taxi, d)rive"


def main():
    bill_to_date = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets Drive")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print_list(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            print("Bill to Date: ${:.2f}".format(bill_to_date))
        elif choice == 'd':
            distance = int(input("Drive how far? "))
            bill_to_date += trip_cost(distance, taxi_choice, taxis)
            print("Bill to Date: ${:.2f}".format(bill_to_date))
        else:
            print('Invalid Menu Choice')
        print(MENU)
        choice = input(">>> ").lower()
    print("Total Trip Cost: ${:.2f}".format(bill_to_date))
    print_list(taxis)


def print_list(taxis):
    print("Taxis Available")
    count = 0
    for item in taxis:
        print("{} - {}".format(count, item))
        count += 1


def trip_cost(distance, taxi_choice, taxis):
    count = 0
    for item in taxis:
        if count == taxi_choice:
            item.start_fare()
            item.drive(distance)
            cost = item.get_fare()
            print("Your {} trip cost you ${}".format(item.name, cost))
            return cost
        else:
            count += 1

main()