import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import re


class Priority(Enum):
    """Task priority levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class Status(Enum):
    """Task status states."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"


@dataclass
class Task:
    """Represents a task with all its attributes."""
    id: str
    title: str
    description: str
    priority: Priority
    status: Status
    created_at: str
    due_date: Optional[str] = None
    completed_at: Optional[str] = None
    tags: Set[str] = field(default_factory=set)
    subtasks: List['Task'] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    assigned_to: Optional[str] = None
    estimated_hours: float = 0.0
    actual_hours: float = 0.0
    comments: List[Dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "completed_at": self.completed_at,
            "tags": list(self.tags),
            "subtasks": [s.to_dict() for s in self.subtasks],
            "dependencies": self.dependencies,
            "assigned_to": self.assigned_to,
            "estimated_hours": self.estimated_hours,
            "actual_hours": self.actual_hours,
            "comments": self.comments
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a Task instance from dictionary data."""
        task = cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            priority=Priority(data["priority"]),
            status=Status(data["status"]),
            created_at=data["created_at"],
            due_date=data.get("due_date"),
            completed_at=data.get("completed_at"),
            tags=set(data.get("tags", [])),
            assigned_to=data.get("assigned_to"),
            estimated_hours=data.get("estimated_hours", 0.0),
            actual_hours=data.get("actual_hours", 0.0)
        )
        task.subtasks = [cls.from_dict(st) for st in data.get("subtasks", [])]
        task.dependencies = data.get("dependencies", [])
        task.comments = data.get("comments", [])
        return task

    def add_subtask(self, subtask: 'Task') -> None:
        """Add a subtask to this task."""
        self.subtasks.append(subtask)

    def add_comment(self, user: str, comment: str) -> None:
        """Add a comment to the task."""
        self.comments.append({
            "user": user,
            "comment": comment,
            "timestamp": datetime.now().isoformat()
        })

    def complete(self) -> None:
        """Mark task as completed."""
        self.status = Status.COMPLETED
        self.completed_at = datetime.now().isoformat()
        # Auto-complete all subtasks
        for subtask in self.subtasks:
            if subtask.status != Status.COMPLETED:
                subtask.complete()

    def is_overdue(self) -> bool:
        """Check if task is overdue."""
        if not self.due_date or self.status == Status.COMPLETED:
            return False
        due = datetime.fromisoformat(self.due_date)
        return datetime.now() > due


class TaskManager:
    """Manages tasks with advanced features."""

    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: Dict[str, Task] = {}
        self.load_data()
        self._id_counter = max([int(t.id.split('-')[1]) for t in self.tasks.values()] + [0])

    def _generate_id(self) -> str:
        """Generate a unique task ID."""
        self._id_counter += 1
        return f"TASK-{self._id_counter:04d}"

    def create_task(self, title: str, description: str, priority: Priority = Priority.MEDIUM,
                   due_date: Optional[str] = None, tags: Optional[List[str]] = None,
                   assigned_to: Optional[str] = None, estimated_hours: float = 0.0) -> Task:
        """Create a new task."""
        task = Task(
            id=self._generate_id(),
            title=title,
            description=description,
            priority=priority,
            status=Status.PENDING,
            created_at=datetime.now().isoformat(),
            due_date=due_date,
            tags=set(tags) if tags else set(),
            assigned_to=assigned_to,
            estimated_hours=estimated_hours
        )
        self.tasks[task.id] = task
        self.save_data()
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieve a task by ID."""
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, **kwargs) -> bool:
        """Update task attributes."""
        task = self.get_task(task_id)
        if not task:
            return False
        for key, value in kwargs.items():
            if hasattr(task, key) and key not in ['id', 'created_at', 'subtasks']:
                if key == 'priority' and isinstance(value, int):
                    setattr(task, key, Priority(value))
                elif key == 'status' and isinstance(value, str):
                    setattr(task, key, Status(value))
                else:
                    setattr(task, key, value)
        self.save_data()
        return True

    def delete_task(self, task_id: str, archive: bool = False) -> bool:
        """Delete or archive a task."""
        task = self.get_task(task_id)
        if not task:
            return False
        if archive:
            task.status = Status.ARCHIVED
            self.save_data()
        else:
            # Remove dependencies from other tasks
            for t in self.tasks.values():
                if task_id in t.dependencies:
                    t.dependencies.remove(task_id)
            del self.tasks[task_id]
            self.save_data()
        return True

    def filter_tasks(self, status: Optional[Status] = None, 
                    priority: Optional[Priority] = None,
                    tag: Optional[str] = None,
                    assigned_to: Optional[str] = None,
                    overdue_only: bool = False) -> List[Task]:
        """Filter tasks by various criteria."""
        result = list(self.tasks.values())
        if status:
            result = [t for t in result if t.status == status]
        if priority:
            result = [t for t in result if t.priority == priority]
        if tag:
            result = [t for t in result if tag in t.tags]
        if assigned_to:
            result = [t for t in result if t.assigned_to == assigned_to]
        if overdue_only:
            result = [t for t in result if t.is_overdue()]
        return result

    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title, description, or tags."""
        query = query.lower()
        results = []
        for task in self.tasks.values():
            if (query in task.title.lower() or 
                query in task.description.lower() or
                any(query in tag.lower() for tag in task.tags)):
                results.append(task)
        return results

    def get_task_statistics(self) -> Dict:
        """Get statistics about all tasks."""
        total = len(self.tasks)
        by_status = defaultdict(int)
        by_priority = defaultdict(int)
        overdue = 0
        total_estimated = 0
        total_actual = 0

        for task in self.tasks.values():
            by_status[task.status.value] += 1
            by_priority[task.priority.name] += 1
            if task.is_overdue():
                overdue += 1
            total_estimated += task.estimated_hours
            total_actual += task.actual_hours

        return {
            "total_tasks": total,
            "by_status": dict(by_status),
            "by_priority": dict(by_priority),
            "overdue_tasks": overdue,
            "total_estimated_hours": total_estimated,
            "total_actual_hours": total_actual,
            "completion_rate": (by_status.get("completed", 0) / total * 100) if total > 0 else 0
        }

    def save_data(self) -> None:
        """Save tasks to JSON file."""
        try:
            data = [task.to_dict() for task in self.tasks.values()]
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        """Load tasks from JSON file."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            for item in data:
                task = Task.from_dict(item)
                self.tasks[task.id] = task
        except Exception as e:
            print(f"Error loading data: {e}")


