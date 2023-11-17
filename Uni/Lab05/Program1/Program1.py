class course :
    def __init__(self, Code, Capacity, Core, StudentNo) :
        self.Code = Code
        self.Capacity = Capacity
        self.Core = Core
        self.StudentNo = StudentNo

    def __str__(self) :
        return f"code : {self.Code}, capacity: {self.Capacity}, core:{self.Core}, student number: {self.StudentNo}"
    
    def __hash__(self) :
        return hash(self.Code)  
    
    def __gt__ (self, o) :
        return self.Capacity > o.Capacity
    
    def buildIndex(text) : 
        mydic = {}
        words = text.split(" ")
        for word in words :
            if word in mydic :
                mydic[word] += 1
            else :
                mydic[word] = 1
        return mydic