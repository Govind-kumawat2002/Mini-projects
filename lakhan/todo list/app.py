# A simple to-do list application

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return
    try:
        task_number = int(input("Enter the task number you want to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
