from dataclasses import dataclass

@dataclass
class TodoItem:
    description: str
    completed: bool = False

    def mark_completed(self):
        """Mark the todo item as completed."""
        self.completed = True