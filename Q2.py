class clockTime:
    def __init__(self):
        hours = 0
        minutes = 0
        seconds = 0

    def setHours(self, hour):
        self.hours = hour

    def setMinutes(self, minute):
        self.minutes = minute

    def setSeconds(self, second):
        self.seconds = second

    def setTime(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def showTime(self):
        final_time = str(self.hours + ":" + self.minutes + ":" + self.seconds)
        return final_time

clock = clockTime()
hr = input("input hour: ")
min = input("input minutes: ")
sec = input("input seconds: ")
clock.setHours(hr)
clock.setMinutes(min)
clock.setSeconds(sec)

time = clock.showTime()
print("Time: " + time)


