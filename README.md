A short video showing the prototype in action is provided: https://drive.google.com/file/d/12Fx1kp2AsuQkQ0iB52BA4xuIlW9dUWXZ/view?usp=sharing

Project Description

This project is a basic Lost & Found Tracker developed in Python, designed to help students report and recover lost items within a school environment. The system uses CSV files to store information about lost and found objects, making it simple to organize and access data.

Users can input item descriptions, locations, and dates, and in the case of lost items, the student ID (matrícula). Additionally, the program includes a matching feature that compares the descriptions of lost and found items to identify possible matches, helping users recover their belongings more efficiently.

# Lost-Found-Item-Tracker
“The Lost &amp; Found Item Tracker is a simple digital system that helps students and staff record lost and found items at school. It organizes item descriptions and locations, making it easier to match lost items with found ones and return them to their owners.”


Instructions on How to Run the Code

To run this program, follow these steps:

Make sure you have Python (version 3 or higher) installed.

Install the required library by running:

pip install pandas

Copy the code into a file with a .py extension, for example:

    lost_found_tracker.py

Run the program in your terminal or command prompt:

    python lost_found_tracker.py

Once executed, a menu will appear where you can:

Register lost items

Register found items

View all items

Match items

The program will automatically generate two files:
    
    lost_items.csv
    
    found_items.csv


Implemented Features

The project includes the following main features:

Automatic file initialization: Creates CSV files if they do not exist.

Lost item registration: Stores description, location, date, and student ID.

Found item registration: Stores description, location, and date.

Data visualization: Displays all recorded lost and found items.

Matching system: Compares item descriptions to detect possible matches.

Interactive menu: Simple console-based interface for easy navigation.

A Brief Comment on the Project’s Initial Impact

The initial impact of this project is positive, as it provides a simple yet functional solution to a common problem in schools: lost personal items. Even though it is a basic system, it improves the organization of lost and found processes and reduces the time students spend trying to recover their belongings.

Furthermore, this project has strong potential for future development. It could be expanded into a more advanced application with a graphical user interface, automatic notifications, or integration with an online database. In its current form, it demonstrates how a simple technological tool can create a meaningful and practical impact in everyday student life.

    import pandas as pd
    
    # File names where data will be stored
    lost_file = "lost_items.csv"
    found_file = "found_items.csv"
    
    # This function ensures both CSV files exist before the program runs
    # If they don't exist, it creates them with the correct columns
    def initialize_files():
        try:
            pd.read_csv(lost_file)
        except:
            # Create a new file for lost items with required columns
            pd.DataFrame(columns=["description","location","date","matricula"]).to_csv(lost_file, index=False)

    try:
        pd.read_csv(found_file)
    except:
        # Create a new file for found items with required columns
        pd.DataFrame(columns=["description","location","date"]).to_csv(found_file, index=False)

    # This function allows the user to register a lost item
    # It collects input and saves it into the lost_items.csv file
    def register_lost():
        description = input("Item description: ")
        location = input("Where was it lost?: ")
        date = input("Date: ")
        matricula = input("Student ID: ")

    # Load existing data
    df = pd.read_csv(lost_file)

    # Create a new row with user input
    new_item = pd.DataFrame([[description, location, date, matricula]],
                            columns=df.columns)

    # Append the new row to the existing data
    df = pd.concat([df,new_item], ignore_index=True)

    # Save updated data back to CSV
    df.to_csv(lost_file, index=False)

    print("Lost item registered!")

    # This function allows the user to register a found item
    def register_found():
        description = input("Item description: ")
        location = input("Where was it found?: ")
        date = input("Date: ")

    # Load existing found items
    df = pd.read_csv(found_file)

    # Create new row
    new_item = pd.DataFrame([[description, location, date]],
                            columns=df.columns)

    # Append and save
    df = pd.concat([df,new_item], ignore_index=True)
    df.to_csv(found_file, index=False)

    print("Found item registered!")

    # This function displays all lost and found items
    def view_items():
        print("\nLost Items:")
        print(pd.read_csv(lost_file))

    print("\nFound Items:")
    print(pd.read_csv(found_file))

    # This function compares descriptions of lost and found items
    # It tries to find possible matches based on similar text
    def match_items():
        lost = pd.read_csv(lost_file)
        found = pd.read_csv(found_file)

    # Compare each lost item with each found item
    for l in lost["description"]:
        for f in found["description"]:
            # If one description is contained in the other (case insensitive)
            if l.lower() in f.lower() or f.lower() in l.lower():
                print("Possible match:", l, "<->", f)

    # Main menu function that controls program flow
    # It keeps running until the user chooses to exit
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

    # Initialize files before starting program
    initialize_files()

    # Start the menu system
    menu()
            else:
                print("Invalid option")
    
    initialize_files()
    menu()
