import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    '''
    This function take error and find the error details from sys and take aas input
    and return the erro message as output
    '''
    _,_,exc_tb=error_detail.exc_info()                 # exc info find the values from error details 
                                                       # and save in 3 variable but the last one is imp 
                                                       #  because it hold the error details 
    file_name=exc_tb.tb_frame.f_code.co_filename       # saving the error details in filename variable
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))            # Printing the error details

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)