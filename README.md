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
