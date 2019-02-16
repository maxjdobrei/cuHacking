

validSchedules = []

def createSchedules(lecturesFound):
	tempSchedule = [0,0,0,0,0,0]

	for lec in lecturesFound[0]:
		tempSchedule.pop(0)
		tempSchedule.insert(0, lec)
		try:
			for lect in lecturesFound[1]:
				tempSchedule.pop(0)
				tempSchedule.insert(0, lect)
				try:
					for lectu in lecturesFound[2]:
						tempSchedule.pop(0)
						tempSchedule.insert(0, lectu)
						try:
							for lectur in lecturesFound[3]:
								tempSchedule.pop(0)
								tempSchedule.insert(0, lectur)
								try:
									for lecture in lecturesFound[4]:
										tempSchedule.pop(0)
										tempSchedule.insert(0, lecture)
										try:
											for lectureFinal in lecturesFound[5]:
												tempSchedule.pop(0)
												tempSchedule.insert(0, lectureFinal)
												if scheduleValidator(tempSchedule):
													temp = Schedule(tempSchedule)
													validSchedules.append(temp)
												


										except:
											if scheduleValidator(tempSchedule):
													temp = Schedule(tempSchedule)
													validSchedules.append(temp)
											continue
								except:
									if scheduleValidator(tempSchedule):
										
										
										
										temp = Schedule(tempSchedule)
										validSchedules.append(temp)
									continue
						except:
							if scheduleValidator(tempSchedule):
								temp = Schedule(tempSchedule)
								validSchedules.append(temp)
							continue
				except:
					if scheduleValidator(tempSchedule):
						temp = Schedule(tempSchedule)
						validSchedules.append(temp)
					continue
		except:
			if scheduleValidator(tempSchedule):
				temp = Schedule(tempSchedule)
				validSchedules.append(temp)
			continue
	
def scheduleValidator(potentialSchedule):
	times = []
	for lecture in potentialSchedule:
		if len(times) == 0:
			times.append(lecture.getTimes())
		else:
			temp = lecture.getTimes()
			for time in times:
				if temp[0][0] == time[1][0]:
					if temp[0][1] <= time[1][1]:
						return False
				elif temp[1][0] == time[0][0]:
					if temp[1][1] <= time[0][1]:
						return False
				elif temp[0][0] > time[0][0] and temp[0][0] < time[1][0]:
					return False
			for tutorial in lecture.getTutorials():
				

	return True	


def addTutorials(potentialSchedule):
	
	result = []

	tutLengths = []
	# times = []


	for lecture in potentialSchedule:
		# times.append(lecture.getTimes())
		if len(lecture.getTutorials) == 0:
			tutLengths.append(-1)
		else:
			tutLengths.append(len(lecture.getTutorials))

	counter = 0

	# for lecture in potentialSchedule:
		
	# 	if (tutLengths[counter] != -1):
	# 		tutList = lecture.getTutorials()
			
	# 		for i in range(tutLengths[counter]):
	# 			temp = i.getTime()
	# 			for time in times:
	# 				if temp[0][0] == time[1][0]:
	# 					if temp[0][1] <= time[1][1]:
	# 						tutList.pop(i)
	# 						pass
	# 				elif temp[1][0] == time[0][0]:
	# 					if temp[1][1] <= time[0][1]:
	# 						tutList.pop(i)
	# 						pass
	# 				elif temp[0][0] > time[0][0] and temp[0][0] < time[1][0]:
	# 					tutList.pop(i)
	# 					pass
		

	for lecture in potentialSchedule:
		if tutLengths[counter] != -1:
			tutList = lecture.getTutorials()
			for i in range(tutLengths[counter]):
				temp = potentialSchedule
				temp.append(tutList[i])
				if scheduleValidator(temp):

					

		









				


