class TaskUI:
    @staticmethod
    def get_task_input():
        title = input("Enter task title: ")
        description = input("Describe task: ")
        priority = int(input("Enter task priority (1-5): "))
        return title, description, priority

    @staticmethod
    def display_error(error: Exception):
        print(f"Action failed: {error}")

    def render_tasks(self, tasks, repository):
        print("--- TASK LIST ---")
        for task in tasks:
            idx = repository.get_original_index(task)
            print(f"ID: {idx} | {task}")