import math

def total(values):
  flt = float(sum(values))
  return(flt)

def average(values):
  if len(values) == 0:
    return math.nan
  sum = 0
  for val in values:
    sum = sum + val
  return sum/len(values)

def median(list):
  list.sort()
  print(list)
  #check if list has odd number of elements
  if len(list) % 2 == 1 :
    index=int(len(list)/2)
    return list[index]
  else:
    index=int(len(list)/2)
    sum = list[index]+list[index-1]
    return sum/2
