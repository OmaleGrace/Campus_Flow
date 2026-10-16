import json

def appened_note_to_db(ticket_dict, ticket_id, author, message):

    ticket = ticket_dict[ticket_id]
    if "note" not in ticket:
        ticket["note"] = []
    next_num =  len(ticket["note"]) + 1
    note_id = f"N{next_num:03d}"

    new_note ={
        "note_id": note_id,
        "author": author,
        "message": message
    }
    ticket["note"].append(new_note)

    with open("database.json", "w") as file:
        json.dump(ticket_dict, file, indent=4)

    return note_id