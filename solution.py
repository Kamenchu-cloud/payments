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
    card_payments = (int)

    for amount, date in (A,D):
        year, month, _ = date.split('-')
        if amount < 0:
            balance += amount
            card_payments[month] += 1
        else:
            balance += amount

        if month in card_payments and card_payments[month] <3 and sum(card_payments.values()) < 100:
            balance -= 5

    return balance