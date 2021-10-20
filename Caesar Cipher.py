#NICHOLAS BISHOP
#Problem: Do Caesar Encryption/Decryption, including cracking a string w/ unknown Caesar key.



#basic input validations
def number_input_validator(user_input):
  try:
    x = int(user_input)
    if 0 >= x > 25:
      x = input('Please enter a number 1-25: ')
      return(number_input_validator(x))
    return(x)
  except ValueError:
    x = input("That's not a number! Please enter a positive number: ")
    return(number_input_validator(x))

def str_input_validator(user_input):
  try:
    user_input = int(user_input)
    user_input = input('Please enter an appropriate string: ')
    return(str_input_validator(user_input))
  except ValueError:
    if user_input.isalpha():
      return(user_input)
    else:
      print('Your string must not contain numbers.')
      return(str_input_validator(user_input))

#shifts the ord value of letters in input string by shift amount then creates new encoded string
def encoder(user_str,shift_amnt):
  new_str = []
  user_str = list(user_str)
  for i in range(len(user_str)):
    x = user_str[i]
    if x.isupper(): 
      letter_val = ord(user_str[i])
      letter_val += shift_amnt
      if letter_val > ord('Z'):
        letter_val -= 26
      new_str.append(chr(letter_val))
    elif x.islower():
      letter_val = ord(user_str[i])
      letter_val += shift_amnt
      if letter_val > ord('z'):
        letter_val -= 26
      new_str.append(chr(letter_val)) 
  encoded_str = ''.join(new_str)
  return(encoded_str)

#shifts the ord value of strings in the negative direction 
def decoder(user_str,shift_amnt):
  new_str = []
  user_str = list(user_str)
  for i in range(len(user_str)):
    x = user_str[i]
    if x.isupper():               #Accurate shifting for uppercase letters
      letter_val = ord(user_str[i])
      letter_val -= shift_amnt
      if letter_val < ord('A'):
        letter_val += 26
      new_str.append(chr(letter_val))
    elif x.islower():             #Accurate shifting for lowercase letters
      letter_val = ord(user_str[i])
      letter_val -= shift_amnt
      if letter_val < ord('a'):
        letter_val += 26
      new_str.append(chr(letter_val))
  return(''.join(new_str))


#Excutes what option the user chooses
def option_execute(user_choice):
  if user_choice == 'e':
    user_str = input('Enter the string to encode: ')
    user_str = str_input_validator(user_str)

    shift_amnt = input('Enter the amount to shift: ')
    shift_amnt = number_input_validator(shift_amnt)

    new_str = encoder(user_str,shift_amnt)
    print('Original String: ',user_str)
    print('Encoded String: ',new_str)

    loop()                    #allows user to use program again

  elif user_choice == 'd':
    user_str = input('Enter the string to decode: ')
    user_str = str_input_validator(user_str)

    shift_amnt = input('Enter the amount to shift: ')
    shift_amnt = number_input_validator(shift_amnt)

    new_str = decoder(user_str,shift_amnt)
    print('Original String: ',user_str)
    print('Decoded String: ',new_str)

    loop()        
                
  elif user_choice == 'q' or user_choice == 'Q':
    print('Thanks for using Caesar Cipher!')
  else:                       #user is forced to enter valid input
    user_choice = input("Please enter 'e', 'd', or 'q': ")
    return(option_execute(user_choice))


#basic program loop
def loop():
  user_choice = input("Would you like to use our program again? (Enter 'y' for yes, 'n' for no): ")
  while user_choice != 'n':
    if user_choice == 'y' or user_choice == 'Y':
      user_choice = input("Please enter 'e', 'd', or 'q' to select an option: ")
      return(option_execute(user_choice))
    else:
      user_choice = input("Please enter 'y' or 'n': ")
  print('Thanks for using Caesar Cipher!')

#program context
print('Welcome to Caesar Cipher')
print('e = Encode a String')
print('d = Decode the String')
print('q = Quit')
print('~'*25)
user_choice = input("Please enter 'e', 'd', or 'q' to select an option: ")
option_execute(user_choice)
