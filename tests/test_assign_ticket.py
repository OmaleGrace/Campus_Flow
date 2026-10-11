import unittest
from unittest.mock import patch
from assign_ticket import assign_ticket


class TestAssignTicket(unittest.TestCase):

    def setUp(self):
        self.tickets = {
            "T001": {
                "id": "T001",
                "title": "Campus Wi-Fi is down",
                "category": "Network",
                "urgency": "high",
                "affected_users": 12,
                "priority": "critical",
                "status": "open",
                "assigned_to": None,
            },
            "T002": {
                "id": "T002",
                "title": "Laptop is faulty",
                "category": "Hardware",
                "urgency": "medium",
                "affected_users": 2,
                "priority": "medium",
                "status": "resolved",
                "assigned_to": None,
            },
        }

    def test_assign_ticket_successfully(self):
        with patch("builtins.input", side_effect=["T001", "Grace"]):
            assign_ticket(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["assigned_to"], "Grace"
        )

    def test_reject_unknown_ticket_id(self):
        with patch("builtins.input", side_effect=["T999"]):
            assign_ticket(self.tickets)

        self.assertIsNone(
            self.tickets["T001"]["assigned_to"]
        )

    def test_reject_empty_staff_name(self):
        with patch("builtins.input", side_effect=["T001", ""]):
            assign_ticket(self.tickets)

        self.assertIsNone(
            self.tickets["T001"]["assigned_to"]
        )

    def test_reject_whitespace_staff_name(self):
        with patch("builtins.input", side_effect=["T001", "   "]):
            assign_ticket(self.tickets)

        self.assertIsNone(
            self.tickets["T001"]["assigned_to"]
        )

    def test_cannot_assign_resolved_ticket(self):
        with patch("builtins.input", side_effect=["T002"]):
            assign_ticket(self.tickets)

        self.assertIsNone(
            self.tickets["T002"]["assigned_to"]
        )

    def test_ticket_id_is_case_insensitive(self):
        with patch("builtins.input", side_effect=["t001", "Grace"]):
            assign_ticket(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["assigned_to"], "Grace"
        )

    def test_no_tickets_available(self):
        with patch("builtins.input") as mock_input:
            assign_ticket({})

        mock_input.assert_not_called()


if __name__ == "__main__":
    unittest.main()