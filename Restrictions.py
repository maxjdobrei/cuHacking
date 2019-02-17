class Restrictions:
  timeofday=""
  breakTime=tuple()
  intensity=[]

  def __init__(self,timeofday,breakTime,intensity):

      self.timeofday= timeofday
      if breakTime != "":
        workingBreakTime=breakTime.split(":")
        self.breakTime=(workingBreakTime,(workingBreakTime[0]+1,workingBreakTime[1]))
      else:
        self.breakTime=99
      self.intensity=intensity

  def getTimeofDay(self):
      return self.timeofday

  def getbreakTime(self):
        return self.breakTime

  def getIntensity(self):
      return self.intensity
