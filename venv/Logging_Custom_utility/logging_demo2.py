import logging
import Logging_Custom_utility.custom_logger_method as cl
class loggingDemo():

    #This is where we are defining the class level logger
    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug("Debug message")
        self.log.info("Info Level message")
        self.log.warning("Warning message")
        self.log.error("Error message")
        self.log.critical("Critical message")

    def method2(self):
        #Defining method level logger
        method2_log = cl.customLogger(logging.DEBUG)
        method2_log.debug("Debug message")
        method2_log.info("Info Level message")
        method2_log.warning("Warning message")
        method2_log.error("Error message")
        method2_log.critical("Critical message")

    def method3(self):
        # Defining method level logger
        method3_log = cl.customLogger(logging.DEBUG)
        method3_log.debug("Debug message")
        method3_log.info("Info Level message")
        method3_log.warning("Warning message")
        method3_log.error("Error message")
        method3_log.critical("Critical message")

obj = loggingDemo()
obj.method1()
obj.method2()
obj.method3()