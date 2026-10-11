import unittest

from workflow import update_ticket_status


def make_ticket(status="open", assigned_to=None):
    return {
        "id": "T001",
        "title": "Campus Wi-Fi is down",
        "category": "Network",
        "urgency": "high",
        "affected_users": 12,
        "priority": "critical",
        "status": status,
        "assigned_to": assigned_to,
    }


class TestTicketWorkflow(unittest.TestCase):

    def setUp(self):
        self.tickets = {
            "T001": make_ticket()
        }

    def test_unassigned_ticket_cannot_start_work(self):
        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T001", "in_progress"
            )

        self.assertEqual(
            self.tickets["T001"]["status"], "open"
        )

    def test_assigned_ticket_can_start_work(self):
        self.tickets["T001"]["assigned_to"] = "Grace"

        ticket = update_ticket_status(
            self.tickets, "T001", "in_progress"
        )

        self.assertEqual(ticket["status"], "in_progress")

    def test_ticket_can_be_resolved(self):
        self.tickets["T001"]["assigned_to"] = "Grace"
        self.tickets["T001"]["status"] = "in_progress"

        ticket = update_ticket_status(
            self.tickets, "T001", "resolved"
        )

        self.assertEqual(ticket["status"], "resolved")

    def test_resolved_ticket_can_be_reopened(self):
        self.tickets["T001"]["status"] = "resolved"

        ticket = update_ticket_status(
            self.tickets, "T001", "open"
        )

        self.assertEqual(ticket["status"], "open")

    def test_resolved_ticket_cannot_skip_reopening(self):
        self.tickets["T001"]["status"] = "resolved"

        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T001", "in_progress"
            )

        self.assertEqual(
            self.tickets["T001"]["status"], "resolved"
        )

    def test_unknown_ticket_is_rejected(self):
        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T999", "in_progress"
            )

    def test_invalid_status_is_rejected(self):
        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T001", "pending"
            )

        self.assertEqual(
            self.tickets["T001"]["status"], "open"
        )

    def test_ticket_cannot_skip_in_progress(self):
        self.tickets["T001"]["assigned_to"] = "Grace"

        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T001", "resolved"
            )

        self.assertEqual(
            self.tickets["T001"]["status"], "open"
        )

    def test_ticket_cannot_return_to_open_from_in_progress(self):
        self.tickets["T001"]["assigned_to"] = "Grace"
        self.tickets["T001"]["status"] = "in_progress"

        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T001", "open"
            )

        self.assertEqual(
            self.tickets["T001"]["status"], "in_progress"
        )

    def test_status_input_is_normalized(self):
        self.tickets["T001"]["assigned_to"] = "Grace"

        ticket = update_ticket_status(
            self.tickets, "t001", "IN_PROGRESS"
        )

        self.assertEqual(ticket["status"], "in_progress")

    def test_ticket_cannot_move_to_its_current_status(self):
        with self.assertRaises(ValueError):
            update_ticket_status(
                self.tickets, "T001", "open"
            )

        self.assertEqual(
            self.tickets["T001"]["status"], "open"
        )


if __name__ == "__main__":
    unittest.main()