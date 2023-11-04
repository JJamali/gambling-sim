import random

money = 45000
most_money = money
most_loops = 0
loops = 0
initial_bet = 50
bet = initial_bet

while money > 0:
  loops += 1
  if random.random() < 0.5:
    money -= bet
    bet = min(bet*2, money) 
  else:
    money += bet
    bet = initial_bet

  if most_money < money:
    most_money = money
    most_loops = loops

print("max money: " + str(most_money))
print("loops to get to max: " + str(most_loops))
print("amt of flips: " + str(loops))
