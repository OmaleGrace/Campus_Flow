from campusflow.tickets import read_data
from search_engine.append_note_to_db import appened_note_to_db

def add_note_to_ticket():
    print("\n---ADD TICKET FOLLOW-UP NOTE---")

    tickets = read_data()
    # validate tickets availability
    if not tickets:
        print("Ticket not available")
        return
    # validate ticket id 
    while True:
        ticket_id = input("Enter Ticket_Ida: ").strip().upper()
        if ticket_id not in tickets:
            print(f"Ticket_id {ticket_id} entered is wrong, please retry")
            continue
        if tickets[ticket_id]["status"].strip().lower() == "resolved":
            print(f"Can't add note to a resolved ticket {ticket_id}")
            return
        break
    # validate author input
    while True:
        author = input("Enter author name: ").strip()
        if not author:
            print("sorry!, author can't be empty.")
            continue
        break
    # validate message characters 
    while True:
        message = input("Enter note message:").strip()
        if len(message) <5 and len(message)> 300:
            print("\033[1mMessage can't be less than 5 or greater than 300\033[0m")
            continue
        break
    try:
        note_id = appened_note_to_db(tickets, ticket_id, author, message)
        print(f"\033[1msuccess: Note {note_id} added to ticket {ticket_id}.\033[0m")
    except OSError:
        print("faild saving the note to database file.")