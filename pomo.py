import time
import os
from plyer import notification

pomo = True
count = 0
timer = 2700  # 45 minutes
breakTime = 900  # 15 minutes
pomoCount = 0

if __name__ == "__main__":
  while (pomo):
    # work
    count = 0
    while count < timer:
      os.system('clear')
      print("The pomodoro timer has started, start working!")
      count += 1
      print(str(count), '/', str(timer))
      time.sleep(1)
    pomoCount += 1
    notification.notify(
      title="Good work!",
      message="Take a 15 minute break! You have completed " +
      str(pomoCount) + " pomodoros so far",
    )
    # os.system('clear')
    print('pomo finished.')
    input('press any key to start your break...')

    # break
    count = 0
    while count < breakTime:
      os.system('clear')
      print("Your break has started, enjoy.")
      count += 1
      print(str(count), ' / ', str(breakTime))
      time.sleep(1)
    notification.notify(
      title="Back to work!",
      message="Try doing another pomodoro...",
    )
    print('break finished.')
    continuePomo = input('start another pomo? (Y/n) : ')
    if continuePomo == 'n':
      pomo = False
  os.system('clear')
  print('you completed', str(pomoCount), 'pomo(s).')
