# Fauzil's Santri Management System
# A simple Python CLI application to manage santri data
# Features: Add, View, Search, Delete, JSON storage

import json

student_list = []

# Load data from file
def load_data():
    global student_list
    try:
        with open("students.json", "r") as file:
            student_list = json.load(file)
    except:
        student_list = []

# Save data to file
def save_data():
    with open("students.json", "w") as file:
        json.dump(student_list, file)

# Display menu
def show_menu():
    print("\n==============================")
    print(" Fauzil's Santri Management System ")
    print("==============================")
    print("1. Add Santri")
    print("2. View All Santri")
    print("3. Search Santri")
    print("4. Delete Santri")
    print("5. Exit")

# Load existing data
load_data()

print("Welcome to Fauzil's Santri Management System!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    # Add santri
    if choice == "1":
        name = input("Enter santri name: ")
        room = input("Enter room/block: ")

        student = {
            "name": name,
            "room": room
        }

        student_list.append(student)
        save_data()
        print("Santri added successfully!")

    # View all santri
    elif choice == "2":
        if len(student_list) == 0:
            print("No data available.")
        else:
            print("\nSantri List:")
            for i, student in enumerate(student_list, start=1):
                print(f"{i}. {student['name']} - Room: {student['room']}")

    # Search santri
    elif choice == "3":
        keyword = input("Enter name to search: ")
        found = False

        for student in student_list:
            if keyword.lower() in student["name"].lower():
                print(f"Found: {student['name']} - Room: {student['room']}")
                found = True

        if not found:
            print("Santri not found.")

    # Delete santri
    elif choice == "4":
        name = input("Enter santri name to delete: ")

        for student in student_list:
            if student["name"] == name:
                student_list.remove(student)
                save_data()
                print("Santri deleted successfully.")
                break
        else:
            print("Santri not found.")

    # Exit
    elif choice == "5":
        print("Program terminated. Thank you for using Fauzil's System!")
        break

    else:
        print("Invalid choice. Please try again.")