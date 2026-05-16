import sys
import logging

# Ensure the project's logging configuration (basicConfig) is applied.
# Importing `networksecurity.logging.logger` runs `logging.basicConfig(...)`
# which sets up the file handler defined in that module.
# import networksecurity.logging.logger  # minimal: run logging setup

# Use a local logger instance (will use configured handlers)
logger = logging.getLogger(__name__)

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
    
if  __name__ == '__main__':
    try:
        logger.info("Enter the try block")
        a = 1/0
        print("this will not be printed", a)
    except Exception as e:
        # Log the exception with traceback to the configured handlers/file
        logger.exception("Unhandled exception in __main__")
        raise NetworkSecurityException(e, sys)