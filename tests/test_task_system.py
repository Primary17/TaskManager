import pytest
import json
from datetime import datetime
from task import Task
from task_repository import TaskRepository
from task_manager import TaskManager
from task_ui import TaskUI

# === Task ===

def test_task_creation_valid():
    task = Task("Buy", "2 loaves of bred, a bottle of milk", 3)
    assert task.title == "Buy"
    assert task.description == "2 loaves of bred, a bottle of milk"
    assert task.priority == 3
    assert isinstance(task.created_at, datetime)

def test_task_invalid_priority_raises():
    with pytest.raises(ValueError, match="Unknown task priority value"):
        Task("Invalid", "test", 0)
    with pytest.raises(ValueError, match="Unknown task priority value"):
        Task("Invalid", "test", 6)

@pytest.mark.parametrize("priority, expected", [
    (1, 1),
    (3, 3),
    (5, 5),
])
def test_task_priority_range(priority, expected):
    task = Task("Test", "desc", priority)
    assert task.priority == expected


def test_task_to_dict_and_from_dict():
    original = Task("Meeting", "Discuss project", 4)
    data = original.to_dict()
    
    assert data["title"] == "Meeting"
    assert data["priority"] == 4
    assert "created_at" in data
    
    restored = Task.from_dict(data)
    assert restored.title == original.title
    assert restored.priority == original.priority
    assert restored.created_at.isoformat() == original.created_at.isoformat()

# === TaskRepository ===

@pytest.fixture
def repo(tmp_path):
    file_path = tmp_path / "test_tasks.json"
    return TaskRepository(filename=str(file_path))


def test_repository_add_and_get_all(repo):
    task1 = Task("Task 1", "desc1", 2)
    task2 = Task("Task 2", "desc2", 5)
    
    repo.add(task1)
    repo.add(task2)
    
    tasks = repo.get_all()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_repository_complete_task(repo):
    task = Task("Do homework", "math", 3)
    repo.add(task)
    
    assert len(repo.get_all()) == 1
    assert len(repo.get_done()) == 0
    
    repo.complete(0)
    
    assert len(repo.get_all()) == 0
    assert len(repo.get_done()) == 1
    assert repo.get_done()[0].title == "Do homework"


@pytest.mark.parametrize("sort_by, expected_order", [
    ("priority", [1, 5]),
    ("created_at", None),
    ("", None),
])
def test_repository_sorting(repo, sort_by, expected_order):
    repo.add(Task("Low", "desc", 1))
    repo.add(Task("High", "desc", 5))
    
    if sort_by:
        tasks = repo.get_all(sort_key=lambda t: getattr(t, sort_by))
    else:
        tasks = repo.get_all()
    
    assert len(tasks) == 2
    if expected_order:
        priorities = [t.priority for t in tasks]
        assert priorities == expected_order


def test_repository_save_and_load(tmp_path):
    file_path = tmp_path / "tasks.json"
    repo1 = TaskRepository(filename=str(file_path))
    
    repo1.add(Task("Persistent task", "should survive", 4))
    repo1.complete(0)
    
    repo2 = TaskRepository(filename=str(file_path))
    
    assert len(repo2.get_all()) == 0
    assert len(repo2.get_done()) == 1
    assert repo2.get_done()[0].title == "Persistent task"


# === TaskManager ===

@pytest.fixture
def manager(repo):
    ui = TaskUI()
    return TaskManager(repo, ui)


def test_manager_create_task(manager, repo):
    task = Task("Test create", "via manager", 2)
    
    initial_count = len(repo.get_all())
    repo.add(Task("Manager test", "desc", 3))
    assert len(repo.get_all()) == initial_count + 1


@pytest.mark.parametrize("bad_index, expected_exception", [
    (-1, IndexError),
    (999, IndexError),
    ("abc", ValueError),
])
def test_repository_invalid_index(repo, bad_index, expected_exception):
    repo.add(Task("Valid", "desc", 3))
    
    with pytest.raises(expected_exception):
        repo.remove(bad_index)
    
    with pytest.raises(expected_exception):
        repo.complete(bad_index)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])