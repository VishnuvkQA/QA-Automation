import logging
logging.basicConfig(level=logging.DEBUG,filemode="w", filename=r"..\logs\loggingdemo.log",format='%(asctime)s -%(levelname)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p' )

class Maths:
    def addition(self,a,b):
         result = a + b
         return  result

    def subtraction(self,a,b):
        result = a - b
        return result

calculation = Maths()
add = calculation.addition(10,12)
logging.debug(f"This is debug mode and the result is {add}")
logging.info(f"This is info mode and the result is {add}")
logging.warning(f"This is warning mode and the result is {add}")
logging.error(f"This is error mode and the result is {add}")
logging.critical(f"This is critical mode and the result is {add}")
sub = calculation.subtraction(11,1)
logging.debug(f"This is debug mode and the result is {sub}")
logging.info(f"This is info mode and the result is {sub}")
logging.warning(f"This is warning mode and the result is {sub}")
logging.error(f"This is error mode and the result is {sub}")
logging.critical(f"This is critical mode and the result is {sub}")