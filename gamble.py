import random

def simulate():
  money = 10367
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

  # print("max money: " + str(most_money))
  # print("loops to get to max: " + str(most_loops))
  # print("amt of flips: " + str(loops))

  return (most_money, most_loops, loops)

most_money = 0
most_loops = 0
loops = 0
runs = 30000
for i in range(runs):
  sim = simulate()
  most_money += sim[0]
  most_loops += sim[1]
  loops += sim[2]

print(most_money / runs, most_loops / runs, loops / runs)


