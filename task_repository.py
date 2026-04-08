import json
from task import Task

class TaskRepository:
    def __init__(self, filename="tasks.json"):
        self._tasks = []
        self._done = []
        self.filename = filename
        self.load_from_file()
    
    def add(self, task):
        self._tasks.append(task)
        self.save_to_file()
        return len(self._tasks) - 1

    def remove(self, index: int):
        if not isinstance(index, int):
            raise ValueError(f"Index must be an integer, got {type(index).__name__}")
        if 0 <= index < len(self._tasks):
            task = self._tasks.pop(index)
            self.save_to_file()
            return task
        raise IndexError("Task index out of range")

    def complete(self, index: int):
        if not isinstance(index, int):
            raise ValueError(f"Index must be an integer, got {type(index).__name__}")
        if 0 <= index < len(self._tasks):
            task = self._tasks.pop(index)
            self._done.append(task)
            self.save_to_file()
            return len(self._done) - 1
        raise IndexError("Task index out of range")

    def get_all(self, sort_key=None):
        if sort_key:
            return sorted(self._tasks, key=sort_key)
        return self._tasks[: ]

    def get_done(self, sort_key=None):
        if sort_key:
            return sorted(self._done, key=sort_key)
        return self._done[: ]

    def get_original_index(self, task):
        if task in self._tasks:
            return self._tasks.index(task)
        elif task in self._done:
            return f"DONE-{self._done.index(task)}"
        raise ValueError("Task not found")

    def save_to_file(self):
        try:
            data = {
                "active": [task.to_dict() for task in self._tasks],
                "done": [task.to_dict() for task in self._done]
            }
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Warning: Could not save to file: {e}")

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self._tasks = [Task.from_dict(t) for t in data.get("active", [])]
            self._done = [Task.from_dict(t) for t in data.get("done", [])]
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Could not load from file: {e}")
            self._tasks = []
            self._done = []