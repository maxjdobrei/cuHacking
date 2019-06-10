from Schedule import *
from Restrictions import *

validSchedules = []




def createSchedules(lecturesFound):
	try:
		if lecturesFound == "":
			return []
	except:
		if len(lecturesFound) == 0:
			return []

	tempSchedule = [0,0,0,0,0,0]

	# testDict = {}

	# for lecture in lecturesFound:
	# 	testDict[lecture.getCoursecode()] = lecture.getDay()
	# createSchedulesHelperTest(lecturesFound, 0, testDict)
	



	for lec in lecturesFound[0]:
		tempSchedule.pop(0)
		tempSchedule.insert(0, lec)
		try:
			for lect in lecturesFound[1]:
				tempSchedule.pop(1)
				tempSchedule.insert(1, lect)
				try:
					for lectu in lecturesFound[2]:
						tempSchedule.pop(2)
						tempSchedule.insert(2, lectu)
						try:
							for lectur in lecturesFound[3]:
								tempSchedule.pop(3)
								tempSchedule.insert(3, lectur)
								try:
									for lecture in lecturesFound[4]:
										tempSchedule.pop(4)
										tempSchedule.insert(4, lecture)
										try:
											for lectureFinal in lecturesFound[5]:
												tempSchedule.pop(5)
												tempSchedule.insert(5, lectureFinal)
												if scheduleValidator(tempSchedule):
													temp = tempSchedule
													tutorialVersions = addTutorials(temp)
													if len(tutorialVersions) != 0:
														for version in tutorialVersions:
															temp = Schedule(version)
															validSchedules.append(temp)


										except:
											tempSchedule = removeNull(tempSchedule)
											if scheduleValidator(tempSchedule):
												temp = tempSchedule
												tutorialVersions = addTutorials(temp)
												if len(tutorialVersions) != 0:
													for version in tutorialVersions:
														temp = Schedule(version)
														validSchedules.append(temp)
											continue
								except:
									tempSchedule = removeNull(tempSchedule)
									if scheduleValidator(tempSchedule):
										temp = tempSchedule
										tutorialVersions = addTutorials(temp)
										if len(tutorialVersions) != 0:
											for version in tutorialVersions:
												temp = Schedule(version)
												validSchedules.append(temp)
									continue
						except:
							tempSchedule = removeNull(tempSchedule)
							if scheduleValidator(tempSchedule):
								temp = tempSchedule
								tutorialVersions = addTutorials(temp)
								if len(tutorialVersions) != 0:
									for version in tutorialVersions:
										temp = Schedule(version)
										validSchedules.append(temp)
							continue
				except:
					tempSchedule = removeNull(tempSchedule)
					if scheduleValidator(tempSchedule):
						tutorialVersions = addTutorials(tempSchedule)
						if len(tutorialVersions) != 0:
							for version in tutorialVersions:
								temp = Schedule(version)
								validSchedules.append(temp)
					continue
		except:
			tempSchedule = removeNull(tempSchedule)
			if scheduleValidator(tempSchedule):
				temp = tempSchedule
				tutorialVersions = addTutorials(temp)
				if len(tutorialVersions) != 0:
					for version in tutorialVersions:
						temp = Schedule(version)
						validSchedules.append(temp)
			continue
	return validSchedules


# def createSchedulesHelperTest(Lectures, index, dict):
# 	if index != len(Lectures):
# 		potentialSchedule = []
# 		courseCode = Lectures[index].getCourseCode()
# 		sections = dict[courseCode]
# 		for section in sections:
# 			potentialSchedule.append(section)
# 			if overlapCheckerTwo(potentialSchedule):
# 				createSchedulesHelperTest(Lectures, index+1, dict)
# 			else:
# 				potentialSchedule.pop(index)




def removeNull(potentialSchedule):
	indexesToRemove = []
	for i in range(len(potentialSchedule)):
		if potentialSchedule[i] == 0:
			indexesToRemove.append(i)
	for index in indexesToRemove:
		potentialSchedule.remove(index)         #changed from remove(0) -> remove remove(index)

	return potentialSchedule


def scheduleValidator(potentialSchedule):
	return overlapCheckerTwo(potentialSchedule)


def overlapChecker(potentialSchedule, lecture):
	temp = lecture.getTimes()                    
	times = []


	tempSched = Schedule(potentialSchedule)
	for i in range(5):
		dayClasses = tempSched.getClassesOnDay(i)
		for lect in dayClasses:
			times.append(lect.getTimes())

		for time in times:
			if temp[0][0] == time[1][0]:                               #if the start hour is the same as the other end hour, compare minutes
				if temp[0][1] <= time[1][1]:
					return False
			elif temp[1][0] == time[0][0]:                             #if the end time is the same as the other start time, compare minutes
				if temp[1][1] <= time[0][1]:
					return False
			elif temp[0][0] > time[0][0] and temp[0][0] < time[1][0]:  #if the start hour is inbetween start and end hours of the thing from schedule
				return False

	return True


def overlapCheckerTwo(potentialSchedule):

	timez = []
	tempSched = Schedule(potentialSchedule)

	for i in range(5):
		dayClasses = tempSched.getClassesOnDay(i)
		timez.clear()
		for lect in dayClasses:
			timez.append(lect.getTimes())

			for i in range(len(timez)):
				for j in range(i, len(timez)):
					#if time[0][1] or time[1][1]
					time = timez[i]
					timeTwo = timez[j]
					if time!=timeTwo:
						if time[0][0] == timeTwo[1][0]:  
							if time[0][1] <= timeTwo[1][1]:
								return False
						elif time[1][0] == timeTwo[0][0]:
							if time[1][1] <= timeTwo[0][1]:
								return False
						elif time[0][0] > timeTwo[0][0] and time[0][0] < timeTwo[1][0]:
							return False
	return True




