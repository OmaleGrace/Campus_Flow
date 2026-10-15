# function for filtering tickets

def filter_tickets(self, tickets_dic, status = None, priority=None, search_term= None):

    filtered_records = []
    for ticket in tickets_dic.values():
        match = True
        # validate status for the filter
        if status and ticket.get('status', '').lower() != status.lower():
            match = False
            # validate priority for the filter
        if priority and ticket.get("priority", "").casefold() != priority.lower():
            match = False
        # keyword search filter
        if search_term:
            term = search_term.lower()
            title = ticket.get('title', '').lower()
            desc = ticket.get('description', '').lower()
            if term not in title and term not in desc:
                match = False
        if match:
            self.filtered_records.append(ticket)
    return self.filtered_records
