'''logging file'''

import os
from datetime import datetime
import logging

log_file_name = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"

# make dir
logs_path = "C:\\development\\NewsBite\\logs"

LOG_FILE_PATH = os.path.join(logs_path, log_file_name)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
