#NICHOLAS BISHOP

import csv
def get_month_from_number():
  months_by_num = {'01': 'January',
  '02': 'February',
  '03': 'March',
  '04': 'Apirl',
  '05': 'May',
  '06': 'June',
  '07': 'July',
  '08': 'August',
  '09': 'September',
  '10': 'October',
  '11': 'November',
  '12': 'December',
  }
  return months_by_num

def file_list(file_name):
  try:
    file1 = open(file_name,'r')
    data_list = []
    data_reader = csv.reader(file1, delimiter= ',')
    for row in data_reader:
      data_list.append(row)
    data_list.pop(0)
    return(data_list)
  except:
    file_name = input('File does not exist, please enter a valid file name: ')
    return(file_list(file_name))

def get_report_date_dict(main_list):
  report_date_dict = {}
  for key in range(len(main_list)):
    try:
      report_date_dict[main_list[key][1]]['number of crimes'] += 1
    except KeyError:
      report_date_dict[main_list[key][1]] = {}
      report_date_dict[main_list[key][1]]['number of crimes'] = 1
  return(report_date_dict)

def get_reported_month_dict(main_list,months_dict):
  month_dict = {}
  for key in range(len(main_list)):
    temp_list = (main_list[key][1]).split('/')
    month = months_dict[temp_list[0]]
    try:
      month_dict[month]['number of crimes'] += 1
    except KeyError:
      month_dict[month] = {}
      month_dict[month]['number of crimes'] = 1
  return(month_dict)

def get_offense_dict(main_list):
  offense_dict = {}
  for key in range(len(main_list)):
    try:
      offense_dict[main_list[key][7]] += 1
    except KeyError:
      offense_dict[main_list[key][7]] = {}
      offense_dict[main_list[key][7]] = 1
  return(offense_dict)

def get_offense_by_zip(main_list):
  zip_dict = {}
  for key in range(len(main_list)):
    offense = main_list[key][7]
    zips = main_list[key][13]
    if offense in zip_dict:
      temp_dict = zip_dict[offense]
      if zips in temp_dict:
        temp_dict[zips] += 1
      else:
        temp_dict[zips] = 1
    else:
      zip_dict[offense] = {zips: 1}
  return(zip_dict)

if __name__ == "__main__":
  #file_name = input('Enter the name of file you are reading (KCPD_Crime_Data_2019.csv) or (CrimeDataSmall.csv): ')
  file_name = 'CrimeDataSmall.csv'
  data_list = file_list(file_name)
  months_dict = get_month_from_number()
  offense_dict = get_offense_dict(data_list)
  zip_dict = get_offense_by_zip(data_list)
  month_report_dict = get_reported_month_dict(data_list,months_dict)
  report_dict = get_report_date_dict(data_list)

  max_val = max(month_report_dict, key = month_report_dict.get)
  print("The month with the highest number of crimes is {} with {} offenses.\n".format(max_val, month_report_dict[max_val]['number of crimes']))

  max_val = max(offense_dict, key = offense_dict.get)
  print("The offense with the highest number of crimes is {} with {} offenses.\n".format(max_val, offense_dict[max_val]))

  while(True):
    offense = input('Enter an offense you would like to search by zip code: ')
    if offense not in zip_dict:
      print("Please enter a valid offense: ")
    else:
      break
  print('{} occurs {} times in zip code: {}'.format(offense, zip_dict[offense]))
