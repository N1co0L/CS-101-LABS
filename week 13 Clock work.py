#Nicholas Bishop


import time

class Clock:

  def __init__(self, hour = 0, minute = 0, second = 0, cl_type = 0, display = 0):
    if second > 59:
      minute += 1
      second -= 60
    if minute > 59:
      hour += 1
      minute -= 60
    '''
    #  method to initialize the time
    '''
    self.hour = hour
    self.minute = minute
    self.second = second
    self.cl_type = cl_type
    self.display = display

  def __str__(self):
    if self.display == 1:
      while self.display == 1:
        if self.second > 59:
          self.minute += 1
          self.second -= 60
        if self.minute > 59:
          self.hour += 1
          self.minute -= 60

        if self.cl_type == 0:
          print('{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second))
        elif self.cl_type == 1:
          temp = self.hour
          if self.hour > 12:
            temp -= 12
            print('{:02}:{:02}:{:02} pm'.format(temp, self.minute, self.second))
          if self.hour < 12:
            print('{:02}:{:02}:{:02} am'.format(temp, self.minute, self.second))
          elif self.hour == 0:
            temp += 12
            print('{:02}:{:02}:{:02} am'.format(temp, self.minute, self.second))
          elif self.hour == 12:
            print('{:02}:{:02}:{:02} pm'.format(temp, self.minute, self.second))
        self.second +=1
        time.sleep(1)
    else:
      if self.cl_type == 0:
          print('{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second))
      elif self.cl_type == 1:
        temp = self.hour
        if self.hour > 12:
          temp -= 12
          print('{:02}:{:02}:{:02} pm'.format(temp, self.minute, self.second))
        elif self.hour == 0:
          temp += 12
          print('{:02}:{:02}:{:02} am'.format(temp, self.minute, self.second))
        elif self.hour == 12:
          print('{:02}:{:02}:{:02} pm'.format(temp, self.minute, self.second))

  def tick(self):
    self.second += 1
    if self.second > 59:
      self.minute += 1
      self.second -= 60
    if self.minute > 59:
      self.hour += 1
      self.minute -= 60

  
      
x = int(input('What is the current hour (0-23): '))
y = int(input('What is the current minute (0-59): '))
z = int(input('What is the current second (0-59): '))
j = int(input('Enter "0" for Military Time, "1" for Standard Time: '))
k = int(input('If you would like to display your live time enter "1", else enter "0": '))

clock1 = Clock(x,y,z,j,k)
print(clock1)
clock1.tick()
print(clock1)
