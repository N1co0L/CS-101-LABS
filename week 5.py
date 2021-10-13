
#Compares check digit to last digit in ID
def get_check_digit(library_card):
  one = ord(library_card[0]) - 65
  one = one * 1
  two = ord(library_card[1]) - 65
  two = two * 2
  three = ord(library_card[2]) - 65
  three = three * 3
  four = ord(library_card[3]) - 65
  four = four * 4
  five = ord(library_card[4]) - 65
  five = five * 5
  six = int(library_card[5])
  six = six * 6
  sev = int(library_card[6])
  sev = sev * 7
  eight = int(library_card[7])
  eight = eight * 8
  nein = int(library_card[8])
  nein = nein * 9
  ten = int(library_card[9])
  total = (one + two + three + four + five + six + sev + eight + nein)
  avg = total % 10
  if ten != avg:
    print('Your check didgit (10th character) does not match with our calcultated value')
    library_card = input('Please enter a valid library card: ')
    return(main_validator(library_card))
  else:
      return(library_card)

#get school
def get_school(library_card):
    if library_card[5] == '1':
        school = 'School of Computing and Engineering'
        return school
    elif library_card[5] == '2':
        school = 'School of Law'
        return school
    elif library_card[5] == '3':
        school = 'College of Arts and Sciences'
        return school

#get grade
def get_grade(library_card):
    if library_card[6] == '1':
        grade = 'Freshman'
        return grade
    elif library_card[6] == '2':
        grade = 'Sophomore'
        return grade
    elif library_card[6] == '3':
        grade = 'Junior'
        return grade
    elif library_card[6] == '4':
        grade = 'Senior'
        return grade

#verify is user input is 10 characters in length
def verify_length(library_card):
  char_list = list(library_card)
  if len(char_list) == 10:
    return(library_card)
  else:
    print('Input must be 10 characters in length.')
    library_card = input('Please enter a valid library card: ')
    return(main_validator(library_card))

#turns a list of the first 5 elements of user's input into a string then checks if all are letters
def verify_first_five_letters(library_card):
  char_list = list(library_card)
  first_five = char_list[0:5]
  first_five = ''.join(first_five)
  if first_five.isalpha() is True:
    return(library_card)
  else:
    print('The first 5 characters must be letters.')
    library_card = input('Please enter a valid library card: ')
    return(main_validator(library_card))

#verify 6th character
def verify_index_six(library_card):
  char_list = list(library_card)
  if int(char_list[5]) == 1 or int(char_list[5]) == 2 or int(char_list[5]) == 3:
    return(library_card)
  else:
    print("The 6th character can only be '1', '2', or '3'.")
    library_card = input('Please enter a valid library card: ')
    return(main_validator(library_card))

#verify 7th character
def verify_index_seven(library_card):
  char_list = list(library_card)
  if int(char_list[6]) != 1 and int(char_list[6]) != 2 and int(char_list[6]) != 3 and int(char_list[6]) != 4:
    print("The 7th character can only be '1', '2', '3'or '4'.")
    library_card = input('Please enter a valid library card: ')
    return(main_validator(library_card))
  else:
    return(library_card)

#checks whether the terms in a list created by getting the last three inputs from user's input, are numbers 0-9
def verify_last_three_nums(library_card):
  numlist = [0,1,2,3,4,5,6,7,8,9]

  char_list = list(library_card)
  last_three = char_list[-3:]
  for i in last_three:
    if int(i) not in numlist:
      print('The 8th, 9th, and 10th character can only be numbers [0-9]')
      library_card = input('Please enter a valid library card: ')
      return(main_validator(library_card))
    return(library_card)

#runs the user input through all the verification steps and returns the ID if it's valid
def main_validator(library_card):
  library_card = verify_length(library_card)
  library_card = verify_first_five_letters(library_card)
  library_card = verify_index_six(library_card)
  library_card = verify_index_seven(library_card)
  library_card = verify_last_three_nums(library_card)
  library_card = get_check_digit(library_card)
  return(library_card)

#program loop
def input_loop():
  library_card = input("Enter your library card ID or enter 'q' to quit:\n")
  while library_card != 'q':
    library_card = main_validator(library_card)
    print(library_card, 'is a valid library card\n')
    print("This card belongs to a student in the {}\n\nThis card belongs to a {}\n".format(get_school(library_card),get_grade(library_card)))
    library_card = input("If you'd like to continue, enter your library card ID, else enter 'q' to quit:\n")
  print('Thanks for using our program!')

input_loop()
