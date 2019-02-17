from bs4 import BeautifulSoup
import urllib.request
import mechanicalsoup
from cuScheduling import *
from Lecture import *
from Tutorial import *
from Restrictions import *

class MegaList:

    def __init__(self):
        self.bigList = []

    def addIt(self,list):
        self.bigList.append(list)

    def printIt(self):
        print(self.bigList)


#################################################################################################################
#passes through the first gateway, and moves on to next page.
#url is starting website, and desired is course term.
def termSelector(url,desiredTerm,courseCode,courseNumber):
    deg = {"sel_levl": "UG"}
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    browser.get_url()
    #first gate form
    browser.select_form('form[action="bwysched.p_search_fields"]')
    browser.get_current_form().set_select(desiredTerm)
    #passes first gate
    browser.submit_selected()
    #second gate form
    browser.select_form('form[action="bwysched.p_course_search"]')
    #selects degree level
    browser.get_current_form().set_select(deg)
    #selects courseCode in letters
    browser.get_current_form().set_select(courseCode)
    #fills in course code number
    browser["sel_number"] = courseNumber
    #past second gate
    browser.submit_selected()
    #now browser is on the page we were looking for, so it is time to scrape!
    #page is now a soup object
    page = browser.get_current_page()
    return courseGetter(page,courseCode,courseNumber)



def courseGetter(page,courseCode,courseNumber):
    holderCount = -1
    #finds all tables in soup object
    tables = page.findAll("table")
    #strings and splits on table, making the list of tables
    tables = str(tables)
    tables = tables.split('<table>')
    #linker = []
    superCount = 0
    for colspans in tables:
        isLecture = False
        isTutorial = False
        colspans = str(colspans)
        colspans =  colspans.split('colspan=')
        for info in colspans:
            if "Lecture" in info:
                isLecture = True
                isTutorial = False
            elif "Tutorial" in info or "Laboratory" in info:
                isTutorial = True
                isLecture = False
            if "Days:" in info:
                info = info.split("<tr bgcolor=")
                info = info.pop(0)
                info = info.split("<b>")
                info.pop(0)
                info.pop(0)
#Now the list is length 4, and contains Days[0], Time[1], Building [2], Room[3]
                #Instantiate the 4 categories
                days = info[0]
                times = info[1]
                building = info[2]
                room = info[3]
                #Calculate Days
                days = days.split()
                days.pop(0)
                #Calculate Time
                times = times.split()
                times.pop(0)
                times.pop(0)
                #Calculate building
                building = building.split("</b>")
                building.pop(0)
                building = building[0]
                #Calculate room
                room = room.split("</b>")
                room = room[1]
                room = room.split("</td>")
                room = room[0]
                location = building + room
                if isLecture == True:
                    holderCount+=1
                    parent = holderCount
                elif isTutorial == True:
                    parent = holderCount
                listOfAll = [days,times,location,isLecture,isTutorial]
                if superCount == 0:
                    listOfAll.append(parent)
                    superList = MegaList()
                    superList.addIt(listOfAll)
                    superCount+=1
                else:
                    listOfAll.append(parent)
                    superList.addIt(listOfAll)
    try:
        half = len(superList.bigList)//2
    except:
        return []
    superList.bigList = superList.bigList[:half]
    return objectCreator(superList,courseCode,courseNumber)


#   0   1       2       3             4     5           INDEX
#[days,times,location,isLecture,isTutorial,parent]
def objectCreator(superList,courseCode,courseNumber):
    #crazyList will store all of my Lecture Objects
	crazyList = []
    #print(len(superList.bigList))
    #print(superList.bigList)
	for entry in superList.bigList:
		#if it is a lecture.
		if entry[3] == True:
			newCourseCode = ''
			newTutCourseCode = ''
			tutorials = []
			parentWanted = entry[5]
			for tutEntry in superList.bigList:
				if tutEntry[4] == True and parentWanted == tutEntry[5]:
					newTutCourseCode = courseCode.get('sel_subj')
					newTutCourseCode += courseNumber
					newTutorial = Tutorial(newTutCourseCode,tutEntry[1],tutEntry[2],tutEntry[0])
					tutorials.append(newTutorial)
				newCourseCode = courseCode.get('sel_subj')
				newCourseCode += courseNumber
			newLecture = Lecture(newCourseCode, entry[1],entry[2],entry[0],tutorials)
			crazyList.append(newLecture)
	return crazyList


def getSchedule(allResults, rating):
	for result in allResults:
		if result.getRating() == rating:
			return result

def main(term,classes):
    #constants throughout the functions
    url = "https://central.carleton.ca/prod/bwysched.p_select_term?wsea_code=EXT"
    numberOfClasses = len(classes)
    if term == "Fall":
        term = {"term_code": "201830"}
    elif term == "Winter":
        term = {"term_code": "201910"}
    elif term == "Summer":
        term = {"term_code": "201920"}
    crazyHugeList = []
    #Gets name of class, and number of class, and runs functions
    for lecture in classes:
        name = ''
        for i in range (0,4):
            name+= lecture[i]
        subject = {"sel_subj":name}
        number = ''
        for i in range (4,8):
            number += lecture[i]
        temp = termSelector(url,term,subject,number)
        crazyHugeList.append(temp)
    for item in crazyHugeList:
        if len(item) == 0:
            return []
    return (crazyHugeList)

rankedResults = []
restrictions = Restrictions("Morning", "3:30", ["COMP1805","MATH1102","COMP1406","ENST1020","PSYC1001"])
results = createSchedules(main("Fall",["COMP1805","ENST1020","COMP1406","MATH1002","PSYC1001"]))
print(len(results))
for result in results:
	scheduleRanker(result,restrictions)
	rankedResults.append(result.getRating())

print(len(rankedResults))
rankedResults.sort()
print(len(rankedResults))
bestFive = []
if len(rankedResults) >= 5:
	print("yuh")
	for i in range(len(rankedResults) - 5, len(rankedResults)):
		bestFive.append(getSchedule(results, rankedResults[i]))
else:
	for i in range(len(rankedResults)):
		bestFive.append(getSchedule(results, rankedResults[i]))	

print(bestFive)
