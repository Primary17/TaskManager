from datetime import datetime

class Task:
    def __init__(self, title, description, priority, created_at=None):
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()
        if priority < 1 or priority > 5:
            raise ValueError("Unknown task priority value")
        self.priority = priority

    def __str__(self):
        return f"Title: {self.title}; description: {self.description}; created at {self.created_at}; priority: {self.priority}"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now()
        return cls(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            created_at=created_at
        )