# Question - 6
from random import randint

def isUnique(ticket : list, num : int):
    for i in ticket:
        if num == i: return False
    return True

def getLotteryTicket():
    ticket = []
    while len(ticket)<6:
        num = randint(1, 49)
        if isUnique(ticket, num):
            ticket.append(num)
    return ticket

print(f"Lottery Ticket: {str(getLotteryTicket())}")