import unittest
# Import your actual filtering function
from search_engine.filter_tickets import filter_tickets

class TestTicketFilter(unittest.TestCase):

    def setUp(self):
        """Sets up a reliable, isolated mock database matching your JSON schema.
        
        This dictionary resets fresh before every individual test case runs.
        """
        self.database = {
            "T001": {
                "id": "T001",
                "title": "Campus Wi-Fi is down",
                "category": "Network",
                "urgency": "high",
                "affected_users": 12,
                "priority": "critical",
                "status": "resolved",
                "assigned_to": "Grace"
            },
            "T002": {
                "id": "T002",
                "title": "Staff laptop lag",
                "category": "Hardware",
                "urgency": "medium",
                "affected_users": 2,
                "priority": "medium",
                "status": "open",
                "assigned_to": "None"
            },
            "T003": {
                "id": "T003",
                "title": "Wi-Fi dropping connection",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": "Alex"
            }
        }

    def test_filter_by_single_status(self):
        """Verifies filtering by status alone returns the correct matches."""
        # T002 and T003 are open
        results = filter_tickets(self.database, status="open")
        
        self.assertEqual(len(results), 2)
        # Ensure we got the correct records by checking their IDs
        ticket_ids = [ticket["id"] for ticket in results]
        self.assertIn("T002", ticket_ids)
        self.assertIn("T003", ticket_ids)

    def test_filter_by_status_and_priority_combination(self):
        """Verifies that multi-filtering combinations narrow down correctly."""
        # Looking ONLY for open AND critical tickets (Should only match T003)
        results = filter_tickets(self.database, status="open", priority="critical")
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "T003")
        self.assertEqual(results[0]["title"], "Wi-Fi dropping connection")

    def test_filter_case_insensitivity(self):
        """Ensures that user string variations in casing still result in accurate matches."""
        # Testing uppercase inputs to verify your inner .lower() implementation
        results = filter_tickets(self.database, status="RESOLVED", priority="CRITICAL")
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "T001")

    def test_keyword_search_across_title_and_description(self):
        """Ensures search terms find matches case-insensitively within string text."""
        # Searching for 'wi-fi' should fetch T001 and T003
        results = filter_tickets(self.database, search_term="wi-fi")
        
        self.assertEqual(len(results), 2)
        ticket_ids = [ticket["id"] for ticket in results]
        self.assertNotIn("T002", ticket_ids)

    def test_empty_results_handling(self):
        """Validates that search queries with zero matches return an empty list gracefully."""
        # Searching for a non-existent priority or status shouldn't crash the code
        results = filter_tickets(self.database, priority="non-existent-priority")
        
        self.assertEqual(results, [])
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()
