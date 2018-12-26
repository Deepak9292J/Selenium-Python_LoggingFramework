import logging
import inspect

def customLogger(loglevel):
    #Gets the name of the class/method from where this logger method is being called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("{}.log".format(loggerName), mode = 'w')
    filehandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s' ,
                    datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    return logger
