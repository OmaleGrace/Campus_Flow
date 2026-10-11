def assign_ticket(tickets):
    if not tickets:
        print("No tickets available.")
        return

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Error: Ticket ID does not exist.")
        return

    ticket = tickets[ticket_id]

    if ticket["status"] == "resolved":
        print("Error: Reopen the ticket before assigning it.")
        return

    staff_name = input("Enter staff member's name: ").strip()

    if not staff_name:
        print("Error: Staff name cannot be empty.")
        return

    ticket["assigned_to"] = staff_name

    print(f"Ticket {ticket_id} assigned to {staff_name} successfully.")