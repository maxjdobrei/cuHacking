from Schedule import *
from Restrictions import *

validSchedules = []




def createSchedules(lecturesFound):
	tempSchedule = [0,0,0,0,0,0]

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
													tutorialVersions = addTutorials(tempSchedule)
													if len(tutorialVersions) != 0:
														temp = Schedule(tempSchedule)
														validSchedules.append(temp)

										except:
											if scheduleValidator(tempSchedule):
													tutorialVersions = addTutorials(tempSchedule)
													if len(tutorialVersions) != 0:
														temp = Schedule(tempSchedule)
														validSchedules.append(temp)
											continue
								except:
									if scheduleValidator(tempSchedule):
										tutorialVersions = addTutorials(tempSchedule)
										if len(tutorialVersions) != 0:
											temp = Schedule(tempSchedule)
											validSchedules.append(temp)
									continue
						except:
							if scheduleValidator(tempSchedule):
								tutorialVersions = addTutorials(tempSchedule)
								if len(tutorialVersions) != 0:
									temp = Schedule(tempSchedule)
									validSchedules.append(temp)
							continue
				except:
					if scheduleValidator(tempSchedule):
						tutorialVersions = addTutorials(tempSchedule)
						if len(tutorialVersions) != 0:
							temp = Schedule(tempSchedule)
							validSchedules.append(temp)
					continue
		except:
			if scheduleValidator(tempSchedule):
				tutorialVersions = addTutorials(tempSchedule)
				if len(tutorialVersions) != 0:
					temp = Schedule(tempSchedule)
					validSchedules.append(temp)
			continue
	return validSchedules



def scheduleValidator(potentialSchedule):
	return overlapCheckerTwo(potentialSchedule)


def overlapChecker(potentialSchedule, lecture):
	temp = lecture.getLectureTimes()
	times = []
	for lecture in potentialSchedule:
		times.append(lecture.getTimes())


	for time in times:
		if temp[0][0] == time[1][0]:
			if temp[0][1] <= time[1][1]:
				return False
		elif temp[1][0] == time[0][0]:
			if temp[1][1] <= time[0][1]:
				return False
		elif temp[0][0] > time[0][0] and temp[0][0] < time[1][0]:
			return False

	return True


def overlapCheckerTwo(potentialSchedule):

	times = []
	for lecture in potentialSchedule:
		if len(times) == 0:
			times.append(lecture.getTimes())
		else:
			temp = lecture.getLectureTimes()
			for time in times:
				if temp[0][0] == time[1][0]:
					if temp[0][1] <= time[1][1]:
						return False
				elif temp[1][0] == time[0][0]:
					if temp[1][1] <= time[0][1]:
						return False
				elif temp[0][0] > time[0][0] and temp[0][0] < time[1][0]:
					return False
	return True




def addTutorials(potentialSchedule):
	tutLengths = []

	for lecture in potentialSchedule:
		if len(lecture.getTutorials) == 0:
			tutLengths.append(-1)
		else:
			tutLengths.append(len(lecture.getTutorials))

	lecturesWithTutorials = []
	for i in range(len(tutLengths)):
		if tutLengths[i] != -1:
			lecturesWithTutorials.append(potentialSchedule[i])

	return addTutorialsHelper



def addTutorialsHelper(potentialSchedule, lectures):
	result = []
	indexCounter = []
	for i in range(len(lectures)):
		indexCounter.append(0)

	tutorialsToCheck = True
	potentialSchedules = []
	counter = 0;

	while tutorialsToCheck:
		potentialSchedules.clear()
		potentialSchedules.append(potentialSchedule)
		holder = indexCounter[0]

		for i in range(len(lectures)):
			for j in range(indexCounter[i], len(lectures[i].getTutorials())):

				if overlapChecker(potentialSchedules[counter], lectures[i].getTutorials()[j]):
					indexCounter[i] = j + 1
					temp = potentialSchedules[counter]
					temp.append(lectures[i].getTutorials()[j])
					if len(temp) == (len(potentialSchedule) + len(lectures)):
						result.append(temp)

					else:
						potentialSchedules.append(temp)
						counter += 1
						break
		if holder == indexCounter[0]:
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
		classRange=(1,5)
	elif (restrictions.getTimeofDay()=="Evening"):
	 	classRange=(6,9)

	breakTime=restrictions.getbreakTime()

	for i in range(5):
		currentClassesOnDay=schedule.getClassesOnDay(i)
		difference=0.09/len(currentClassesOnDay)
		differenceIntensity=(0.07/len(currentClassesOnDay))*2
		oldIntensity=restrictions.getIntensity().index(currentClassOnDay[0])
		for currentClass in currentClassesOnDay:
			temp=currentClass.getTimes()
			if temp[0][0] <classRange[0] or temp[1][0]>classRange[1]:
				firstRank=firstRank-difference

			if temp[0][0]> breakTime[0][0] or temp[1][0]<breakTime[1][0]:
				secondRank=secondRank-0.04
			try:
				throwAway=currentClass.getTutorials()

				if oldIntensity==restrictions.getIntensity().index(currentClass)-1 or oldIntensity==restrictions.getIntensity().index(currentClass)+1:
					thirdRank=thirdRank-differenceIntensity
				oldIntensity=restrictions.getIntensity().index(currentClass)
			except:
				pass



	schedule.setRating(firstRank+secondRank+thirdRank)
