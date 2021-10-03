#NICHOLAS BISHOP
#email: ncb7fv@umsystem.edu 
#ID: 16292909

#Summary: This program gives the user three choices, and after enterering a positive integer, the user recieves the values from whatever option they chose

#comments: This code validates all inputs, so the user must give what is asked else it will loop whatever prompt until a valid input is achieved. In addition, this program doesn't crash when you enter a string for a number input, however, you must correct your input to continue.

########################################################################################################################

#determine if input is a prime or not using formula given to us
def optionA(user_num):
  for i in range(2, int((user_num + 1)**(0.5)) + 1):
    if user_num % i == 0:
      return(print('\n{} is not prime'.format(user_num)))
  return(print('\n{} is prime'.format(user_num)))


#using a universal list, create a new list with values not found in the non-prime list >> (prime numbers list)
def optionB(user_num):
  temp_list = []
  not_prime_list = []
  prime_list = []

  for i in range(1, user_num):
    temp_list.append(i)
    for j in range(2, int((i + 1)**(0.5)) + 1):
      if i % j == 0:
        not_prime_list.append(i)
  
  for l in temp_list:
    if l not in not_prime_list:
      prime_list.append(l)

  return(prime_list)


#using the prime list created in the optionB function, add values within the list together and print when the sum equals the initial input
def optionC(prime_list,x):
  print('\nTwo prime numbers that add up to {} are:'.format(x))
  range1 = len(prime_list)//2 #only need to itterate over first half to avoid printing repeated couplets >>> [x,y] == [y,x]
  for i in prime_list:
    for j in range(range1+1):
      if prime_list[j] + i == x:
        print('{} and {}'.format(i,prime_list[j]))
        break


#Makes sure integer input is above 0 and is not a string
def number_validator(x):
  try:
    x = int(x)
    if x <= 0:
      x = input('Please enter a number greater than 0: ')
      return(number_validator(x))
    return(x)
  except ValueError:
    x = input("That's not a number! Please enter a positive number: ")
    return(number_validator(x))
  


#Gets user's number of choice and returns values with respect to the option chosen
def option_output(user_input):

  if user_input == 'A':
    x = input('Enter a positive integer: ')
    user_num = number_validator(x) 
    optionA(user_num)

  elif user_input == 'B':
    x = input('Enter a positive integer: ')
    user_num = number_validator(x)
    print('\nThe prime numbers less than',user_num,'are:')
    a = optionB(user_num)
    for x in range(len(a)):
      print('{}'.format((a[x])),end=' ')
    print()

  elif user_input == 'C':
    x = input('Enter a positive integer: ')
    user_num = number_validator(x)
    while user_num % 2 != 0:
      x = input('Please enter a EVEN input: ')
      user_num = number_validator(x)
    optionC(optionB(user_num),user_num)  


#Loops the prompts
def promptloop():
  choice = input('\nWould you like to continue? Type "Y" to continue, "Q" to quit: ')
  while choice != 'Y' and choice != 'Q':
      choice = input('Please choose "Y" or "Q"')
  if choice == 'Y':
    user_input = input('\nTo select and option, type "A", "B", or "C"\n')
    option_output(user_input)
    promptloop()
  elif choice == 'Q':
    print('\n{txt:~^100}'.format(txt = txt6))
    

#txt formatting
txt1 = 'Welcome to the prime numbers Goldback Conjecture!'
txt2 = 'OPTIONS'
txt3 = 'Find out whether or not my number is prime'
txt4 = 'List all prime numbers less than my number'
txt5 = 'Find two prime numbers that add up to my number'
txt6 = 'Thank you for using our program!'
 
print('{txt:~^100}'.format(txt = txt1))
print('\n\n{txt:^50}'.format(txt = txt2))
print('{txt:^50}'.format(txt = '-'*50))
print('\n A.) {txt}'.format(txt=txt3))
print('\n B.) {txt}'.format(txt = txt4))
print('\n C.) {txt}'.format(txt = txt5))
print('\n{txt:^50}'.format(txt = '-'*50))

#the program
user_input = input('\nTo select and option, type "A", "B", or "C"\n')
while user_input != 'A' and user_input != 'B' and user_input!= 'C':
      user_input = input('Please type "A", "B", or "C"')
option_output(user_input)
promptloop()






