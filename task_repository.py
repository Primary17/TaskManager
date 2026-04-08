class TaskRepository:
    def __init__(self):
        self._tasks = []
        self._done = []

    def add(self, task):
        self._tasks.append(task)
        return len(self._tasks) - 1

    def remove(self, index: int):
        if 0 <= index < len(self._tasks):
            return self._tasks.pop(index)
        raise IndexError("Task index out of range")

    def complete(self, index: int):
        if 0 <= index < len(self._tasks):
            task = self._tasks.pop(index)
            self._done.append(task)
            return len(self._done) - 1
        raise IndexError("Task index out of range")

    def get_all(self, sort_key=None):
        if sort_key:
            return sorted(self._tasks, key=sort_key)
        return self._tasks

    def get_done(self, sort_key=None):
        if sort_key:
            return sorted(self._done, key=sort_key)
        return self._done

    def get_original_index(self, task):
        if task in self._tasks:
            return self._tasks.index(task)
        elif task in self._done:
            return f"DONE-{self._done.index(task)}"
        raise ValueError("Task not found in repository")