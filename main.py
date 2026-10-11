from campusflow.tickets import Create_ticket, read_data, tickets_database
from campusflow.list_ticket import list_ticket
from campusflow.view_ticket import view_ticket
from campusflow.assign_ticket import assign_ticket
from campusflow.workflow import change_ticket_status
from campusflow.work_queue import display_work_queue
from campusflow.reports import display_report


def campus_flow():
    while True:
        design = "🀫" * 50
        print()
        print("****Welcome To CampusFlow Helper Desk Service****")
        print(design)
        print("Menu")
        print("᠆᠆᠆᠆᠆")
        print("1. Generate Ticket")
        print("2. List Tickets")
        print("3. View Ticket")
        print("4. Assign Ticket")
        print("5. Reports")
        print("6. Change Ticket Status")
        print("7. Work Queue")
        print("8. Exit")

        option = input("Select option: ")

        if option == "1":
            print(Create_ticket())

        elif option == "2":
            print(list_ticket())

        elif option == "3":
            print(view_ticket())

        elif option == "4":
            assign_ticket(tickets_database)

        elif option == "5":
            display_report(tickets_database)

        elif option == "6":
            change_ticket_status(tickets_database)

        elif option == "7":
            display_work_queue(tickets_database)

        elif option == "8":
            print("Exited...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    campus_flow()