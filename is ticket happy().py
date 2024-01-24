def is_happy_ticket(ticket):

    first = [int(i) for i in ticket[0:len(ticket)//2]]
    second = [int(i) for i in ticket[len(ticket)//2:]]

    if sum(first) == sum(second):
        return True
    else:
        return False
    

print(is_happy_ticket('123123'))
print(is_happy_ticket('341800'))

print(is_happy_ticket('42'))
print(is_happy_ticket('12345678'))
