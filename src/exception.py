'''custom exception'''
import sys
from src.logger import logging

def errors(error, error_details: sys):
    '''this function is used to write custom message for exception'''

    _, _, exe_tb = error_details.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    message = "the error is from file [{0}] at line no. [{1}] and error message is [{2}]"
    error_message = message.format(
        file_name, exe_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    '''custom exception for printing the message '''

    def __init__(self, error, error_details: sys):
        super().__init__(error)
        self.error_message = errors(error, error_details)

    def __str__(self):
        return self.error_message


    