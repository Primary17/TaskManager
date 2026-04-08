class TaskUI:
    def get_task_input(self):
        title = input("Enter task title: ")
        description = input("Describe task: ")
        try:
            priority = int(input("Enter task priority (1-5): "))
        except ValueError:
            priority = 3
            print("Incorrect priority value, set 3 by default")
        return title, description, priority

    def display_message(self, message: str):
        print(f"{message}")

    def display_error(self, error):
        print(f"Action failed: {error}")

    def render_tasks(self, tasks, repository, done=False):
        if done == False:
            print("--- TASK LIST ---")
        else:
            print("--- COMPLETED TASKS ---")
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            idx = repository.get_original_index(task)
            print(f"ID: {idx} | {task}")