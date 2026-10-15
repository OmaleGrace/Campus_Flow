import unittest

from search_engine.gen_campus_report import generate_campus_report

class TestAnalyticsEngine(unittest.TestCase):

    def setUp(self):
        self.data = {
            "T001": {"status": "resolved", "priority": "critical"},
            "T002": {"status": "open", "priority": "high"},
            "T003": {"status": "open", "priority": "critical"}
        }
    
    def test_generation_campus_report(self):
        campus_report = generate_campus_report(self.data)
        self.assertEqual(campus_report['total'], 3)
        self.assertEqual(campus_report["status_counts"]["open"], 2)
        self.assertEqual(campus_report['status_counts']['resolved'], 1)
        self.assertEqual(campus_report["priority_counts"]['high'], 1)
        self.assertEqual(campus_report['priority_counts']['critical'], 2)
if __name__ == "__main__":
    unittest.main()