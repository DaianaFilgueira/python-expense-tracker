import csv

FILE_NAME = "expenses.csv"


def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

    print("Expense added.")


def show_summary():
    totals = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                category, amount = row
                amount = float(amount)

                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

    except FileNotFoundError:
        print("No expenses recorded yet.")
        return

    print("\nExpense Summary:")
    for category, total in totals.items():
        print(f"{category}: ${total}")


def main():
    while True:
        print("\n1. Add expense")
        print("2. Show summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_summary()

        elif choice == "3":
            break

        else:
            print("Invalid option.")


main()
