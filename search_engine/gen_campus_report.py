# Function to generate campus report for the head of campus
def generate_campus_report(ticket_list):
    report = {
        "status_counts": {
            "open": 0,
            "in_proress": 0,
            "resolved": 0
        },
        "priority_counts":{
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        },
        "total": 0
    }
    for ticket in ticket_list.values():
        report["total"] += 1
        
        status = ticket.get("status", "").lower().strip()
        if status == "in prograss":
            status = "in_prograss"
        if status in report["status_counts"]:
            report["status_counts"][status] +=1
        priority = ticket.get("priority", "").lower().strip()

        if priority in report["priority_counts"]:
            report["priority_counts"][priority] += 1
    return report