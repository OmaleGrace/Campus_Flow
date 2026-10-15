import json

def view_ticket_notes(tickets):
    if not tickets:
        print("No tickets available.")
        return
    ticket_id = input("Enter ticket ID to see notes: ").strip().upper()
    if ticket_id not in tickets:
        print("Error: Ticket ID does not exist.")
        return
    ticket = tickets[ticket_id]
    notes = ticket.get("notes", [])
    if not notes:
        print("No notes found for this ticket.")
        return
    print(f"\n--- Notes for Ticket {ticket_id} ---")
    for note in notes:
        print(f"[{note['note_id']}] By: {note['author']}")
        print(f"Message: {note['message']}")
        print("-" * 20)