class Schedule:
    rating=1.0
    lectures=[]
    def __init__(self,lectures):
        self.lectures=lectures
        self.rating=1.0

    def getRating(self):
        return self.rating

    def setRating(self, rating):
        self.rating=rating

    def getClassesOnDay(self,whichDay):
        dayClasses=[]
        for currentClass in self.lectures:
            if whichDay in currentClass.getDay():
                dayClasses.append(currentClass)
        return dayClasses
