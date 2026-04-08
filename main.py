from task_manager import TaskManager
from task_repository import TaskRepository
from task_ui import TaskUI

def main():
    repo = TaskRepository()
    ui = TaskUI()
    manager = TaskManager(repo, ui)

    actions = {
        "1": manager.create_task,
        "2": manager.delete_task,
        "3": manager.show_tasks,
        "4": manager.mark_task_as_done,
        "5": manager.show_completed_tasks,
        "6": exit
    }

    while True:
        print("--- MENU ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Mark Task As Done")
        print("5. Show Completed Tasks")
        print("6. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            ui.display_message("Invalid choice, please try again.")

if __name__ == "__main__":
    main()