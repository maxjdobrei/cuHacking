#courseCode,Time,location,day,tutorialsdays
#courseCode,Time,location,day
from Schedule import *
from Lecture import *
from Tutorial import *
from cuScheduling import *


compa = []
compa1 = Tutorial("COMP1405A1", "4:35 - 5:55", "Mon Wed")
compa2 = Tutorial("COMP1405A1", "4:35 - 5:55", "Mon Wed")
compa.append(compa1)
compa.append(compa2)



comp = Lecture("COMP1405A", "10:00 - 11:35", "Tue Thu", compa)


result = createSchedules(comp)