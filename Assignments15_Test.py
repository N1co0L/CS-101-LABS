import math
import unittest
import Grades

class Grade_Test(unittest.TestCase):
  def test_total_returns_total_of_list(self):
    result = Grades.total([1, 10, 22])
    self.assertEqual(result, 33, "The total function should return 33")

def test_total_returns_0(self):
  result = Grades.total([1,10,22])
  self.assertEqual(result,0,"The toal function should return 33")

def test_average_one(self):
  values = (2,5,9)
  self.assertAlmostEqual(grades.average(values),5.33333,5)
  
def test_average_two(self):
  values = (2,15,22,9)
  self.assertAlmostEqual(grades.average(values),12.0000,4)
  
def test_average_returns_nan(self):
  values = ()
  self.assertIs(grades.average(values),math.nan)

def error(self):
#self.assertRaises(ValueError, parse_int, 'N/A')
  self.assertRaises(ValueError)

def median(list):
  if len(list) <=0 :
    raise ValueError

  list.sort()
  print(list)

  if len(list) % 2 == 1 :
    index=int(len(list)/2)
    return list[index]
  else:
    index=int(len(list)/2)
    sum = list[index]+list[index-1]
    return sum/2


  print("Array index out of range error")
  unittest.main()
