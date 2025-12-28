import sys

def error_message_detail(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    filename = exec_tb.tb_frame.f_code.co_filename
    message = f"Error message has occured on script [{filename}] line number [{exec_tb.tb_lineno}] error message [{str(error)}]"

    return message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(self)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message