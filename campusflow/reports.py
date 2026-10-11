STATUS_OPTIONS = ("open", "in_progress", "resolved")
PRIORITY_OPTIONS = ("critical", "high", "medium", "low")


def generate_report(tickets):
    report = {
        "total": len(tickets),
        "by_status": {status: 0 for status in STATUS_OPTIONS},
        "by_priority": {priority: 0 for priority in PRIORITY_OPTIONS},
    }

    for ticket in tickets.values():
        status = ticket["status"].strip().lower()
        priority = ticket["priority"].strip().lower()

        if status in report["by_status"]:
            report["by_status"][status] += 1

        if priority in report["by_priority"]:
            report["by_priority"][priority] += 1

    return report


def display_report(tickets):
    report = generate_report(tickets)

    print("\n===== TICKET REPORT =====")
    print(f"Total tickets: {report['total']}")

    print("\nTickets by status:")
    for status, count in report["by_status"].items():
        print(f"{status}: {count}")

    print("\nTickets by priority:")
    for priority, count in report["by_priority"].items():
        print(f"{priority}: {count}")