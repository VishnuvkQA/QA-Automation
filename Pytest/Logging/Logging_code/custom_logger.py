import logging
import inspect

class custlog:
    def customlogger(self,log_level=logging.DEBUG):
        log_inspect = inspect.stack()[1][3]
        logger = logging.getLogger("custlogger")
        logger.setLevel(log_level)
        format = logging.Formatter( '%(asctime)s -%(levelname)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p')
        #here in custom logger we dont need to set console streaming as we just need to print everything in a file
        file = logging.FileHandler(r"..\logs\customlogs.log",mode="a")
        file.setFormatter(format)
        if not logger.handlers:
            logger.addHandler(file)
        return logger #return the logger always at the end
    