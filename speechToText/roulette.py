import random
import matplotlib.pyplot as plt

bankroll = 250
random.seed()
total_bankroll = 5000
loss_streak = 0
outcome = "loss"
bet = 1
times_left_in_profit = 0
times_left_in_loss = 0
bankrolls = []
visits = []
for j in range(1200):
    total_bankroll -= 250
    if total_bankroll <= 0:
        print("Lost it all")
        break
    print(f"Total bankroll at ${total_bankroll}")
    bankroll = 256
    bet = 1
    for i in range(1,100):
        roll = random.randint(0,36)
        if bankroll < bet:
            print(f"Went Broke, Bank roll at {bankroll}, bet at {bet}, loss streak at {loss_streak}")
            print(f"You went broke after {(i*2)//60} hour(s), {((i*2)%60)} minutes.")
            times_left_in_loss+=1
            break
        if (roll % 2) == 1:
            loss_streak = 0
            bankroll+= bet
            bet = 1
        elif roll == 0:
            loss_streak+=1
            bankroll = bankroll - bet
            bet = bet*2
        else:
            loss_streak+=1
            bankroll = bankroll - bet
            bet = bet*2
    times_left_in_profit+=1
    total_bankroll += bankroll
    bankrolls.append(total_bankroll)
fig, ax = plt.subplots()
for a in range(len(bankrolls)):
    visits.append(a+1)
ax.scatter(visits, bankrolls, 10)
ax.set_title('Rjs Gambling Addiction')
ax.set_xlabel('Visits')
ax.set_ylabel('Bankroll')
plt.show()

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# chance = [times_left_in_profit/times_left_in_loss]
# options = ["Chance of leaving in profit"]
# ax.bar(options, chance)
# ax.set_title('Rjs Gambling Addiction')
# ax.set_xlabel('Visits')
# ax.set_ylabel('Bankroll')
# plt.show()

print(f"Ending Bankroll ${total_bankroll}, chance of profit {times_left_in_profit/times_left_in_loss}")
