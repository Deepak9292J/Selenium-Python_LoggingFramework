"""
By default the logs are being printed like this-
DEBUG:root:Debug message
INFO:root:Info Level message

But we want the logs to be printed in a better and neat way. So, if we need only the log level and
the message and the time in the logs, we would customise the basicConfig() statement like below
"""

import logging

#Here for the sake of demo, we are printing logs in console. But the same can be done for file logging as well
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s' ,
                    datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info Level message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")


