from selenium import webdriver
import time
import logging

#To simply print the logs in the file, we are doing it like below-

logging.basicConfig(filename="test.log",level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info Level message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

