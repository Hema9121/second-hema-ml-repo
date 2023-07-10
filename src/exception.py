import sys
import logging

def my_err_msg(error,error_detail:sys):
    
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error="the error is occured in the file {0} at line {1} as error:{2}".format(file_name,exc_tb.tb_lineno,str(error))
    return error
class myexcclass(Exception):
    def __init__(self,error,error_detail:str):
        super().__init__(error)
        self.error=my_err_msg(error,error_detail)
    def __str__(self) -> str:
        return self.error
    

if __name__=="__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("division by 0")
        raise myexcclass(e,sys)
