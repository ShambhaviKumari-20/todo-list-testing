class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task.strip():
            raise ValueError("Task cannot be empty.")
        if len(task) > 100:
            raise ValueError("Task name is too long.")
        self.tasks.append(task)
        return f"Task '{task}' added."

    def update_task(self, index, new_task):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Task index out of range.")
        if not new_task.strip():
            raise ValueError("Task cannot be empty.")
        self.tasks[index] = new_task
        return f"Task at index {index} updated to '{new_task}'."

    def delete_task(self, index):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Task index out of range.")
        removed_task = self.tasks.pop(index)
        return f"Task '{removed_task}' deleted."

    def list_tasks(self):
        return self.tasks

