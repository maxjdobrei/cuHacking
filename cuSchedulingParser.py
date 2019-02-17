from bs4 import BeautifulSoup
import urllib.request
import mechanicalsoup
from cuScheduling import *
from Lecture import *
from Tutorial import *
from Restrictions import *



# class Lecture:

#     startTime=tuple()
#     endTime=tuple()
#     location=""
#     days=[]
#     tutorials=[]
#     courseCode=""

#     def __init__(self,courseCode,Time,location,day,tutorialsdays):
#         Start= Time[0].split(":")
#         End= Time[1].split(":")
#         self.courseCode=courseCode
#         self.startTime= (int(Start[0]), int(Start[1]))
#         self.endTime= (int(End[0]), int(End[1]))
#         self.location=location
#         self.days= self.convertLectureDay(day)
#         self.tutorials = tutorialsdays

#     def toList(self):
#         return [self.courseCode,self.startTime,self.endTime,self.location,self.days,self.tutorials]
#     def convertLectureDay(self,day):
#         dayNum=[]
#         tempdays = day
#         for days in tempdays:
#             if days=="Mon":
#                dayNum.append(0)
#             elif days == "Tue":
#                 dayNum.append(1)
#             elif days == "Wed":
#                 dayNum.append(2)
#             elif days == "Thu":
#                 dayNum.append(3)
#             elif days == "Fri":
#                 dayNum.append(4)
#         return dayNum

#     def getLectureTimes(self):
# 	    return (self.startTime, self.endTime)

# ############################################################################
# class Tutorial:
#     startTime=tuple()
#     endTime=tuple()
#     location=""
#     days=[]
#     courseCode=""
#     def __init__(self,courseCode,Time,location,day):
#         Start= Time[0].split(":")
#         End= Time[1].split(":")

#         self.courseCode=courseCode
#         self.startTime= (int(Start[0]), int(Start[1]))
#         self.endTime= (int(End[0]), int(End[1]))
#         self.location=location
#         self.days=self.convertDay(day)
#     def __str__(self):
#         return "Days of tuts " + self.days
#     def convertDay(self,day):
#         dayNum=[]
#         tempdays = day
#         for days in tempdays:
#             if days=="Mon":
#                 dayNum.append(0)
#             elif days == "Tue":
#                 dayNum.append(1)
#             elif days == "Wed":
#                 dayNum.append(2)
#             elif days == "Thu":
#                 dayNum.append(3)
#             elif days == "Fri":
#                 dayNum.append(4)
#         return dayNum
    
#     def getTimes(self):
# 	    return (self.startTime, self.endTime)

#################################################################################################################

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
                times.pop(1)
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
            tutorials = []
            parentWanted = entry[5]
            for tutEntry in superList.bigList:
                if tutEntry[4] == True and parentWanted == tutEntry[5]:
                    newTutorial = Tutorial(courseCode,entry[1],entry[2],entry[0])
                    tutorials.append(newTutorial)
                newCourseCode = courseCode.get('sel_subj')
                newCourseCode += courseNumber
            newLecture = Lecture(courseCode, entry[1],entry[2],entry[0],tutorials)
            crazyList.append(newLecture)   
    return crazyList

            
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
            return [-1]
    return (crazyHugeList)


results = createSchedules(main("Fall",["COMP1406","ENST1020","GEOM2007","COMP1805","MATH1104"]))
print(results)