class TaskRepository:
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)
        return len(self._tasks) - 1

    def remove(self, index: int):
        if 0 <= index < len(self._tasks):
            return self._tasks.pop(index)
        raise IndexError("Task index out of range")

    def get_all(self, sort_key=None):
        if sort_key:
            return sorted(self._tasks, key=sort_key)
        return self._tasks

    def get_original_index(self, task):
        return self._tasks.index(task)