# LEARNER B

# Fellow: Omale Ooja Grace

## Interaction #1 — Ticket Assignment (F3)

**Problem:**
I needed to learn how to assign a helpdesk ticket to a staff member and save the assignment so that it would still exist when the program runs again.

**My initial understanding:**
I understood that I needed to collect the ticket ID and staff member's name. However, I needed help handling invalid ticket IDs, preventing empty staff names, and saving the assignment to the JSON database.

**Prompt to AI:**
I asked AI to help me implement the ticket assignment feature for my CampusFlow helpdesk system, including validation and saving the assigned staff member.

**Useful AI guidance:**
AI helped me understand how to check whether a ticket exists, prevent assigning a ticket without a staff name, and update the ticket's assigned_to field. It also helped me implement saving the updated ticket data to database.json.

**My independent experiment/test:**
I tested the assignment feature by entering a ticket ID and a staff member's name. I also checked how the program handled invalid ticket IDs and attempted to assign a resolved ticket.

**Verification source or result:**
I tested the feature manually and ran the assignment unit tests. The assignment was saved successfully, and the program rejected attempts to assign resolved tickets.

**Decision:**
I accepted and tested the guidance because it helped implement the required feature and handle important validation cases.
Related file/commit:
- File: campusflow/assign_ticket.py
- Test file: campusflow/test_assign_ticket.py
- Commit: 49f5b7b — Implement ticket assignment (F3)

**What I can now explain without AI:**
I can explain how to find a ticket using its ID, update its assigned staff member, validate user input, and save changes to a JSON file.


## Interaction #2 — Ticket Status Workflow (F4)

**Problem:**
I needed to implement a ticket status workflow that controls how tickets move between open, in-progress, and resolved statuses.

**My initial understanding:**
I knew that tickets needed statuses to show their progress, but I needed to understand how to prevent invalid status changes and ensure that only permitted transitions were allowed.

**Prompt to AI:**
I asked AI for help implementing ticket status changes with validation, including checking the ticket ID, validating the new status, and enforcing the correct workflow rules.

**Useful AI guidance:**
AI helped me structure the status validation logic and implement rules for changing ticket statuses. For example, a ticket must be assigned before it can move from open to in_progress. A resolved ticket can be reopened by changing its status back to open.

**My independent experiment/test:**
I ran the workflow unit tests and manually tested changing a ticket from open to in_progress and then to resolved. I also checked how the program responded when I attempted to assign a resolved ticket or set a ticket to its existing status.

**Verification source or result:**
The workflow unit tests passed. My manual tests also showed the expected status changes and validation messages.

**Decision:**
I accepted the guidance after testing the workflow. I also corrected the implementation when the indentation around the try block was wrong, so the saving logic could execute properly.

**Related file/commit:**
- File: campusflow/workflow.py
- Test file: campusflow/test_workflow.py
- Commit: c9e7982 — Implement ticket status workflow (F4)

**What I can now explain without AI:**
I can explain why a workflow needs rules, how to validate a ticket's current and new statuses, and why not every status change should be permitted.


## Interaction #3 — Ticket Work Queue (F5)

**Problem:**
I needed to create a work queue that displays unresolved tickets in priority order so staff can identify which tickets need attention first.

**My initial understanding:**
I understood that tickets needed to be displayed, but I needed help organizing unresolved tickets according to their priorities and ensuring resolved tickets were excluded.

**Prompt to AI:**
I asked AI for guidance on implementing a ticket work queue that filters out resolved tickets and sorts the remaining tickets by priority.

**Useful AI guidance:**
AI helped me separate the logic for generating the work queue from the logic for displaying it. The queue filters out resolved tickets and sorts the remaining tickets by priority, with critical tickets appearing before high, medium, and low priority tickets.

**My independent experiment/test:**
I ran the work queue unit tests and tested the queue with my ticket data. After resolving my available ticket, I checked the queue's response.

**Verification source or result:**
All six work queue tests passed. During manual testing, the program displayed No unresolved tickets when the available ticket had been resolved.

**Decision:**
I accepted the guidance after the tests confirmed the expected filtering and sorting behavior.

**What I can now explain without AI:**
I can explain how filtering removes tickets that no longer need attention and how sorting helps staff prioritize the remaining work.


## Interaction #4 — Ticket Reports (F6) and Checking AI Guidance

**Problem:**
I needed to generate reports showing the total number of tickets and how tickets are distributed across different statuses and priorities.

**My initial understanding:**
I understood that a report should summarize ticket information, but I needed help organizing the counts and displaying the results clearly.

**Prompt to AI:**
I asked AI to help me implement ticket reports that calculate the total number of tickets and group them by status and priority.

**Useful AI guidance:**
AI helped me implement a report-generation function that counts tickets by status and priority. It also helped me separate the report calculations from the code that displays the report to the user.

**My independent experiment/test:**
I ran the report unit tests and manually viewed the report using my ticket data. The report showed one ticket, with its status recorded as resolved and its priority recorded as critical.

**Verification source or result:**
All six report tests passed. The manual output matched the ticket data I was testing with.

**Decision:**
I accepted the report implementation after checking it against the test results and the actual ticket data. I also learned to verify AI-generated code by running tests instead of assuming that suggested code is correct.

**What I can now explain without AI:**
I can explain how to count tickets by status and priority, calculate the total number of tickets, and separate data processing from displaying the results.



# Learner A

## Fellow: Tavershima Gbaa
### Interaction #1 — <itertools>
Problem: atumation of generating unique numbers
My initial understanding: i got to understand how the itertool method in python works, how the count() provides the iteration and the next() gives the next number, aslo setting from where to start
Prompt to AI: explain python method can i use to generate unique characters
Useful AI guidance: it provide with the itertools method and showed me how to import it , from itertools import count
My independent experiment/test: tried with ticket_id T001 and it generate T001 and T002
Verification source or result: <google ai>
Decision: accept
Related file/commit: ticket.py
What I can now explain without AI: how the itertools work

## Fellow: Tavershima Gbaa
### Interaction #2 — <json.dumps and json.loads with json.dump and json.load>
Problem:convertion of python object to json format, to json file and also byte
My initial understanding: the different between json.dumps and json.dump with json.load and loads
Prompt to AI: how to convert to json format
Useful AI guidance: it explained about the json format converstion
My independent experiment/test: converted a python structure to json string using json.dump(variable holding the python structure, the indent=4 i want it to be at)
Verification source or result: <google ai>
Decision: accept
Related file/commit: ticket.py
What I can now explain without AI: how the json work

## Fellow: Tavershima Gbaa
### Interaction #2 — <how the backend processes text into math.
Problem: Extracting numerical values from text-based ticket IDs to calculate the next unique ticket number.
My initial understanding: I was confused about how the loop variables were created, why we were stripping the letter "T", and where the tracking IDs were coming from.
Prompt to AI: please explain again, still confuse, why striping T and where did ticket_id came from
Useful AI guidance: It explained that the loop variable is a temporary label, and that we cut off the "T" because Python cannot perform mathematical operations like finding the maximum value on letters or text strings.
My independent experiment/test: Rewrote a complex one-liner list comprehension into a clean, multi-line for loop that safely uses .append() to gather the numbers into a list before running the max() math.
Verification source or result: <Google AI / Personal Script Execution>
Decision: accept
Related file/commit: ticket.py
What I can now explain without AI: How to isolate numbers from text strings using indexing, convert them to integers, and use a fallback baseline to find the highest number for a counter.
