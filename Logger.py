import time
import logging


def show_log(message_type, message, error_code = 0):
    today = "[" + time.time().strftime("%d/%m/%Y") + "]"
    message_type = "[" + message_type + "]"
    if (error_code == 0):
        print(today + message_type + message)
    else:
        print(today + message_type + str(error_code) + ":" + message)




