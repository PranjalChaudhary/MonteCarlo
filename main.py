from random import randint

number_of_simulations = 1000
betting_amount = 1
total_money = 1000
number_of_hands = 1000
reward_amount = 4


def monte_carlo(seed, bet, total):
    balance = total
    for j in range(seed):
        x = randint(1, 6)
        y = randint(1, 6)

        if x == y:
            balance = balance + reward_amount*bet
        else:
            balance = balance - bet

    return balance


winnings = 0
for i in range(number_of_simulations):
    amount = monte_carlo(number_of_hands, betting_amount, total_money)
    if amount > total_money:
        winnings += 1

win_percentage = (winnings / number_of_simulations) * 100

print(f"The win percentage for the game will be {win_percentage} %")
