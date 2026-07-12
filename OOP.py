# # # Defining a class:
# class Oop:
#     def __init__(self,name,status):
#         self.name = name
#         self.status = status

#     def show(self):
#         print(f"Name = {self.name} and Status = {self.status}")

# test1 = Oop("vk",'pass')
# test2 = Oop('sarath','pass')
# test1.display()
# test2.display()

# class Testcase:
#     def __init__(self, name,status):
#         self.name = name
#         self.status = status

#         def is_passed(self):
#             return self.status == 'pass'
        
# test1 = Testcase('vk','pass')
# test2 = Testcase('vkvk','fail')
# print(test1.is_passed())
# print(test2.is_passed())

# # Practice task
# class BugReport:
#     def __init__(self,title,severity,status):
#         self.title=title
#         self.severity = severity
#         self.status = status

#     def display(self):
#         print(f"Title is {self.title} severity is {self.severity} and status is {self.status}")

#         def is_critical(self):
#             return self.status == 'Critical'
        
# bug1 = BugReport("Login crash", "Critical", "Open")
# bug2 = BugReport("Button color wrong", "Low", "Closed")

# bug1.display()
# bug2.display()

        

# class TestResult:
#     def __init__(self, test_name, passed):
#         self.test_name = test_name
#         self.passed = passed

#     def display(self):
#         # write a print f-string showing
#         # test_name and passed
#         print(f'The test name is {self.test_name} and the status is {self.passed}')

#     def status_label(self):
#         # return "PASS" if self.passed is True
#         # return "FAIL" if self.passed is False
#         if self.passed == True:
#             return 'Pass'
#         else:
#             return 'Fail'
        
# case1 = TestResult('Gta',True)
# case2 = TestResult('6',False)
# case1.display()
# case2.display()

#trying to learn

class Student:
     def __init__(self, name,mark,age,sec):
          self.name = name
          self.mark = mark
          self.age = age
          self.sec = sec
     def __str__(self):
          return f'Student name is {self.name} and his mark is {self.mark}'
     def details(self):
          print(f'Student name is {self.name} and his mark is {self.mark}')
     def result(self):
          if self.mark >= 65:
               print(f'{self.name} is excellent')
          elif self.mark >=35:
               print(f'{self.name} is passed')
          else:
               print(f'{self.name} is failed...bcoz his mark is {self.mark}')
     def activity(self):
          print(f'Student is currently active on all sports')

student1 = Student('vishnu',80,21,'12th')
student2 = Student('Rahul',25,24,'12th')
student1.details()
student1.result()

student2.details()
student2.result()

          
