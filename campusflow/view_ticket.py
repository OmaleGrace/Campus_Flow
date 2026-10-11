from campusflow.tickets import read_data

def view_ticket():
    tickets_database=read_data
    choose=input("Enter Ticket_ID:")
    if choose in tickets_database() or tickets_database() !={}:
        print("*Ticket Details*")
        print(f"{tickets_database()[choose]}")
    else:
        print("invalid id number/empty data")
