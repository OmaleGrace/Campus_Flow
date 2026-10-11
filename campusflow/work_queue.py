PRIORITY_ORDER = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
}


def get_work_queue(tickets):
    unresolved_tickets = [
        ticket
        for ticket in tickets.values()
        if ticket["status"].strip().lower() != "resolved"
    ]

    unresolved_tickets.sort(
        key=lambda ticket: (
            PRIORITY_ORDER.get(ticket["priority"].strip().lower(), 5),
            int(ticket["id"][1:]),
        )
    )

    return unresolved_tickets


def display_work_queue(tickets):
    work_queue = get_work_queue(tickets)

    if not work_queue:
        print("No unresolved tickets in the work queue.")
        return

    print("\n===== WORK QUEUE =====")

    for ticket in work_queue:
        print(f"Ticket ID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"Assigned to: {ticket['assigned_to'] or 'Unassigned'}")
        print("-" * 30)