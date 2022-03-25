class WeekDayError(Exception):
    pass
	

class Weeker:
    allowDays=('Mon','Tue','Web','Thu','Fri','Sat','Sun')

    def __init__(self, day):
        if day not in self.allowDays:
            raise WeekDayError()
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        pos = self.allowDays.index(self.__day)+n%7
        self.__day = self.allowDays[pos]

    def subtract_days(self, n):
        pos = self.allowDays.index(self.__day)-n%7 
        self.__day = self.allowDays[pos]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")