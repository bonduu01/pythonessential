class Timer:
    def __init__(self, hr=0, mins=0, sec=0):
        if not (0 <= sec <= 59):
            raise ValueError("Hours must be between 0 and 59")
        self.__sec = sec

        if not (0 <= mins <= 59):
            raise ValueError(" Minutes must be between 0 and 59")
        self.__min = mins

        if not (0 <= hr <= 23):
            raise ValueError("Hours is between 0 and 23")
        self.__hr = hr

    def __str__(self):
        __hour = self.__hr
        __seconds = self.__sec
        __mins = self.__min
        return f"{__hour:02}:{__mins:02}:{__seconds:02}"

    def next_second(self):
        self.__sec += 1
        if self.__sec > 59:
            self.__sec = 0
            self.__min += 1
            if self.__min > 59:
                self.__min = 0
                self.__hr += 1
                if self.__hr > 23:
                    self.__hr = 0

    def prev_second(self):
        self.__sec -= 1
        if self.__sec < 0:
            self.__sec = 59
            self.__min -= 1
            if self.__min < 0:
                self.__min = 59
                self.__hr -= 1
                if self.__hr < 0:
                    self.__hr = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
