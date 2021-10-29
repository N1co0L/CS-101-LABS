#NICHOLAS BISHOP
#ncb7fv@umsystem.edu
#LAB WEEK 9 - LIST
#WEIGHTED GRADES

import math
def menu():
  print('1 - Add Test')
  print('2 - Remove Test')
  print('3 - Clear Test')
  print('4 - Add Assignment')
  print('5 - Remove Assignment')
  print('6 - Clear Assignments')
  print('D - Display Scores')
  print('Q - Quit')

#basic number validator
def number_input_validator(user_input):
  try:
    x = float(user_input)
    if 0 >= x:
      x = input('Please enter a number greater than 0: ')
      return(number_input_validator(x))
      
    return(x)
  except ValueError:
    x = input("That's not a number! Please enter a number greater than 0: ")
    return(number_input_validator(x))

#basic input validator
def user_input_validator(user_input):
  if user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != '5' and user_input != '6' and user_input != 'D' and user_input != 'Q' and user_input != 'q':
  
    user_input = input('Please give a valid input: ')
    return(user_input_validator(user_input))

  else:
    return(user_input)

#returns a nested list of min max avg and std for assign and test and includes weighted grade
def calculations(num_of_test_scores,num_of_assignment_scores,test_scores,assignment_scores):
  data = []
  test_data = []
  assign_data = []

  if num_of_test_scores == 0:
    test_min = 'n/a'
    test_max = 'n/a'
    test_avg = 'n/a'
    test_std = 'n/a'
    test_weight = 0.00
  else:
    test_min = min(test_scores)
    test_min = '{:.2f}'.format(test_min)

    test_max = max(test_scores)
    test_max = '{:.2f}'.format(test_max)

    test_avg_num = sum(test_scores)/num_of_test_scores
    test_avg = '{:.2f}'.format(test_avg_num)

    test_std = standard_deviation(test_scores,test_avg_num)
    test_std = '{:.2f}'.format(test_std)

    test_weight = test_avg_num * 0.6

  if num_of_assignment_scores == 0:
    assign_min = 'n/a'
    assign_max = 'n/a'
    assign_avg = 'n/a'
    assign_std = 'n/a'
    assign_weight = 0.00
  else:
    assign_min = min(assignment_scores)
    assign_min = '{:.2f}'.format(assign_min)

    assign_max = max(assignment_scores)
    assign_max = '{:.2f}'.format(assign_max)

    assign_avg_num = sum(assignment_scores)/num_of_assignment_scores

    assign_avg = '{:.2f}'.format(assign_avg_num)

    assign_std = standard_deviation(assignment_scores,assign_avg_num)
    assign_std = '{:.2f}'.format(assign_std)

    assign_weight = assign_avg_num * 0.4

  weighted_score = test_weight + assign_weight
  weighted_score = '{:.2f}'.format(weighted_score)

  test_data.append(test_min)
  test_data.append(test_max)
  test_data.append(test_avg)
  test_data.append(test_std)

  assign_data.append(assign_min)
  assign_data.append(assign_max)
  assign_data.append(assign_avg)
  assign_data.append(assign_std)

  data.append(weighted_score)
  data.append(test_data)
  data.append(assign_data)
  return(data)

#returns standard deviation of given list
def standard_deviation(scores_list,score_average):
  temp_list = []
  for i in scores_list:
    num = (i - score_average) ** 2
    temp_list.append(num)
  temp_avg = sum(temp_list)/len(temp_list)
  std = math.sqrt(temp_avg)
  return(std)

#prints data from nested list
def display_scores(test_scores,assignment_scores):
  test_len = len(test_scores)
  assignment_len = len(assignment_scores)

  #[weighted score, [test data],[assignment data]]
  #                  ^^^  [min,max,avg,std]  ^^^
  data_list = calculations(test_len,assignment_len,test_scores,assignment_scores)

  print()
  format_str = '{types:20}{number:<10}{min:10}{max:10}{avg:10}{std:10}'
  print(format_str.format(types= 'Type',number= '#',min= 'min',max= 'max',avg= 'avg',std= 'std'))
  print('='*64)

  print(format_str.format(types= 'Tests',number= test_len,min= data_list[1][0],max= data_list[1][1],avg= data_list[1][2],std= data_list[1][3]))

  print(format_str.format(types= 'Assignments',number= assignment_len,min= data_list[2][0],max= data_list[2][1],avg= data_list[2][2],std= data_list[2][3]))

  print('\nThe weighted score is', data_list[0])

test_scores = []
assignment_scores = []
menu()
user_input = input('\nSelect an option above: ')
user_input = user_input_validator(user_input)

#loops user_inputs through options until q is entered
while user_input != 'Q' and user_input != 'q':
  if user_input == '1':
    test_score = input('Enter the new test score (1-100): ')
    test_score = number_input_validator(test_score)
    test_scores.append(test_score)

    user_input = input('\nSelect another option or enter "Q" to quit: ')
    user_input = user_input_validator(user_input)
  
  elif user_input == '2':
    if len(test_scores) == 0:
      user_input = input('\nThere are no test scores, please select another option: ')
      user_input = user_input_validator(user_input)
    else:
      test_score = input('Enter the test score to remove (1-100): ')
      test_score = number_input_validator(test_score)
      while test_score not in test_scores:
        test_score = input('Unable to find score, please enter another score: ')
        test_score = number_input_validator(test_score)
      test_scores.remove(test_score)

      user_input = input('\nSelect another option or enter "Q" to quit: ')
      user_input = user_input_validator(user_input)
  
  elif user_input == '3':
    test_scores.clear()
    print('Test scores have been cleared.\n')

    user_input = input('\nSelect another option or enter "Q" to quit: ')
    user_input = user_input_validator(user_input)
  
  elif user_input == '4':
    assignment_score = input('Enter the new assignemnt score (1-100): ')
    assignment_score = number_input_validator(assignment_score)
    assignment_scores.append(assignment_score)

    user_input = input('\nSelect another option or enter "Q" to quit: ')
    user_input = user_input_validator(user_input)
  
  elif user_input == '5':
    if len(assignment_scores) == 0:
      user_input = input('\nThere are no assignment_scores, please select another option: ')
      user_input = user_input_validator(user_input)
    else:
      assignment_score = input('Enter the assignment score to remove (1-100): ')
      assignment_score = number_input_validator(assignment_score)
      while assignment_score not in assignment_scores:
        assignment_score = input('Unable to find score, please enter another score: ')
        assignment_score = number_input_validator(assignment_score)
      assignment_scores.remove(assignment_score)

      user_input = input('\nSelect another option or enter "Q" to quit: ')
      user_input = user_input_validator(user_input)

  elif user_input == '6':
    assignment_scores.clear()
    print('Assignment scores have been cleared.\n')

    user_input = input('\nSelect another option or enter "Q" to quit: ')
    user_input = user_input_validator(user_input)
    

  elif user_input == 'D':
    display_scores(test_scores,assignment_scores)

    user_input = input('\nSelect another option or enter "Q" to quit: ')
    user_input = user_input_validator(user_input)

print('Thanks!')