def addTutorials(potentialSchedule):
	tutLengths = []

	for lecture in potentialSchedule:
		if len(lecture.getTutorials()) == 0:
			tutLengths.append(-1)
		else:
			tutLengths.append(len(lecture.getTutorials()))

	lecturesWithTutorials = []
	for i in range(len(tutLengths)):
		if tutLengths[i] != -1:
			lecturesWithTutorials.append(potentialSchedule[i])

	return addTutorialsHelper(potentialSchedule, lecturesWithTutorials)



def addTutorialsHelper(potentialSchedule, lectures):



	result = []
	indexCounter = []
	for i in range(len(lectures)):
		indexCounter.append(0)

	foundSomething = False
	tutorialsToCheck = True
	listOfSchedules = []
	holder = 0
	counter = 0

	while tutorialsToCheck:
		foundSomething = False
		listOfSchedules.clear()
		listOfSchedules.append(potentialSchedule)
		holder = indexCounter[0]
		counter = 0

		for i in range(len(lectures)):
			for j in range(indexCounter[i], len(lectures[i].getTutorials())):

				if overlapChecker(listOfSchedules[counter], lectures[i].getTutorials()[j]):
					foundSomething = True
					temp = listOfSchedules[counter][:]            ###################################################################################################
					temp.append(lectures[i].getTutorials()[j])
					for resultSched in result:
						if temp == resultSched:
							foundSomething = False
							indexCounter[i] = len(lectures[i].getTutorials())
					else:
						if j ==  (len(lectures[i].getTutorials()) - 1):
							indexCounter[i] = 0
						else:
							indexCounter[i] = j + 1
						if len(temp) == (len(potentialSchedule) + len(lectures)):
							result.append(temp)
						else:
							listOfSchedules.append(temp)
							counter += 1
							break
				else:
					foundSomething = False
					break
			if foundSomething == False:
				tutorialsToCheck = False
		if foundSomething == False:
				tutorialsToCheck = False

	return result

def scheduleRanker(schedule, restrictions):
	firstRank=0.45
	secondRank=0.20
	thirdRank=0.35
	classRange=tuple()
	breakTime=tuple()


	if (restrictions.getTimeofDay()=="Morning"):
		classRange=(8,12)

	elif (restrictions.getTimeofDay()=="Afternoon"):
		classRange=(13,17)
	elif (restrictions.getTimeofDay()=="Evening"):
	 	classRange=(18,21)

	breakTime=restrictions.getbreakTime()


	for j in range(5):
		currentClassesOnDay=schedule.getClassesOnDay(j)
		
		classMetPref = 0
		classNotMetPref = 0
		# for course in currentClassesOnDay:
		# 	try:
		# 		course.getTutorials()
		# 	except:
		# 		currentClassesOnDay.remove(course)
	
		for classes in currentClassesOnDay:
			temp=classes.getTimes()
			if restrictions.getTimeofDay()=="":
				break

			elif temp[0][0] <classRange[0] or temp[1][0]>classRange[1]:
				classNotMetPref += 1
		classMetPref = len(currentClassesOnDay) - classNotMetPref
		if classNotMetPref == 0:
			classNotMetPref = 1
		if classMetPref == 0:
			difference = 0.09
		else:
			difference = 0.09 / (classMetPref / classNotMetPref)
		firstRank -= difference

	for i in range(5):
		currentClassesOnDay=schedule.getClassesOnDay(i)
		
		
		if not (len(currentClassesOnDay) == 0):
			differenceIntensity=(0.07/len(currentClassesOnDay))*2
			oldIntensity=restrictions.getIntensity().index(currentClassesOnDay[0].getCoursecode())
		else:
			differenceIntensity = 0
			oldIntensity=0

		for currentClass in currentClassesOnDay:
			temp=currentClass.getTimes()


			if breakTime=="":
				pass
			elif temp[0][0]> int(breakTime[0][0]) and temp[1][0]< int(breakTime[1][0]):
				secondRank=secondRank-0.04
			try:
				throwAway=currentClass.getTutorials()

				if oldIntensity==restrictions.getIntensity().index(currentClass.getCoursecode())-1 or oldIntensity==restrictions.getIntensity().index(currentClass.getCoursecode())+1:
					thirdRank=thirdRank-differenceIntensity
				oldIntensity=restrictions.getIntensity().index(currentClass)
			except:
				pass
	if (firstRank+secondRank+thirdRank>1.0):
		schedule.setRating(1)
	else:
		schedule.setRating(firstRank+secondRank+thirdRank)

def dayTo(day):
	if day == 0:
		return "Monday"
	elif day == 1:
		return "Tuesday"
	elif day == 2:
		return "Wednesday"
	elif day == 3:
		return "Thursday"
	elif day == 4:
		return "Friday"


def lectureParser(lecture,i):
	listOfDays = lecture.days
	newListOfDays = []
	for day in listOfDays:
		newListOfDays.append(dayTo(day))
	returnedDict = {"name":lecture.courseCode,"location":lecture.location,"days":newListOfDays, "startTime":lecture.startTime,"endTime":lecture.endTime,"color":i}
	return returnedDict

def scheduleParser(schedule):
	lecturesList = []
	i=0
	if schedule is not None:
		for lecture in schedule.lectures:
			if len(lecture.courseCode) == 9:
				i +=1
				lecturesList.append(lectureParser(lecture,i))
		newLecturesList = lecturesList[:]
		for tutorial in schedule.lectures:
			if len(tutorial.courseCode) == 10:
				for lecture in newLecturesList:
					if lecture['name'] in tutorial.courseCode:
						lecturesList.append(lectureParser(tutorial,lecture['color']))
	return lecturesList
