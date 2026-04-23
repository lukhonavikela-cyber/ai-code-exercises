
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
