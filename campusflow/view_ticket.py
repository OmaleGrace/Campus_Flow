from campusflow.tickets import read_data

def view_ticket():
    tickets_database=read_data
    while True:
        choose=input("Enter Ticket_ID:")
        if choose in tickets_database() and tickets_database() !={}:
            print("*Ticket Details*")
            print(tickets_database()[choose])
            break
        else:
            print("invalid id number/empty data")
            answer=input("continue? y/n:").lower()
            if answer=="y":
                pass
            elif answer=="n":
                return 

