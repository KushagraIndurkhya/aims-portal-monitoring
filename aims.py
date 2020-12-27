import requests
import time

cookie={"JSESSIONID":input("Enter Cookie: ")}
TIME_QUANT=600
URL="https://aims.iiitr.ac.in/iiitraichur/courseReg/loadMyCoursesHistroy?studentId=17&courseCd=&courseName=&orderBy=1&degreeIds=&acadPeriodIds=&regTypeIds=&gradeIds=&resultIds=&isGradeIds="

def req():
    return requests.get(URL, cookies=cookie).json()

def getCG(resp):
    gradeDescriptor = {"A+": 10, "A": 10, "A-": 9, "B": 8, "B-": 7, "C": 6, "C-": 5, "D": 4, "S": 0}
    total_credits=0
    my_credits=0
    for course in resp:
        if course['gradeDesc'] != 'S' and course['gradeDesc'] != '':
            my_credits+=gradeDescriptor[(course['gradeDesc'])]*float(course['credits'])
            total_credits+=float(course["credits"])
    return (my_credits/total_credits)

def getGrade(resp,courseID):
    for course in resp:
        if course['courseCd'] == courseID:
            return course['gradeDesc']

def getUngraded(resp):
    res=[]
    for course in resp:
        if course['gradeDesc'] == '':
            res.append((course['courseCd'],course['courseName']))
        else:
            pass
    return res


def monitor(lastreq=getUngraded(req())):
    while True:   
        latestreq=getUngraded(req())
        if len(lastreq)!=len(latestreq):
            for cid,courseName in lastreq:
                if (cid,courseName) not in latestreq:
                    print("{}:{} updated Grade:{}".format(cid,courseName,getGrade(req(),cid)))
                    time.sleep(TIME_QUANT)
                    monitor(latestreq)    
        else:
            time.sleep(TIME_QUANT)
            monitor(latestreq)

print(getCG(req()))
monitor()

    




