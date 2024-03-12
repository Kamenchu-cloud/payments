from collections import defaultdict

def solution(A, D):
    # Acc bal in 2020 == 0
    # If amount === <0 then payment was made by card else it was an incoming transfer.
    # Fee of 5$ every month deducted unless 3 or more payments made by card for a total of 100$ or more in that month.
    # Given array A(with N intengers) and Array D(with N strings)
    # N is an integer within the range [1..100];
    # each element of array A is an integer within the range [−1,000..1,000];
    # D contains strings in YYYY−MM−DD format, representing dates in the range 2020−01−01 to 2020−12−31.

    # Use a for loop

    balance = 0
    card_payments = defaultdict(int)
    
    for amount, date in zip(A, D):
        year, month, _ = map(int, date.split("-"))
        
        # Update card payments for the month
        if amount < 0:
            card_payments[(year, month)] += abs(amount)
        
        # Update balance based on incoming transfer
        else:
            balance += amount
        
        # Apply fee at the end of the month if needed
        if month < 12:
            card_payment_total = sum(card_payments[(year, m)] for m in range(month, month + 3))
            if card_payment_total < 100:
                balance -= 5
    
    return balance


result = solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"])
print(result)