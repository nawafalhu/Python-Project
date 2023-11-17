<<<<<<< HEAD
import Program12 as p

def num_is_core(self, list) :
    count=0
    for course in list :
        if "IS" in course:
            count+=1
    return count

def course_search(self,list,core,rate) :
    for course in list :
        if course.core == core and course.StudentNo / course.Capacity * 100 >= rate :
            return course
=======
import Program12 as p

def num_is_core(self, list) :
    count=0
    for course in list :
        if "IS" in course:
            count+=1
    return count

def course_search(self,list,core,rate) :
    for course in list :
        if course.core == core and course.StudentNo / course.Capacity * 100 >= rate :
            return course
>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
