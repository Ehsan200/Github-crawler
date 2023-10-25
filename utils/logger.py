import logging
import os

FOLDER_PATH = 'logs'

if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)

logging.basicConfig(
    filename=f'{FOLDER_PATH}/crawler-{len(os.listdir(FOLDER_PATH))}.info.log',
    filemode='w',
    format='%(process)d - %(levelname)s - %(name)s - %(message)s',
    level=logging.INFO,
)

info_logger = logging.getLogger(__name__)
