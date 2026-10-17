import os
import json
from itertools import count

def add_note(ticket_id, author, message):
 
    if not ticket_id or str(ticket_id).strip() == "":
        raise ValueError("Ticket ID cannot be empty.")   
    if not author or author.strip() == "":
        raise ValueError("Author name cannot be empty.")  
    if not message or len(message.strip()) < 5:
        raise ValueError("Note message must be at least 5 characters.")
    if not message or len(message.strip())>300:
        raise ValueError("Note message must not be greaterthan 300 characters") 

    filename = "database.json"
    ticket_id_strip=str(ticket_id).strip()
    if not os.path.exists(filename):
        raise ValueError(f"Database error: The file {filename} does not exist.")
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, IOError):
        raise ValueError("Database error: Failed to read the JSON file.")
        
    if ticket_id_strip not in data:
        raise ValueError(f"Ticket {ticket_id_strip} not found.")

    next_note_number =count(start=1)
    note_id = f"N{next(next_note_number):03d}" 
    note = {
        "note_id": note_id,
        "author": author.strip(),
        "message": message.strip()
    }

    data[ticket_id_strip]["notes"].append(note)
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise ValueError("Database error: Failed to write updates to the file.")


