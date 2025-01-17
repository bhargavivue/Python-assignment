import sys
class Students:
    def __init__(self):
        self.students = [
            {"firstname": "ravi", "lastname": "doe", "fullname": "doeravi","dob":"10/12/1989", "address": "hyderabad", "course": "cse", "collegename": "rsn", "fee": 30000, "age": 25, "rollnumber": 1234},
            {"firstname": "raju", "lastname": "joe", "fullname": "joeraju","dob":"15/12/1989", "address": "chennai", "course": "ece", "collegename": "svn", "fee": 10000, "age": 26, "rollnumber": 4321},
            {"firstname": "hema", "lastname": "m", "fullname": "mhema", "dob":"10/12/1985","address": "bangalore", "course": "eee", "collegename": "cng", "fee": 20000, "age": 26, "rollnumber": 6543},
            {"firstname": "phil", "lastname": "baker", "fullname": "philbaker", "dob":"15/11/1999","address": "bangalore", "course": "eee", "collegename": "cng", "fee": 10000, "age": 24, "rollnumber": 6543}
        ]
     
     # Get all students method
    def getAllStudents(self):
        return self.students
    
    # Method to get students by specific fee by using list 
    def getStudentByfee(self, fee):
        students_list=[]
        for student in self.students:
            if student["fee"] == fee:
             # If it matches, add the student to the list 
              students_list.append(student)  
        return students_list if students_list else "Fee is not matching"

# Method to get students with the lowest fee
    def get_students_with_lowest_fee(self):
        if not self.students:
            return "No students available."

# Find the lowest fee among students
        lowest_fee=min(student["fee"]  for student in self.students)
# Return students with the lowest fee
        return self.getStudentByfee(lowest_fee)
    
# Method to get students with the highest fee
    def get_student_with_highest_fee(self):
        if not self.students:
           return "No students available."
    #find the highest fee among students
        highest_fee=max(student["fee"]for student in self.students)
    #return students withe the highest fee
        return self.getStudentByfee(highest_fee)
    
    # Get student by firstname
    def getStudentByname(self, firstname):
        for student in self.students:
            if student["firstname"] == firstname:
                return student
        return "Student not found"

    # Get student by roll number
    def getStudentByrollnum(self, rollnumber):
        for student in self.students:
            if student["rollnumber"] == rollnumber:
                return student
        return "Student not found"
   # Get students by course
    def getStudentByCourse(self, course):
        students_list=[]
        for student in self.students:
            if student["course"] == course:
             students_list.append(student)  
        return students_list if students_list else "course is not matching"
    # Get student by age
    def getStudentByage(self, age):
        students_list=[]
        for student in self.students:
            if student["age"] == age:
             students_list.append(student)
        return students_list if students_list else "age is not matching" 
    
    def addstudent(self,firstname,lastname,fullname,dob,rollnumber,age,course,address,collegename,fee):
       dict={"firstname": firstname, "lastname": lastname, "fullname": fullname, "dob":dob,"address": address, "course": course, "collegename": collegename, "fee": fee, "age": age, "rollnumber": rollnumber}
       self.students.append(dict)
       return "Student:" +firstname+ " added successfully."
s1 = Students()

if len(sys.argv) == 11:
# Unpack command-line arguments
 firstname =sys.argv[1]
 lastname =sys.argv[2] 
 fullname =sys.argv[3] 
 dob=sys.argv[4]
 rollnumber=sys.argv[5]
 age=sys.argv[6]
 course=sys.argv[7]
 address=sys.argv[8]
 collegename =sys.argv[9] 
 fee = sys.argv[10]
 print(s1.addstudent(firstname,lastname,fullname,dob,rollnumber,age,course,address,collegename,fee))

    