
import unittest
from campusflow.view_note import view_ticket_notes

class TestViewTicketNotes(unittest.TestCase):

    def test_view_notes_empty_database(self):
        """Test that viewing notes fails gracefully if no tickets exist."""
        empty_tickets = {}
        
        # Capture logging output directly through unittest
        with self.assertLogs(level='INFO') as log:
            view_ticket_notes(empty_tickets)
            
            # Verify the function logged the expected warning
            self.assertTrue(any("No tickets available." in message for message in log.output))

if __name__ == '__main__':
    unittest.main()

