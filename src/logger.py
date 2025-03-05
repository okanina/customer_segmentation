import os
import logging
from datetime import datetime

FILE_NAME =f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
FILE_DIR_PATH =os.path.join(os.getcwd(), "logs")
os.makedirs(FILE_DIR_PATH, exist_ok=True)

file_path = os.path.join(FILE_DIR_PATH, FILE_NAME)

logging.basicConfig(filename=file_path, format= "[%(asctime)s] - %(name)s - %(levelname)s - %(lineno)d - %(message)s", level=logging.INFO)
