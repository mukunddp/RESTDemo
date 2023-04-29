import calendar
from datetime import datetime

current = datetime.now()
dt = current.strftime("%m/%d/%Y, %H:%M:%S")
print(dt)


yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

