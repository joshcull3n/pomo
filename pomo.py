import time
import os
#from plyer import notification

pomo = True
plural = 'pomo'

timer = 2700  # 45 minutes
breakTime = 900  # 15 minutes

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  END = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  BOLDRED = '\x1b[1;31m'

def pomoCompleteString(num):
  os.system('clear')
  pomoSymbol = "🍅 "
  if (num == 0):
    symbols = '0'
  else:
    symbols = num*pomoSymbol
  pomoString = "pomos completed : " + symbols + '\n'
  print(pomoString)

if __name__ == "__main__":
  pomoCount = 0
  breakCount = 0
  
  while (pomo):
    # work
    count = 0
    if pomoCount > 1:
      plural = 'pomos'
    while count < timer:
      pomoCompleteString(pomoCount)
      print("the pomodoro timer has started, start working!")
      count += 1
      print(str(count), '/', str(timer))
      print()
      time.sleep(1)
    pomoCount += 1
    #notification.notify(
    #  title="good work!",
    #  message="take a 15 minute break! you have completed " +
    #  str(pomoCount) + " pomodoros so far",
    #)
    
    pomoCompleteString(pomoCount)
    print('pomo finished.')
    continuePomo = input('enter \'q\' to end the session.\npress any other key to start your break...\n\n')
    if continuePomo.lower() == 'q':
      pomo = False
      break

    # break
    count = 0
    while count < breakTime:
      pomoCompleteString(pomoCount)
      print("your break has started, enjoy.")
      count += 1
      print(str(count), ' / ', str(breakTime))
      print()
      time.sleep(1)
    breakCount += 1
    #notification.notify(
    #  title="Back to work!",
    #  message="Try doing another pomodoro...",
    #)
    pomoCompleteString(pomoCount)
    print('break finished.\n')
    continuePomo = input('enter \'q\' to end the session.\npress any other key to start the next pomo...\n\n')
    if continuePomo == 'q':
      pomo = False
  pomoCompleteString(pomoCount)
  print('you completed' + bcolors.BOLDRED, str(pomoCount), plural + bcolors.END + '!')
  print('that\'s ' + str(int((pomoCount*timer)/60)) + ' minutes of productivity and ' + str(int((breakCount*breakTime)/60)) + ' minutes of breaktime.\n')

