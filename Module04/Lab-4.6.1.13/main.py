from calendar import Calendar

class ExtendedCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday=0):
        count = 0
        for month in range(1,13):
            for data in self.monthdays2calendar(year,month): 
                if data[weekday][0] !=0:
                    count+=1 
        return count

obj = ExtendedCalendar()
print(obj.count_weekday_in_year(2019) == 52) 
print(obj.count_weekday_in_year(2000,6) == 53) 
