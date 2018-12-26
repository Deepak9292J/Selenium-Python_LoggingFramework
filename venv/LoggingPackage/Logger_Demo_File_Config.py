import logging
import logging.config

class LoggerDemoConfig():
    def testLog(self):

        # Create Logger
        logging.config.fileConfig("logging.conf")
        logger = logging.getLogger(LoggerDemoConfig.__name__)

        #Logging messages
        logger.debug('Debug message')
        logger.info('Info Level message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')

obj = LoggerDemoConfig()
obj.testLog()




