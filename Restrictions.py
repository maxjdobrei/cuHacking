class Restrictions:
  timeofday=""
  breakTime=tuple()
  intensity=[]

  def __init__(self,timeofday,breakTime,intensity):
      self.timeofday= timeofday
      self.breakTime= breakTime.split(":")
      self.intensity=intensity
