import builtins
from campusflow.tickets import tickets_database
from campusflow.list_ticket import view_ticket  

tickets_database["T001"] = {"id": "T001", "title": "Wi-Fi Issue", "status": "Open"}

print("--- TEST 1: Searching for an existing ticket ---")
builtins.input = lambda prompt: "T001"  
view_ticket()

print("\n--- TEST 2: Searching for a fake ticket ---")
builtins.input = lambda prompt: "T999" 
view_ticket()
