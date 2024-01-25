def speeding_ticket(speed, is_birthday):
    # Adjust speed limits based on the birthday condition
    if is_birthday:
        speed_limits = {'No Ticket': 65, 'Small Ticket': 85, 'Big Ticket': float('inf')}
    else:
        speed_limits = {'No Ticket': 60, 'Small Ticket': 80, 'Big Ticket': float('inf')}

    # Determine the appropriate ticket category based on the driver's speed
    for ticket, limit in speed_limits.items():
        if speed <= limit:
            return ticket

# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))   # Expected output: "No Ticket"
print(speeding_ticket(85, True))   # Expected output: "Small Ticket"