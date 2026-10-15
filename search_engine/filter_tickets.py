# function for filtering tickets

def filter_tickets(tickets_dic, status = None, priority=None, search_term= None):

    filtered_records = []
    for ticket in tickets_dic.values():
        match = True
        # validate status for the filter
        if status and ticket.get('status', '').lower() != status.lower():
            match = False
            # validate priority for the filter
        if priority and ticket.get("priority", "").lower() != priority.lower():
            match = False
        # keyword search filter
        if search_term:
            term = search_term.lower()
            title = ticket.get('title', '').lower()

            if term not in title:
                match = False
        if match:
            filtered_records.append(ticket)
    return filtered_records
