import sys
from src.logger import logging

''' Here the error message detial function will give custom error message
    i the customexception class and def we have error_detail will managed by sys
    '''

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format()
    file_name,exc_tb.tb_lineno, str(error)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detial:sys):
        #inhert the exception class here by super
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detial=error_detial)
    #printing the error message and raised here
    def __str__(self):
        return self.error_message

    