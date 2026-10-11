from campusflow.tickets import read_data

def list_ticket():
    
    tickets_database=read_data
    print("**Tickets-ID**:")
    for id_list in tickets_database():
        print(id_list)
