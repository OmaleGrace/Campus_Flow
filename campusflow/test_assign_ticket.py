from assign_ticket import assign_ticket

tickets = {
    "T001": {
        "id": "T001",
        "title": "Campus Wi-Fi is down",
        "category": "Network",
        "urgency": "high",
        "affected_users": 15,
        "priority": "critical",
        "status": "open",
        "assigned_to": None
    }
}

assign_ticket(tickets)

print("\nUpdated ticket:")
print(tickets["T001"])