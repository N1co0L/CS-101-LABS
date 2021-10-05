#NICHOLAS BISHop
#email: ncb7fv@umsystem.edu
#CS 101 LAB - Assignment 4_Week4
#Problem: create a slots machine program
##############################################################################################################



import random

#Gets a bank or total chip count - validates input to make sure it isn't a str and is between (1,100)
def get_bank(x):
  try:
    x = int(x)
    if x <= 0:
      x = input('Please enter a number greater than 0: ')
      return(get_bank(x))
    elif x > 100:
      x = input('Please enter a number less than or equal to 100: ')
      return(get_bank(x))
    return(x)
  except ValueError:
    x = input("That's not a number! Please enter a positive number: ")
    return(get_bank(x))

#gets wager and makes sure input is an integer less or equal to bank
def get_wager(bank):
  x = input('\nHow many chips would you like to wager? ')
  try:
    x = int(x)
    if x > bank:
      print('Please enter a number less than or equal to your total chips ({}): '.format(bank))
      return(get_wager(bank))
    elif x <= 0:
      print('Please enter a value greater than zero.')
      return(get_wager(bank))
    return(x)
  except ValueError:
    print("That's not a number! Please enter a positive number.")
    return(get_wager(bank))

#outputs three random numbers (1-10) tp simulate slot machine
def get_slot_results():
  x = random.randint(1, 10)
  y = random.randint(1, 10)
  z = random.randint(1, 10)
  return(x,y,z)

#counts how many times the three random values match
def get_matches(reelVal):
  count = 0
  if reelVal[0] == reelVal[1]:
    count += 1
  if reelVal[0] == reelVal[2]:
    count += 1
  if reelVal[1] == reelVal[2]:
    count += 1
  if count == 1:
    count += 1
  return(count)

#determines the payout based on matches and initial wager
def get_payout(wager, matches):
  if matches == 3:
    return((int(wager)*9))
  elif matches == 2:
    return((int(wager)*2))
  else:
    return((int(wager)*(-1)))

#Allows the user to play again if they want to
def game_loop():
  choice = input('\nWould you like to play again? Type "Y" to continue, "Q" to quit: ')
  while choice != 'Y' and choice != 'Q':
      choice = input('Please choose "Y" or "Q" ')
  if choice == 'Y':
    game()
    return(game_loop())
  elif choice == 'Q':
    return(print('Thanks for playing!'))
    

#What the user will be interacting with
def game():
  x = input("Enter the amount of chips you would like to start with (1-100): ")
  bank = get_bank(x)
  count = 0
  og_bank = bank
  winnings_list = [bank]
  while bank > 0:
    wager = get_wager(bank)
    spins = get_slot_results()
    matches = get_matches(spins)
    payout = get_payout(wager, matches)
    bank += payout
    count += 1
    winnings_list.append(bank)
    print('Your spin {} {} {}'.format(spins[0],spins[1],spins[2]))
    print('You matched {} reels'.format(matches))
    if payout > 0:
      print('You won {}'.format(payout))
    elif payout < 0:
      print('You lost {}'.format((payout)*-1))
    print('Current bank {}'.format(bank))
  print('You lost all {} chips in {} spins'.format(og_bank,count))
  print('The most chips you had was {}'.format(max(winnings_list)))
  
#start and stop of program
game()
game_loop()

    


