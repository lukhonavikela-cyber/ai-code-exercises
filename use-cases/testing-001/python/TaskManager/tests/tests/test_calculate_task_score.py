
import unittest
from datetime import datetime

from task_priority import calculate_task_score


class TestCalculateTaskScore(unittest.TestCase):

    def test_higher_priority_results_in_higher_score(self):
        now = datetime(2026, 1, 1)

        low_priority_task = {
            "priority": 1,
            "last_updated": now,
            "due_date": None
        }

        high_priority_task = {
            "priority": 3,
            "last_updated": now,
            "due_date": None
        }

        low_score = calculate_task_score(low_priority_task, now)
        high_score = calculate_task_score(high_priority_task, now)

        self.assertGreater(high_score, low_score)

def test_overdue_task_gets_score_boost(self):
        now = datetime(2026, 1, 10)

        overdue_task = {
            "priority": 1,
            "last_updated": now,
            "due_date": datetime(2026, 1, 5)
        }

        score = calculate_task_score(overdue_task, now)

        # Base score from priority is at least 10
        # Overdue tasks should receive a significant boost
        self.assertGreaterEqual(score, 60)


def test_task_assigned_to_current_user_gets_score_boost(self):
        now = datetime(2026, 1, 1)

        task = {
            "priority": 1,
            "last_updated": now,
            "due_date": None,
            "assigned_to_current_user": True
        }

        score = calculate_task_score(task, now)

        # Base score = 10 (priority 1 * 10)
        # Assigned-to-current-user bonus = +12
        self.assertEqual(score, 22)
``

def test_days_since_update_uses_whole_days(self):
        now = datetime(2026, 1, 10, 12, 0, 0)
        last_updated = datetime(2026, 1, 9, 13, 0, 0)

        task = {
            "priority": 1,
            "last_updated": last_updated,
            "due_date": None
        }

        score = calculate_task_score(task, now)

        # Base score = 10
        # Task was updated 1 day ago → penalty should be exactly 1
        self.assertEqual(score, 9)
``

