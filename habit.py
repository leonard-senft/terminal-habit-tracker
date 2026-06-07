import json
from datetime import date

today = str(date.today())


def main():
    habits = load_data()
    while True:
        print("\n---   HABIT TRACKER ---")
        print("1. Add habit")
        print("2. Mark done")
        print("3. Show habits")
        print("4. Delete habit")
        print("5. Exit")

        choice=input("Choose an option 1-5! ").strip()

        if choice == "1":
            add_habit(habits)

        elif choice == "2":
            mark_done(habits)

        elif choice == "3":
            show_habits(habits)

        elif choice == "4":
            delete_habit(habits)

        elif choice=="5":
            print("Goodbye!")
            break

        else:
            print("Invalid input, try again!")


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(habits):
    with open("data.json", "w") as file:
        json.dump(habits, file, indent=4)


def add_habit(habits):
    habit=input("Enter habit: ").strip()
    if not habit:
        print("Habit name cannot be empty!")
        return

    if habit not in habits:
        habits[habit] = []
        print(f"Habit '{habit}' added successfully!")
        save_data(habits)
    else:
        print("This habit already exists!")

def mark_done(habits):
    if not habits:
        print("You have not created any habits yet!")
        return

    print("Your habits:", ", ".join(habits.keys()))

    choice_1=input("Which habit do you want to mark done?").strip()

    if choice_1 in habits:
        if today not in habits[choice_1]:
            habits[choice_1].append(today)
            print(f"{choice_1} has been successfully marked done for today!")
            save_data(habits)
        else:
            print(f"{choice_1} has already been marked done today!")
    else:
        print("This habit has not been found!")

def show_habits(habits):
    if not habits:
        print("No habits found. Add some first!")
        return
    print("\n---YOUR HABITS ---")
    for habit, dates in habits.items():
        print(f"- {habit}: {len(dates)} times done (Dates: {', '.join(dates)})")

def delete_habit(habits):
    if not habits:
        print("No habits found. Add some first!")
        return
    print("\n---YOUR HABITS ---")
    print("Your habits:", ", ".join(habits.keys()))
    choice = input("Which habit do you want to delete? ").strip()
    if choice in habits:
        del habits[choice]
        print(f"{choice} has been successfully deleted!")
        save_data(habits)

    else:
        print("This habit has not been found! To create one, go to 'Add habit'.")

if __name__=="__main__":
    main()
