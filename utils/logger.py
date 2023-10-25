import logging
import os

FOLDER_PATH = 'logs'

is_exists = os.path.exists(FOLDER_PATH)
if not is_exists:
    os.makedirs(FOLDER_PATH)

logging.basicConfig(
    filename=f'{FOLDER_PATH}/crawler-{len(os.listdir(FOLDER_PATH))}.info.log',
    filemode='w',
    format='%(process)d - %(levelname)s - %(name)s - %(message)s',
    level=logging.INFO,
)

info_logger = logging.getLogger(__name__)
