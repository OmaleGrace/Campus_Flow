# tickets = {
#     "T001": {
#         "title": "Campus Wi-Fi is down",
#         "category": "Network",
#         "urgency": "high",
#         "affected_users": 15,
#         "priority": "critical",
#         "status": "open",
#         "assigned_to": None
#     },

#     "T002": {
#         "title": "Camp Widown",
#         "category": "Network",
#         "urgency": "high",
#         "affected_users": 15,
#         "priority": "critical",
#         "status": "open",
#         "assigned_to": "Grace"
#     }
# }


## F2 — LIST / VIEW: Show all tickets and details for one chosen ticket.


def list_tickets(tickets):
    if not tickets:
        print("No ticket available")
        return
    print("\n-------ALL TICKETS------")

    for ticket_id, ticket_details in tickets.items():
        print(f"\nTicket ID: {ticket_id}")
        print(f"Title: {ticket_details['title']}")
        print(f"Category: {ticket_details['category']}")
        print(f"Urgency: {ticket_details['urgency']}")
        print(f"Affected Users: {ticket_details['affected_users']}")
        print(f"Priority: {ticket_details['priority']}")
        print(f"Status: {ticket_details['status']}")

        assigned_to = ticket_details["assigned_to"]

        if assigned_to:
            print(f"Assigned To: {assigned_to}")
        else:
            print("Assigned To: Not assigned")
        print("-" * 30)

def view_ticket(tickets):
    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Error: Ticket ID does not exist")
        return
    
    ticket_details = tickets[ticket_id]

    print("\n------TICKET DETAILS------")
    print(f"Ticket ID: {ticket_id}")
    print(f"Title: {ticket_details['title']}")
    print(f"Category: {ticket_details['category']}")
    print(f"Urgency: {ticket_details['urgency']}")
    print(f"Affected Users: {ticket_details['affected_users']}")
    print(f"Priority: {ticket_details['priority']}")
    print(f"Status: {ticket_details['status']}")

    if ticket_details["assigned_to"]:
        print(f"Assigned To: {ticket_details['assigned_to']}")
    else:
        print("Assigned To: Not assigned")

# list_tickets(tickets)
# view_ticket(tickets)


## ✳️ F3 — ASSIGN: Assign a ticket to a non-empty staff member name; reject unknown ticket IDs.

def assign_ticket(tickets):
    if not tickets:
        print("No ticket available")
        return

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Error: Ticket ID does not exist.")
        return

    staff_name = input("Enter staff member's name: ").strip()

    if not staff_name:
        print("Error: Staff name cannot be empty.")
        return

    tickets[ticket_id]["assigned_to"] = staff_name

    print(f"Ticket {ticket_id} has been assigned to {staff_name}.")