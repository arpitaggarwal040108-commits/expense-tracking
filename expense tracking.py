def add_expense():
    print("\n" + "=" * 50)
    print("              ADD EXPENSE")
    print("=" * 50)
    date = input("Enter Date (DD/MM/YY): ")
    amount = input("Enter Amount: ₹")
    print("\nCategories:")
    print("1. Food")
    print("2. Transport")
    print("3. Entertainment")
    print("4. Others")

    category_choice = input("\nChoose Category (1-4): ")
    match category_choice:
        case "1":
            category = "Food"
        case "2":
            category = "Transport"
        case "3":
            category = "Entertainment"
        case "4":
            category = "Others"
        case _:
            print("Invalid Category!")
            return

    choice_for_note = input("Do you want to add a note? (y/n): ")
    if choice_for_note.lower() == "y":
        note = input("Enter Note: ")
    else:
        note = "N/A"

    with open("data.txt", "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")
    print("\n✓ Expense Added Successfully!")

def view_all_expenses():
    total = 0
    count = 0
    try:
        with open("data.txt", "r") as file:
            print("\n" + "=" * 70)
            print(" " * 26 + "ALL EXPENSES")
            print("=" * 70)
            print(
                f"{'Date':<15}{'Category':<18}{'Amount':<12}{'Note'}"
            )
            print("-" * 70)
            for line in file:
                date, category, amount, note = line.strip().split(",")
                print(
                    f"{date:<15}{category:<18}{amount:<12}{note}"
                )
                total += float(amount)
                count += 1
            print("-" * 70)
            print(f"Total Expenses   : ₹{total:.2f}")
            print(f"Total Records    : {count}")
            print("=" * 70)
    except FileNotFoundError:
        print("\nNo Expense Records Found.")

def filter_by_category():
    print("\nSelect Category:")
    print("1. Food")
    print("2. Transport")
    print("3. Entertainment")
    print("4. Others")

    category_choice = input("\nChoose Category (1-4): ")
    match category_choice:
        case "1":
            search = "Food"
        case "2":
            search = "Transport"
        case "3":
            search = "Entertainment"
        case "4":
            search = "Others"
        case _:
            print("Invalid Category!")
            return
    subtotal = 0
    found = False

    try:
        with open("data.txt", "r") as file:
            print("\n" + "=" * 70)
            print(f"EXPENSES IN CATEGORY : {search.upper()}")
            print("=" * 70)

            print(
                f"{'Date':<15}{'Category':<18}{'Amount':<12}{'Note'}"
            )

            print("-" * 70)
            for line in file:
                date, category, amount, note = line.strip().split(",")
                if category == search:
                    found = True
                    print(
                        f"{date:<15}{category:<18}{amount:<12}{note}"
                    )
                    subtotal += float(amount)
            print("-" * 70)
            if found:
                print(f"Category Total : ₹{subtotal:.2f}")
            else:
                print("No Records Found.")
            print("=" * 70)

    except FileNotFoundError:
        print("\nNo Expense Records Found.")

while True:
    print("\n" + "=" * 50)
    print("        PERSONAL EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter By Category")
    print("4. Exit")
    print("=" * 50)

    choice = input("Enter Your Choice: ")
    match choice:
        case "1":
            add_expense()
        case "2":
            view_all_expenses()
        case "3":
            filter_by_category()
        case "4":
            print("\nThank You For Using Expense Tracker!")
            break
        case _:
            print("\nInvalid Choice! Please Try Again.")



