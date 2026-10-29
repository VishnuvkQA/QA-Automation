# import logging
# class LoggerDemo:
#     def demo_logging(self):
#         #create a logger
#         logger = logging.getLogger("Logs")
#         #level the logger
#         logger.setLevel(logging.DEBUG)
#         #stream it in console terminal
#         Console = logging.StreamHandler()
#         #Format the logger
#         Format = logging.Formatter('%(asctime)s -%(levelname)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p' )
#         #Link the format to the console file
#         Console.setFormatter(Format)
#         #Connect the console to main logger
#         logger.addHandler(Console)


import logging
class Loggerdemo:
    def sample_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter ( '%(asctime)s -%(levelname)s : %(message)s ',datefmt='%y/%m/%d' )
        File_formatter = logging.Formatter ( '%(asctime)s -%(levelname)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p')
        console = logging.StreamHandler()
        File = logging.FileHandler(r"..\logs\Demo_log_file.log")
        console.setFormatter(console_formatter)
        File.setFormatter(File_formatter)
        logger.addHandler(console)
        logger.addHandler(File)

        logger.debug("This is Debug log statement")
        logger.info("This is Info log statement")
        logger.warning("This is warning log statement")
        logger.error("This is error log statement")
        logger.critical("This is critical log statement")

demo = Loggerdemo()
demo.sample_logger()



