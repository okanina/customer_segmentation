import os
import logging
from datetime import datetime

filename=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
dir_path = os.path.join(os.getcwd(), "logs")
os.makedirs(dir_path, exist_ok=True)

filepath_name= os.path.join(dir_path, filename)

logging.basicConfig(
    filename= filepath_name,
    format="[%(asctime)s] - %(name)s -%(levelname)s - %(lineno)d -%(message)s",
    level=logging.INFO
)
