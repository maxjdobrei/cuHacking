class Restrictions:
  timeofday=""
  breakTime=tuple()
  intensity=[]

  def __init__(self,timeofday,breakTime,intensity):
      self.timeofday= timeofday
      self.breakTime= breakTime.split(":")
      self.intensity=intensity
  def getTimeofDay(self):
      return self.timeofday

  def getbreakTime(self):
        return self.breakTime

  def getIntensity(self):
      return self.intensity
