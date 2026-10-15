
import json

def add_ticket_note(tickets):
    if not tickets:
        print("No tickets available.")
        return
    while True:
        ticket_id = input("Enter ticket ID: ").strip().upper()
        if ticket_id in tickets:
            ticket = tickets[ticket_id]
        if ticket_id not in tickets:
            print("Error: Ticket ID does not exist.")
            answer=input("continue? y/n:").lower()
            if answer=="y":
                pass
            elif answer=="n":
                return 
    
        elif ticket["status"].strip().lower() == "resolved":
            print("Error: Cannot add notes to a resolved ticket.")
        else:
            break
    while True:
        author = input("Enter your name: ").strip()
        if not author:
            print("Error: Author name cannot be empty.")
            answer=input("continue? y/n:").lower()
            if answer=="y":
                pass
            elif answer=="n":
                return 
        else:
            break
    while True:
        message = input("Enter note message: ").strip()
        if len(message) < 5 or len(message) > 300:
            print("Error: Message must be between 5 and 300 characters.")
        if "notes" not in ticket:
            ticket["notes"] = []
        next_number = len(ticket["notes"]) + 1
        note_id = f"N{next_number:03d}"
        new_note = {
            "note_id": note_id,
            "author": author,
            "message": message
        }
        ticket["notes"].append(new_note)
        try:
            with open("database.json", "w") as file:
                json.dump(tickets, file, indent=4)
            print(f"Success: Note {note_id} added to ticket {ticket_id}.")
            answer=input("continue? y/n:").lower()
            if answer=="y":
                pass
            elif answer=="n":
                return 
        except OSError:
            print("Error saving the note to database.")
 
