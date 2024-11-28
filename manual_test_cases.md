## Manual Test Cases for To-Do List Application

### Add Task
1. Add a valid task: Should be added successfully.
2. Add an empty task: Should raise `ValueError: Task cannot be empty.`.
3. Add a very long task (> 100 characters): Should raise `ValueError: Task name is too long.`.

### Update Task
1. Update an existing task: Should update successfully.
2. Update with invalid index: Should raise `IndexError: Task index out of range.`.
3. Update with an empty task: Should raise `ValueError: Task cannot be empty.`.

### Delete Task
1. Delete an existing task: Should delete successfully.
2. Delete with invalid index: Should raise `IndexError: Task index out of range.`.

### List Tasks
1. List tasks after adding: Should display added tasks.
2. List tasks after deletion: Should display updated list.

