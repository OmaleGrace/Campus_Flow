# Baseline check

## Test Ran
### Test command:
#### python3 main.py
#### inputed option 1 correctly for Generate Ticket
### second option for category: inputed the wrong input
### Result
#### Error message: invalid selection
#### The program restart from the begining menu
### inputed 1 again correctly for Generate Ticket after it restarted
### Result
#### New ticket id was created while the previous one where an invalid error happed was not stored in the data base
### third test
#### inputed option 4 for view Ticket
#### inputed the ticket id  that was skiped when the ivalid error happend in the first test
### Result
#### Traceback (most recent call last):
  File "/home/student/Campus_Flow_Next/main.py", line 48, in <module>
    campus_flow()
  File "/home/student/Campus_Flow_Next/main.py", line 33, in campus_flow
    view_ticket()
  File "/home/student/Campus_Flow_Next/campusflow/view_ticket.py", line 8, in view_ticket
    print(tickets_database()[choose])
          ~~~~~~~~~~~~~~~~~~^^^^^^^^
#### the error shows the item does not exist





