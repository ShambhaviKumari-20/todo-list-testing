import pytest
from todo_list import ToDoList

@pytest.fixture
def todo():
    return ToDoList()

def test_add_task(todo):
    assert todo.add_task("Read a book") == "Task 'Read a book' added."
    assert "Read a book" in todo.list_tasks()

def test_add_empty_task(todo):
    with pytest.raises(ValueError, match="Task cannot be empty."):
        todo.add_task("")

def test_add_long_task(todo):
    with pytest.raises(ValueError, match="Task name is too long."):
        todo.add_task("A" * 101)

def test_update_task(todo):
    todo.add_task("Buy milk")
    assert todo.update_task(0, "Buy almond milk") == "Task at index 0 updated to 'Buy almond milk'."

def test_delete_task(todo):
    todo.add_task("Clean the house")
    assert todo.delete_task(0) == "Task 'Clean the house' deleted."

