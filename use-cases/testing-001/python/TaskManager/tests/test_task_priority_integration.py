
import unittest
from datetime import datetime, timedelta

from task_priority import (
    calculate_task_score,
    sort_tasks_by_importance,
    get_top_priority_tasks
)
from models import TaskPriority


class TestTaskPriorityIntegration(unittest.TestCase):

    def test_full_task_priority_workflow(self):
        now = datetime(2026, 1, 10)

        tasks = [
            {
                "id": 1,
                "priority": TaskPriority.HIGH,
                "last_updated": now,
                "due_date": None,
                "tags": [],
                "status": None
            },
            {
                "id": 2,
                "priority": TaskPriority.MEDIUM,
                "last_updated": now,
                "due_date": now - timedelta(days=1),  # overdue
                "tags": [],
                "status": None
            },
            {
                "id": 3,
                "priority": TaskPriority.LOW,
                "last_updated": now,
                "due_date": None,
                "tags": [],
                "status": None
            }
        ]

        top_tasks = get_top_priority_tasks(tasks, limit=2)

        self.assertEqual(len(top_tasks), 2)
        self.assertEqual(top_tasks[0]["id"], 2)  # overdue first
        self.assertEqual(top_tasks[1]["id"], 1)  # high priority second
