#writing a file (file handling)
# with open('result.txt','w') as f:
#     f.write("test case 1 : passed\n")
#     f.write("test case 2 : failed\n")
#     f.write('test case 1 and 2 are read successfully')

#reading a file
# with open("result.txt",'r') as file:
#     content = file.read()
#     print(content)

#appending a file
# with open('result.txt','a') as file:
#     file.write("\nNow we have added a new line without using write mode")

#reading file line by line
# with open('result.txt','r') as file:
#     for line in file:
#         print(line)

#Exception handling
# try:
#     a = 10/0
# except:
#     print("An error came")

# Specific except
# try:
#     a = 10/0
# except ZeroDivisionError:
#     print("Something went wrong")

#most common error in automation - missing files
# try:
#     file = open('ressult.txt','r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print('Filenotfound error occured - Check file name or location')

# def divide(value1,value2):
#     try:
#         result = (value1/value2) *100
#         return result
#     except ZeroDivisionError:
#         print("An error occured, check the values")
#         return None
    
# result1 = divide(10,2)
# print(result1)
# result2 = divide(5,0)
# print(result2)

#Practice task
# with open('practice.txt','w') as file:
#     file.write('Practice started\n')
# # with open('practice.txt','a') as file:
# #     file.write('Test write 1 on append\n')
# #     file.write("Test write 2 on append")

# with open("test_log.txt", "w") as file:
#     file.write("Test Run Started\n")

# with open('test_log.txt','a') as file:
#     file.write("Test case 1 started\n")
#     file.write("Test case 2 started\n")

# with open('test_log.txt','r') as file:
#     content = file.read()
#     print(content)

# def safe_divide(passed,total):
#     try:
#         result = (passed/total)*100
#         return result
#     except ZeroDivisionError:
#         print("An error occured")
#         return None
# value1 = safe_divide(15,20)
# print(value1)
# value2 = safe_divide(15,0)
# print(value2)