import pandas as pd

lost_file = "lost_items.csv"
found_file = "found_items.csv"

# Create files if they don't exist
def initialize_files():
    try:
        pd.read_csv(lost_file)
    except:
        pd.DataFrame(columns=["description","location","date","matricula"]).to_csv(lost_file, index=False)

    try:
        pd.read_csv(found_file)
    except:
        pd.DataFrame(columns=["description","location","date"]).to_csv(found_file, index=False)

def register_lost():
    description = input("Item description: ")
    location = input("Where was it lost?: ")
    date = input("Date: ")
    matricula = input("Student ID: ")

    df = pd.read_csv(lost_file)
    new_item = pd.DataFrame([[description, location, date, matricula]],
                            columns=df.columns)

    df = pd.concat([df,new_item], ignore_index=True)
    df.to_csv(lost_file, index=False)

    print("Lost item registered!")

def register_found():
    description = input("Item description: ")
    location = input("Where was it found?: ")
    date = input("Date: ")

    df = pd.read_csv(found_file)
    new_item = pd.DataFrame([[description, location, date]],
                            columns=df.columns)

    df = pd.concat([df,new_item], ignore_index=True)
    df.to_csv(found_file, index=False)

    print("Found item registered!")

def view_items():
    print("\nLost Items:")
    print(pd.read_csv(lost_file))

    print("\nFound Items:")
    print(pd.read_csv(found_file))

def match_items():
    lost = pd.read_csv(lost_file)
    found = pd.read_csv(found_file)

    for l in lost["description"]:
        for f in found["description"]:
            if l.lower() in f.lower() or f.lower() in l.lower():
                print("Possible match:", l, "<->", f)

def menu():
    while True:
        print("\n--- Lost & Found Tracker ---")
        print("1. Register Lost Item")
        print("2. Register Found Item")
        print("3. View Items")
        print("4. Match Items")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_lost()

        elif choice == "2":
            register_found()

        elif choice == "3":
            view_items()

        elif choice == "4":
            match_items()

        elif choice == "5":
            break

        else:
            print("Invalid option")

initialize_files()
menu()