def display_tasks(tasks: List[Task], title: str = "Tasks") -> None:
    """Display tasks in a formatted table."""
    if not tasks:
        print(f"\nNo {title.lower()} found.")
        return
    
    print(f"\n{'='*80}")
    print(f"{title.upper()}")
    print(f"{'='*80}")
    print(f"{'ID':<12} {'Title':<25} {'Priority':<10} {'Status':<15} {'Due Date':<15}")
    print(f"{'-'*80}")
    for task in tasks:
        due = task.due_date[:10] if task.due_date else "N/A"
        print(f"{task.id:<12} {task.title[:24]:<25} {task.priority.name:<10} "
              f"{task.status.value:<15} {due:<15}")
    print(f"{'='*80}\n")


def main():
    """Main program loop."""
    manager = TaskManager()
    
    # Sample data for demonstration
    if not manager.tasks:
        manager.create_task(
            "Complete Python Project",
            "Finish the task management system with all features",
            Priority.HIGH,
            (datetime.now() + timedelta(days=7)).isoformat(),
            ["python", "project"]
        )
        manager.create_task(
            "Review Documentation",
            "Review and update project documentation",
            Priority.MEDIUM,
            (datetime.now() + timedelta(days=3)).isoformat(),
            ["documentation"]
        )

    while True:
        print("\n" + "="*60)
        print("TASK MANAGEMENT SYSTEM")
        print("="*60)
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Filter Tasks")
        print("4. Search Tasks")
        print("5. Update Task")
        print("6. Complete Task")
        print("7. Delete Task")
        print("8. Add Subtask")
        print("9. Task Statistics")
        print("10. Add Comment")
        print("11. View Task Details")
        print("12. Exit")
        print("="*60)
        
        choice = input("Enter your choice (1-12): ").strip()
        
        if choice == '1':
            # Create Task
            title = input("Task title: ").strip()
            description = input("Description: ").strip()
            print("Priority (1=LOW, 2=MEDIUM, 3=HIGH, 4=URGENT): ")
            priority = Priority(int(input("Enter number: ")))
            due_date = input("Due date (YYYY-MM-DD, press Enter to skip): ").strip()
            if due_date:
                try:
                    due_date = datetime.fromisoformat(due_date).isoformat()
                except ValueError:
                    print("Invalid date format. Skipping due date.")
                    due_date = None
            tags = input("Tags (comma-separated): ").strip().split(',')
            tags = [t.strip() for t in tags if t.strip()]
            assigned_to = input("Assign to (name): ").strip() or None
            
            task = manager.create_task(title, description, priority, due_date, tags, assigned_to)
            print(f"Task created successfully! ID: {task.id}")
        
        elif choice == '2':
            # View All Tasks
            tasks = manager.filter_tasks()
            display_tasks(tasks, "All Tasks")
        
        elif choice == '3':
            # Filter Tasks
            print("\nFilter options:")
            print("Status (pending/in_progress/completed/archived): ")
            status_input = input("Enter status (press Enter to skip): ").strip()
            status = Status(status_input) if status_input else None
            
            print("Priority (1=LOW, 2=MEDIUM, 3=HIGH, 4=URGENT): ")
            priority_input = input("Enter priority number (press Enter to skip): ").strip()
            priority = Priority(int(priority_input)) if priority_input else None
            
            tag = input("Filter by tag (press Enter to skip): ").strip() or None
            assigned_to = input("Filter by assignee (press Enter to skip): ").strip() or None
            overdue = input("Show only overdue? (y/n): ").strip().lower() == 'y'
            
            tasks = manager.filter_tasks(status, priority, tag, assigned_to, overdue)
            display_tasks(tasks, "Filtered Tasks")
        
        elif choice == '4':
            # Search Tasks
            query = input("Enter search term: ").strip()
            tasks = manager.search_tasks(query)
            display_tasks(tasks, f"Search Results for '{query}'")
        
        elif choice == '5':
            # Update Task
            task_id = input("Enter task ID: ").strip()
            task = manager.get_task(task_id)
            if not task:
                print("Task not found!")
                continue
            
            print(f"Updating task: {task.title}")
            title = input(f"New title (current: {task.title}, press Enter to skip): ").strip()
            description = input(f"New description (press Enter to skip): ").strip()
            priority_input = input(f"New priority (1-4, current: {task.priority.value}, press Enter to skip): ").strip()
            status_input = input(f"New status (pending/in_progress/completed/archived, press Enter to skip): ").strip()
            
            updates = {}
            if title: updates['title'] = title
            if description: updates['description'] = description
            if priority_input: updates['priority'] = int(priority_input)
            if status_input: updates['status'] = status_input
            
            if manager.update_task(task_id, **updates):
                print("Task updated successfully!")
            else:
                print("Failed to update task.")
        
        elif choice == '6':
            # Complete Task
            task_id = input("Enter task ID to complete: ").strip()
            task = manager.get_task(task_id)
            if task:
                task.complete()
                manager.save_data()
                print(f"Task {task_id} completed successfully!")
            else:
                print("Task not found!")
        
        elif choice == '7':
            # Delete Task
            task_id = input("Enter task ID to delete: ").strip()
            archive = input("Archive instead of delete? (y/n): ").strip().lower() == 'y'
            if manager.delete_task(task_id, archive):
                print(f"Task {task_id} {'archived' if archive else 'deleted'} successfully!")
            else:
                print("Task not found!")
        
        elif choice == '8':
            # Add Subtask
            parent_id = input("Enter parent task ID: ").strip()
            parent = manager.get_task(parent_id)
            if not parent:
                print("Parent task not found!")
                continue
            
            title = input("Subtask title: ").strip()
            description = input("Subtask description: ").strip()
            subtask = Task(
                id=manager._generate_id(),
                title=title,
                description=description,
                priority=parent.priority,
                status=Status.PENDING,
                created_at=datetime.now().isoformat()
            )
            parent.add_subtask(subtask)
            manager.save_data()
            print(f"Subtask added! ID: {subtask.id}")
        
        elif choice == '9':
            # Statistics
            stats = manager.get_task_statistics()
            print("\n" + "="*50)
            print("TASK STATISTICS")
            print("="*50)
            print(f"Total Tasks: {stats['total_tasks']}")
            print(f"Completion Rate: {stats['completion_rate']:.1f}%")
            print(f"Overdue Tasks: {stats['overdue_tasks']}")
            print(f"Total Estimated Hours: {stats['total_estimated_hours']:.1f}")
            print(f"Total Actual Hours: {stats['total_actual_hours']:.1f}")
            print("\nBy Status:")
            for status, count in stats['by_status'].items():
                print(f"  {status}: {count}")
            print("\nBy Priority:")
            for priority, count in stats['by_priority'].items():
                print(f"  {priority}: {count}")
            print("="*50)
            
        
        elif choice == '10':
            # Add Comment
            task_id = input("Enter task ID: ").strip()
            task = manager.get_task(task_id)
            if not task:
                print("Task not found!")
                continue
            user = input("Your name: ").strip()
            comment = input("Your comment: ").strip()
            task.add_comment(user, comment)
            manager.save_data()
            print("Comment added successfully!")
        
        elif choice == '11':
            # View Task Details
            task_id = input("Enter task ID: ").strip()
            task = manager.get_task(task_id)
            if not task:
                print("Task not found!")
                continue
            
            print("\n" + "="*60)
            print("TASK DETAILS")
            print("="*60)
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Priority: {task.priority.name}")
            print(f"Status: {task.status.value}")
            print(f"Created: {task.created_at[:19]}")
            if task.due_date:
                print(f"Due Date: {task.due_date[:19]}")
            if task.completed_at:
                print(f"Completed: {task.completed_at[:19]}")
            if task.assigned_to:
                print(f"Assigned To: {task.assigned_to}")
            print(f"Estimated Hours: {task.estimated_hours}")
            print(f"Actual Hours: {task.actual_hours}")
            print(f"Tags: {', '.join(task.tags) if task.tags else 'None'}")
            print(f"Is Overdue: {'Yes' if task.is_overdue() else 'No'}")
            
            if task.subtasks:
                print(f"\nSubtasks ({len(task.subtasks)}):")
                for st in task.subtasks:
                    print(f"  - {st.title} [{st.status.value}]")
            
            if task.dependencies:
                print(f"\nDependencies: {', '.join(task.dependencies)}")
            
            if task.comments:
                print(f"\nComments ({len(task.comments)}):")
                for comment in task.comments:
                    print(f"  [{comment['user']}] {comment['comment'][:50]}...")
            print("="*60)
        
