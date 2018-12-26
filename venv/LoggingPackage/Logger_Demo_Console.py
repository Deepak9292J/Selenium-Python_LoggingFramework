#This script is showing how to use to logger object for logging on the console

import logging

class LoggerDemoConsole():
    def testLog(self):
        # Create Logger object and set the log level to Info
        #The name used within the paranthesis of getlogger is the name of the class file from where the logs are being pulled out
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set the log level to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter, the same way like how we did it earlier
        console_formatter = logging.Formatter('%(asctime)s: %(name)s %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

        # Add formatter to console handler
        console_handler.setFormatter(console_formatter)

        # Add console handler to logger
        logger.addHandler(console_handler)


        #Log messages
        logger.debug('Debug message')
        logger.info('Info Level message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')


obj = LoggerDemoConsole()
obj.testLog()