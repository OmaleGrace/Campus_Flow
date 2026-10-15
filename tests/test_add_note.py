import unittest
from unittest.mock import patch
from campusflow.notes import add_ticket_note

class TestAddTicketNote(unittest.TestCase):
    def test_add_note_empty_database(self):
        """Test that adding a note fails gracefully if no tickets exist."""
        empty_tickets = {}
        with patch('sys.stdout') as mocked_stdout:
            add_ticket_note(empty_tickets)
            # Verify the function handles empty databases safely
            mocked_stdout.write.assert_any_call("No tickets available.")

if __name__ == '__main__':
    unittest.main()
