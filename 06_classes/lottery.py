from random import choice

combination = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d']
my_ticket = ['a','b','1','2','3']

winning_combination = []

runs = 0
while True:
    
    for _ in range (0,5):
        winning_combination.append(choice(combination))

    if winning_combination == my_ticket:
        print(f"Congratulations, your ticket has won. It took only {runs} attempts.")
        break
    else:
        runs += 1
        status = f"{my_ticket} {winning_combination} {runs}"
        winning_combination = []
        print(status)
    
    




print(f"Winning combination is: {winning_combination}\n")
print(f"Your ticket {my_ticket} took {runs}x runs to go until you hit the jackpot. Well done!")


