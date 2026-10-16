import os
import json
from campusflow.note_validate import add_note

setup_data = {"123": {"notes": []}}
with open("database.json", "w") as f:
    json.dump(setup_data, f)
print("Running tests...")

# Test 1: Adding a valid note works
add_note(ticket_id="123", author="Alice", message="Hello World")

with open("database.json", "r") as f:
    saved_data = json.load(f)

assert len(saved_data["123"]["notes"]) == 1
assert saved_data["123"]["notes"][0]["author"] == "Alice"
print("✓ Valid note test passed!")

# Test 2: Empty author throws an error
try:
    add_note(ticket_id="123", author="", message="Hello World")
    print("✗ Test failed: Empty author should have thrown an error.")
except ValueError:
    print("✓ Empty author error test passed!")

# 3. Clean up the file afterward
os.remove("database.json")
print("All tests finished.")
