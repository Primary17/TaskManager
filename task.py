from datetime import datetime

class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        if priority < 1 or priority > 5:
            raise ValueError("Unknown task priority value")
        self.priority = priority

    def __str__(self):
        return f"Title: {self.title}; description: {self.description}; created at {self.created_at}; priority: {self.priority}"