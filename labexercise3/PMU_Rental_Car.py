# IFA SHAFIKA BINTI KEMRI
#20DDT21F1027
CAR_LIST_FILE = r"C:\\Users\ikaa\Desktop\PYTHON\labexercise3\CarList.txt"
CUSTOMER_RENTAL_RECORDS_FILE = r"C:\\Users\ikaa\Desktop\PYTHON\labexercise3\customerrentalrecords.txt"

def display_packages():
    try:
        with open(CAR_LIST_FILE, "r") as file:
            packages = file.readlines()
            for package in packages:
                print(package.strip())
    except FileNotFoundError:
        print("Error: CarList.txt file not found.")

def calculate_total_price(car_selection, duration):
    # TO DO: implement total price calculation logic
    # For now, assume a fixed price per day
    daily_rate = 170.00
    total_price = daily_rate * int(duration)
    return total_price

def insert_new_order():
    customer_name = input("Enter customer name: ")
    customer_ic_no = input("Enter customer IC No: ")
    customer_phone_number = input("Enter customer phone number: ")
    car_selection = input("Enter car selection (from CarList.txt): ")
    duration = input("Enter duration: ")

    total_price = calculate_total_price(car_selection, duration)

    try:
        with open(CUSTOMER_RENTAL_RECORDS_FILE, "a") as file:
            file.write(f"{customer_name},{customer_ic_no},{customer_phone_number},{car_selection},{duration},{total_price:.2f}\n")
    except FileNotFoundError:
        print("Error: customerrentalrecords.txt file not found.")

    print("")
    print("Order inserted successfully!")
    print("")
    print(f"Customer Name: {customer_name}")
    print(f"Customer IC No: {customer_ic_no}")
    print(f"Customer Phone Number: {customer_phone_number}")
    print(f"Car Selection: {car_selection}")
    print(f"Duration: {duration} days")
    print(f"Total Price: RM {total_price:.2f}")
    print("")
    print("Customer rental has been record. Thank You!")
    print("")
def main():
    while True:
        print("PMU Rental Car System")
        print("1. Display packages")
        print("2. Insert new order")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_packages()
        elif choice == "2":
            insert_new_order()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()