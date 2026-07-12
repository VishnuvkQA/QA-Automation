# def check(expected,actual):
#     return (expected ==actual)

# result = check(200,200)
# print(result)

# tests = ['login','logout']

# def run(name):
#     print(f'Running {name}')
#     print('Finished running')

# for test in tests:
#     run(test)


# writing a test case script from scratch

# with open('testresult.txt','w') as file:
#     file.write('New Testcase Started\n')


# class Testscript:
#     def __init__(self,name,expected,actual):
#         self.name = name
#         self.expected = expected
#         self.actual = actual
#     def passed(self):
#         return self.expected==self.actual
#     def result(self):
#         if self.passed():
#             return 'Pass'
#         else:
#             return "Fail"      
# test_list = [Testscript('Login1',200,200),
#              Testscript ('login2',200,200),
#              Testscript('Login3',500,200)]
# def testlog(test):
#     with open('testresult.txt','a') as file:
#         file.write(f'{test.name} is {test.result()}\n')

# def test_run(test_list):
#     passed = 0
#     failed = 0

#     for test in test_list:
#         try:
#             print(f'{test.name} is {test.result()}')
#             testlog(test)

#             if test.passed():
#                 passed = passed+1
#             else:
#                 failed = failed+1
#         except Exception as e:
#             print(f'Error in {test.name} : {e}')

#     return passed,failed
# passed,failed = test_run(test_list)
# with open ('testresult.txt','a') as file:
#     file.write(f'Total tests = {passed+failed}\n')
#     file.write(f'Passed = {passed}\n')
#     file.write(f'Failed = {failed}')


def check_response(expected,actual):
    if expected==actual:
        return "PASS"
    else:
        return "FAIL"

result = check_response(200,404)
print(result)
