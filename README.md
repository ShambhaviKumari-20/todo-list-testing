To-Do List Application Testing
This is a simple Python-based To-Do List application with both manual and automated testing. The app allows you to add, update, delete, and list tasks. It has basic functionality and validates inputs, ensuring that tasks cannot be empty or too long.

Project Overview
The To-Do List application has the following key features:

Add Tasks: Add new tasks to the list.
Update Tasks: Edit an existing task.
Delete Tasks: Remove tasks from the list.
List Tasks: View the current list of tasks.
The project also includes testing scripts to ensure that the application works as expected.

Features
Input Validation: Ensures that empty tasks or tasks longer than 100 characters are not added.
Task Management: Provides functionality to add, update, and delete tasks by their index.
Testing: Both manual and automated tests are included to verify the app’s functionality.
Manual Testing
Manual tests ensure that the app’s features behave as expected. The following test cases were created:

Add Task
Add a valid task: The task should be successfully added.
Add an empty task: An error message should appear saying, "Task cannot be empty."
Add a very long task: An error message should appear saying, "Task name is too long."
Update Task
Update an existing task: The task should be updated successfully.
Update with an invalid index: An error message should appear saying, "Task index out of range."
Update with an empty task: An error message should appear saying, "Task cannot be empty."
Delete Task
Delete an existing task: The task should be deleted successfully.
Delete with an invalid index: An error message should appear saying, "Task index out of range."
List Tasks
List tasks after adding: The tasks should appear in the list.
List tasks after deletion: The updated list should display after deleting a task.
Automated Testing
Automated tests using pytest are included to verify the functionality of the application. These tests:

Ensure tasks can be added, updated, and deleted.
Validate input constraints (empty tasks, long tasks).
Test edge cases such as invalid task indices.
To run the automated tests, simply use the following command:

bash
Copy code
pytest test_todo_list.py
Getting Started
Prerequisites
Ensure that you have Python 3 installed on your machine. You will also need to install pytest for automated testing.

You can install the required dependencies by running:

bash
Copy code
pip3 install pytest
Running the Application
To run the application manually, you can import and test the ToDoList class in a Python interpreter.

Running Tests
Manual Tests: Refer to the test cases in the manual_test_cases.md file for step-by-step instructions.
Automated Tests: Run the tests using pytest:
bash
Copy code
pytest test_todo_list.py
Moving Files
To bring the files to your Desktop, simply use the mv command in Terminal:

bash
Copy code
mv todo_list.py manual_test_cases.md test_todo_list.py ~/Desktop/
File Structure
bash
Copy code
├── todo_list.py              # The application logic
├── manual_test_cases.md      # Manual test case documentation
├── test_todo_list.py         # Automated test cases using pytest
└── README.md                 # Project documentation
Conclusion
This project is a simple demonstration of how to build a To-Do List application with basic functionality and tests. It serves as a learning tool to practice Python, basic software engineering principles, and automated testing using pytest.
