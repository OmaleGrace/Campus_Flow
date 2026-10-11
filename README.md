# CampusFlow

CampusFlow is a command-line helpdesk app for Learn2Earn campus staff. It records tech problems (Wi-Fi outages, faulty laptops, broken dev environments) as tickets, works out how urgent each one is, assigns it to someone, and tracks it until it is resolved. Tickets are saved to a JSON file so nothing is lost when the program closes.

## Team

- Omale Ooja Grace
- Tavershima Gbaa Elvis

## Requirements

- Python 3.10 or newer
- No extra packages needed

## How to run

```bash
python main.py
```

The menu keeps running until you choose Exit.

## Features

- Create a ticket (with input validation)
- List all tickets or view one
- Assign a ticket to a staff member
- Change ticket status
- View the work queue
- View reports
- Save and reload tickets from JSON

## Ticket rules

- **Category:** Network, Hardware, Software or Other
- **Urgency:** low, medium or high
- **Affected users:** a positive whole number
- **Title:** cannot be blank
- **ID:** generated automatically (T001, T002, ...)

## Priority

The first rule that matches is used:

1. High urgency and 10 or more affected users: critical
2. High urgency or 10 or more affected users: high
3. Medium urgency or 3 or more affected users: medium
4. Anything else: low

## Status

Tickets move in this order: `open` -> `in_progress` -> `resolved`.

- A ticket must be assigned before it can be set to `in_progress`.
- A resolved ticket can only be changed after it is reopened (set back to `open`).

## Work queue

Shows open tickets from critical to low. Tickets with the same priority are ordered by ticket number, lowest first.

## Saved data

Tickets are saved in `data/tickets.json` and loaded when the program starts. If the file is missing, the program starts empty. If the file is corrupted, the program shows an error instead of erasing your data. Delete the file to start fresh.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Known limitations

- Terminal only, no graphical interface
- Tickets are stored in a single JSON file, so it is not safe for several people to use at once
- Staff names are free text and are not checked
