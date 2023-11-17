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
