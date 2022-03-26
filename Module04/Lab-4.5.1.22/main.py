from calendar import weekday
from datetime import datetime

class Creator:
    def __init__(self,datestr) -> None:
        self.__date = datetime.strptime(datestr, "%B %d, %Y, %H:%M:%S")

    def YMdHMS(self):
        return self.__date.strftime("%Y/%M/%d %H:%M:%S")
    
    def yBdHMSp(self):
        return self.__date.strftime("%y/%B/%d %H:%M:%S %p")
    
    def aYbd(self):
        return self.__date.strftime("%a, %Y %b %d")

    def AYBd(self):
        return self.__date.strftime("%A, %Y %B %d")
    
    def weekday(self):
        return "Weekday: "+self.__date.strftime("%w")

    def DayOfTheYear(self):
        return "Day of the year: "+self.__date.strftime("%j")
    
    def WeekOfTheYear(self):
        return "Day of the year: "+self.__date.strftime("%W")


obj = Creator("November 04, 2020, 14:53:00")
print(obj.YMdHMS())
print(obj.yBdHMSp())
print(obj.aYbd())
print(obj.AYBd())
print(obj.weekday())
print(obj.DayOfTheYear())
print(obj.WeekOfTheYear())


 