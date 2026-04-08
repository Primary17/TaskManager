from task import Task
from task_ui import TaskUI
from task_repository import TaskRepository

class TaskManager:
    def __init__(self, repository: TaskRepository, ui: TaskUI):
        self.repo = repository
        self.ui = ui

    def create_task(self):
        try:
            data = self.ui.get_task_input()
            task = Task(*data)
            task_id = self.repo.add(task)
            self.ui.display_message(f"Task created with index: {task_id}")
        except Exception as e:
            self.ui.display_error(e)

    def delete_task(self):
        try:
            idx = int(input("Enter index to delete: "))
            self.repo.remove(idx)
            self.ui.display_message("Task deleted successfully.")
        except (ValueError, IndexError) as e:
            self.ui.display_error(e)

    def show_tasks(self):
        sort_choice = input("Sort by (priority/created_at): ").strip()
        
        strategies = {
            "priority": lambda t: t.priority,
            "created_at": lambda t: t.created_at
        }
        
        try:
            key = strategies.get(sort_choice)
            if sort_choice and not key:
                raise ValueError("Invalid sorting type")
                
            tasks = self.repo.get_all(sort_key=key)
            self.ui.render_tasks(tasks, self.repo)
        except Exception as e:
            self.ui.display_error(e)