#Nicholas Bishop
#ncb7fv@umsystem.edu


import string
import os.path

#used for sorting dictionary by word frequescy
def get_ranking(item):
  return int(item[1]['Freq'])

def read_file(file_name):
  file_1 = open(file_name)
  txt_1 = file_1.read()
  words = txt_1.split()

  #takes list of words then removes punctuation from each word and appends it
  word_list = []
  for s in words:
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in exclude)
    s = s.lower()
    word_list.append(s)
  
  #string formatting
  format_str = '{num:<10}{word:20}{freq:3}'
  print('Most frequently used words:')
  print(format_str.format(num='#', word= 'Word', freq= 'Freq.'))
  print('='*35)

  #making sets,lists, and dictionaries
  word_set = set(word_list)
  word_dict = {}
  single_use_words = []
  count = 0
  
  for word in word_set:
    if len(word) > 3:
      z = word_list.count(word)
      if z == 1:
        single_use_words.append(z)
      word_dict[word] = {}
      word_dict[word]['Freq'] = z
  
  #sorting dict by frequency
  ordered_dict = dict(sorted(word_dict.items(),key=get_ranking, reverse=True))
  
  #displaying results
  for i in ordered_dict:
    count += 1
    print(format_str.format(num= count, word= i, freq= word_dict[i]['Freq']))
    if count == 10 or count == len(ordered_dict):
      break

  print('\nThere are {} words that occur only once'.format(len(single_use_words)))
  print('There are {} unique words'.format(len(ordered_dict)))

#start program
user_input = input('Enter the name of the file you would like to analyze: ')
while user_input != 'q' and user_input != 'Q':
  try:
    read_file(user_input)
  except:
    user_input = input('File not found, please try again or press "Q" to quit: ')
  user_input = input('Would you like to analyze another file?\nIf so enter file name, if not press "Q" to quit: ')
print('Thanks for using our program!')
