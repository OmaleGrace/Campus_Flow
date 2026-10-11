VALID_STATUSES = ("open", "in_progress", "resolved")


def update_ticket_status(tickets, ticket_id, new_status):
    ticket_id = ticket_id.strip().upper()
    new_status = new_status.strip().lower()

    # Check whether the ticket exists.
    if ticket_id not in tickets:
        raise ValueError("Ticket ID does not exist.")

    ticket = tickets[ticket_id]

    # Validate the requested status.
    if new_status not in VALID_STATUSES:
        raise ValueError(
            "Invalid status. Choose open, in_progress, or resolved."
        )

    current_status = ticket["status"].strip().lower()

    # Check whether the ticket's current status is valid.
    if current_status not in VALID_STATUSES:
        raise ValueError("The ticket has an invalid current status.")

    # Do not allow a ticket to be moved to its current status.
    if current_status == new_status:
        raise ValueError(
            f"Ticket is already in {current_status} status."
        )

    # A ticket must be assigned before work can begin.
    if current_status == "open" and new_status == "in_progress":
        if not ticket.get("assigned_to"):
            raise ValueError(
                "Cannot start work on an unassigned ticket."
            )

        ticket["status"] = "in_progress"

    # Work can only be completed from in_progress.
    elif current_status == "in_progress" and new_status == "resolved":
        ticket["status"] = "resolved"

    # Reopening a resolved ticket must be explicit.
    elif current_status == "resolved" and new_status == "open":
        ticket["status"] = "open"

    else:
        raise ValueError(
            f"Cannot change status from {current_status} "
            f"to {new_status}."
        )

    return ticket


def change_ticket_status(tickets):
    if not tickets:
        print("No tickets available.")
        return

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Error: Ticket ID does not exist.")
        return

    print("\nAvailable statuses:")
    print("1. open")
    print("2. in_progress")
    print("3. resolved")

    status_options = {
        "1": "open",
        "2": "in_progress",
        "3": "resolved",
    }

    choice = input("Choose the new status: ").strip()

    if choice not in status_options:
        print("Error: Invalid status selection.")
        return

    new_status = status_options[choice]

    try:
        ticket = update_ticket_status(
            tickets,
            ticket_id,
            new_status,
        )

        print(
            f"Ticket {ticket_id} status updated to "
            f"{ticket['status']} successfully."
        )

    except ValueError as error:
        print(f"Error: {error}")