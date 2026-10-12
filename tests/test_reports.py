import unittest
from campusflow.reports import generate_report


class TestReports(unittest.TestCase):

    def setUp(self):
        self.tickets = {
            "T001": {
                "id": "T001",
                "title": "Network down",
                "status": "open",
                "priority": "critical",
            },
            "T002": {
                "id": "T002",
                "title": "Software issue",
                "status": "in_progress",
                "priority": "high",
            },
            "T003": {
                "id": "T003",
                "title": "Old ticket",
                "status": "resolved",
                "priority": "medium",
            },
            "T004": {
                "id": "T004",
                "title": "Another issue",
                "status": "open",
                "priority": "low",
            },
        }

    def test_total_tickets(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["total"], 4)

    def test_status_breakdown(self):
        report = generate_report(self.tickets)

        self.assertEqual(
            report["by_status"],
            {"open": 2, "in_progress": 1, "resolved": 1},
        )

    def test_priority_breakdown(self):
        report = generate_report(self.tickets)

        self.assertEqual(
            report["by_priority"],
            {"critical": 1, "high": 1, "medium": 1, "low": 1},
        )

    def test_empty_database(self):
        report = generate_report({})

        self.assertEqual(report["total"], 0)
        self.assertEqual(
            report["by_status"],
            {"open": 0, "in_progress": 0, "resolved": 0},
        )
        self.assertEqual(
            report["by_priority"],
            {"critical": 0, "high": 0, "medium": 0, "low": 0},
        )

    def test_capitalized_status(self):
        self.tickets["T005"] = {
            "id": "T005",
            "title": "Another completed ticket",
            "status": "Resolved",
            "priority": "high",
        }

        report = generate_report(self.tickets)
        self.assertEqual(report["by_status"]["resolved"], 2)

    def test_counts_are_independent(self):
        report = generate_report(self.tickets)

        self.assertEqual(sum(report["by_status"].values()), 4)
        self.assertEqual(sum(report["by_priority"].values()), 4)


if __name__ == "__main__":
    unittest.main()