from src.todo_list import TodoList

class TodoApp:
    def __init__(self):
        self.todo_list = TodoList()

    def run(self):
        """Run the main loop of the todo application."""
        while True:
            print("\nTodo List:")
            for idx, item in enumerate(self.todo_list.get_items()):
                status = "Done" if item.completed else "Pending"
                print(f"{idx + 1}. {item.description} [{status}]")

            print("\nOptions:")
            print("1. Add a new todo item")
            print("2. Mark a todo item as completed")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                description = input("Enter the description of the new todo item: ")
                self.todo_list.add_item(description)
            elif choice == "2":
                index = int(input("Enter the number of the todo item to mark as completed: ")) - 1
                self.todo_list.mark_item_completed(index)
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")