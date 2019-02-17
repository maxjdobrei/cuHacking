class Tutorial:
    startTime=tuple()
    endTime=tuple()
    location=""
    days=[]
    courseCode=""
def __init__(self,courseCode,Time,location,day):
    Time=Time.split("-")
    Start= Time[0].split(":")
    End= Time[1].split(":")

    self.courseCode=courseCode
    self.startTime= (int(Start[0]), int(Start[1]))
    self.endTime= (int(End[0]), int(End[1]))
    self.location=location
    self.days=convertDay(day)

def convertDay(self,day):
    dayNum=[]
    tempdays=day.strip().split(" ")
    for days in tempdays:
        if days=="Mon":
            dayNum.append(0)
        elif days == "Tue":
            dayNum.append(1)
        elif days == "Wed":
            dayNum.append(2)
        elif days == "Thu":
            dayNum.append(3)
        elif days == "Fri":
            dayNum.append(4)
    return dayNum

def getTimes(self):
	return (self.startTime, self.endTime)

    def getDay(self):
        return self.days
