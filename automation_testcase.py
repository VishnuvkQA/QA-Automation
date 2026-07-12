
# class Testcases:
#     def __init__(self,name,expected,actual):
#         self.name = name
#         self.expected = expected
#         self.actual = actual
    
#     def is_passed(self):
#         return self.expected == self.actual

#     def result(self):
#         if self.is_passed():
#             return "Pass"
#         else:
#             return "Fail"       
# tests = [Testcases('login1',500,500),Testcases('login2',200,500),Testcases('login3',500,500)]
# for test in tests:
#     print(f"{test.name}: {test.result()}")

#     def run_looptest(tests):
#         passed = 0
#         failed = 0

#         for test in tests:
#             # print(f'{test.name}: {test.result()}')
#             log_result(test)
#             if test.is_passed():
#                 passed = passed+1
#             else:
#                 failed = failed+1
#         print(f"Total passed = {passed}")
#         print(f"Total failed = {failed}")
#     def log_result(test):
#         with open('log_result.txt','a') as file:
#             file.write(f'{test.name}:{test.result()}\n')

class Testcase:
    def __init__(self,name,actual,expected):
        self.name = name
        self.expected= expected
        self.actual=actual
    def is_pass(self):
        return self.expected == self.actual
    def result(self):
        if self.is_pass():
            return 'Pass'
        else:
            return 'True'
    def log_results(test):
        with open ('log_results.txt','a') as file:
            file.write(f'{test.name}: {test.result()}\n')
    def run_test(test_list):
        passed = 0
        failed = 0
        for test in test_list:
            try:
                print(f'{test.name}: {test.result()}')
                Testcase.log_results(test)
                if test.is_pass():
                    passed = passed+1
                else:
                    failed = failed+1
            except Exception as e:
                print(f'{test.name} has an error')
        return passed,failed
with open('log_results.txt','w') as file:
    file.write('Test run started \n')
test = [Testcase('login1',500,500),Testcase('login2',800,450),Testcase('login3',400,400)]
passed,failed = Testcase.run_test(test)
print(f'Total {passed + failed}')
print(f'Passed = {passed}')
print(f'Failed = {failed}')
    
        