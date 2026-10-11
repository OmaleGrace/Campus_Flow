
from campusflow.tickets import Create_ticket, read_data
from campusflow.list_ticket import list_ticket
from campusflow.view_ticket import view_ticket

def campus_flow():
    while True:
        design="🀫"*50
        print()
        print("****Welcome To CampusFlow Helper Desk Service****")
        print(design)
        print("Menu")
        print("᠆᠆᠆᠆᠆")
        print("1. generate Ticket")
        print("2. list")
        print("3. view")
        print("4. assign")
        print("5. reports")
        print("6. exit")
        option=input("select option:")
        if option=="1":
            print(Create_ticket())
        elif option=="2":
            print(list_ticket())
        elif option=="3":
            print(view_ticket())
        elif option=="4":
            pass
        elif option=="5":
            pass
        elif option=="6":
            print("exited...")
            break
        else:
            print("invalid option")  
campus_flow()