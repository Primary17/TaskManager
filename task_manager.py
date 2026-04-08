from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = list()

    def add_task(self):
        title = input("Enter task title:")
        description = input("Descript task:")
        priority = input("Enter task priority (in range from 1 to 5):")
        try:
            task = Task(title, description, priority)
        except ex:
            print(f"Failed to create task: '{ex}'.")
        else:
            self.tasks.append(task)
            task_id = self.tasks.index(task)
            print("The task succesful was created.")
            print(f"Index of the created task: {task_id}.")

    def delete_task(self):
        task_id = input("Enter index of the task, that should be deleted:")
        try:
            self.tasks.pop(task_id)
        except ex:
            print("Failed to create task: '{ex}'.")
        else:
            print("The task succesful was deleted.")

    def get_tasks(self, sorted_by="priority"):
        if sorted_by == "priority":
            sorted_tasks = sorted(self.tasks, key=lambda t: t.priority)
        elif sorted_by == "created_at":
            sorted_tasks = sorted(self.tasks, key=lambda t: t.created_at)
        else:
            raise ValueError("Unknown tasks sorting type")
        for task in sorted_taskstasks:
            yield (f"{task}; index: {self.tasks.index(task)}")

    def print_tasks():
        sorting_type = input("Choose between 'priority' and 'created_ad' task sorting:")
        try:
            task_list = self.get_tasks(sorted_by=sorting_type)
            for task in task_list:
                print(task)
        except ex:
            print(f"Failed to print task list: {ex}.")