from typing import List
from src.todo_item import TodoItem

class TodoList:
    def __init__(self):
        self.items: List[TodoItem] = []

    def add_item(self, description: str):
        """Add a new todo item to the list."""
        item = TodoItem(description)
        self.items.append(item)

    def mark_item_completed(self, index: int):
        """Mark a specific todo item as completed by its index."""
        if 0 <= index < len(self.items):
            self.items[index].mark_completed()

    def get_items(self) -> List[TodoItem]:
        """Get the list of todo items."""
        return self.items