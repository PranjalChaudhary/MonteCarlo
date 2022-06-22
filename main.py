from random import randint

number_of_simulations = 1000
betting_amount = 1
total_money = 1000
number_of_hands = 1000
reward_amount = 5


def monte_carlo(seed, bet, total):
    """Simulates seed amount of game where the player wins the bet times the reward amount if both die rolls are
    same and loses the bet amount if not """
    balance = total
    for j in range(seed):
        x = randint(1, 6)
        y = randint(1, 6)

        if x == y:
            balance = balance + reward_amount*bet
        else:
            balance = balance - bet

    return balance


wins = 0
winnings = 0
for i in range(number_of_simulations):
    amount = monte_carlo(number_of_hands, betting_amount, total_money)
    winnings += amount
    if amount > total_money:
        wins += 1

win_percentage = (wins / number_of_simulations) * 100
average_winnings = winnings/number_of_simulations

print(f"The win percentage for the game will be {win_percentage} %")
print(f"The average balance at the end of the game is {average_winnings}")
