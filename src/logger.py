import logging
import os
from datetime import datetime


file_name=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",file_name)
os.makedirs(logs_path,exist_ok=True)

logs_file_path=os.path.join(logs_path,file_name)

logging.basicConfig(filename=logs_file_path,
                    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
                    level=logging.INFO)

#if __name__=="__main__":
#    logging.info("logging started")