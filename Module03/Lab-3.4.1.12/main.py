class Timer:
    def __init__(self, hour=0,minutes=0,seconds=0 ):
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return ("{0:0>2d}:{1:0>2d}:{2:0>2d}".format(self.__hour, self.__minutes, self.__seconds))

    def next_second(self):
        self.__seconds+=1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes+=1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hour+=1
                if self.__hour == 24:
                    self.__hour = 0

    def prev_second(self):
        self.__seconds-=1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes-=1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hour-=1
                if self.__hour == -1:
                    self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
