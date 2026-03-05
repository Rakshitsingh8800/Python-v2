class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task Removed!")
        else:
            print("Task not found!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks: ")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

todo = TodoList()
while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show tasks")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.add_task(task)

    elif choice == "2":
        task = input("Enter task to remove: ")
        todo.remove_task(task)

    elif choice == "3":
        todo.show_tasks()

    elif choice == "4":
        break