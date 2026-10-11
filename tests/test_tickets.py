import builtins
from campusflow.tickets import Create_ticket, tickets_database
fake_answers = ["Internet is down", "1", "3", "12"]
def fake_input(prompt_text):
    return fake_answers.pop(0)

builtins.input = fake_input
print("🚀 Running ticket creation test...")
Create_ticket()

last_id = list(tickets_database.keys())[-1]
ticket = tickets_database[last_id]
print("\n🔍 Verifying results...")

if ticket["title"] == "Internet is down" and ticket["category"] == "Network":
    print("✅ TEST PASSED: Ticket created successfully with correct data!")
else:
    print("❌ TEST FAILED: The data saved does not match what we typed.")
