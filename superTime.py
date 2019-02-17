from	bs4	import	BeautifulSoup
import	urllib.request
import	mechanicalsoup
from	cuSchedulingParser	import	*
from	cuScheduling	import	*
from	Lecture	import	*
from	Tutorial	import	*
from	Restrictions	import	*

def	superMain(term,classes,hardTime,timeOfDay):
	rankedResults	=	[]
	listoBisto	=	[]
	if	timeOfDay=="":
		timeofDay="Afternoon"	
	if	hardTime=="":
		hardTime="1:00"
	restrictions	=	0
	restrictions	=	Restrictions(timeOfDay,	hardTime,classes)
	results	=	createSchedules(main(term,classes))[:]
	for	result	in	results:
		scheduleRanker(result,restrictions)
		rankedResults.append(result.getRating())
	rankedResults.sort()
	rankedResults.reverse()
	
	toBeCopied	=	[]
	bestFive	=	[]
	if	len(rankedResults)	>=	10:
		for	i	in	range(10):
			temp	=	bestFive
			bestFive.append(getSchedule(results,temp,	rankedResults[i]))
			toBeCopied.append(bestFive[0])
			toBeCopied.append(bestFive[2])
			toBeCopied.append(bestFive[4])
			toBeCopied.append(bestFive[6])
			toBeCopied.append(bestFive[8])
	else:
		for	i	in	range(len(rankedResults)):
			temp	=	bestFive[:]
			bestFive.append(getSchedule(results,temp,	rankedResults[i]))
	for	sched	in	bestFive:
		if	sched	is	not	None:
			listoBisto.append(scheduleParser(sched))
	return	listoBisto

print(superMain("Winter",["COMP1406","MATH1104"],"3:30","Afternoon"))
print(superMain("Winter",["COMP1805","ENST1020"],"3:30","Afternoon"))