class Students:
  def __init__(self):
   self.students= [
     {"firstname":"ravi","lastname":"doe","fullname":"doeravi","address":"hyderbad","course":"cse","colleganame":"rsn","fee":20000,"age":25,"rollnumber":1234},
     {"firstname":"raju","lastname":"joe","fullname":"joeraju","address":"chennai","course":"ece","colleganame":"svn","fee":20000,"age":26,"rollnumber":4321},
     {"firstname":"hema","lastname":"m","fullname":"mhema","address":"bangalore","course":"eee","colleganame":"cng","fee":20000,"age":24,"rollnumber":6543 }
     ]
   
  def getAllStudents(self):
     return self.students
   
  def getStudentByName(self,firstname):
    for student in self.students:
      if (student["firstname"]== firstname):
         return student
    return "student not found"  

  def getStudentByrollnum(self,rollnumber):
    for student in self.students:
      if(student["rollnumber"]==rollnumber):
       return student
    return "student not found"  



s1=Students()
print(s1.getAllStudents())
print(s1.getStudentByName("hema"))
print(s1.getStudentByrollnum(1234))
