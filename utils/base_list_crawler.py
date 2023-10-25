import abc
import os
import json
from time import sleep

import requests

from const import BASE_FOLDER_NAME
from .base_crawler import BaseCrawler
from .logger import info_logger


class BaseListCrawler(BaseCrawler, abc.ABC):

    def crawl(self):
        folder_path = f'{BASE_FOLDER_NAME}/{self._final_folder_name}'
        is_exists = os.path.exists(folder_path)
        if not is_exists:
            os.makedirs(folder_path)

        while True:
            try:
                response = requests.get(
                    url=self._base_url,
                    headers={
                        'Accept': 'application/vnd.github+json',
                        'Authorization': f'Bearer {self._token}',
                    },
                    params={
                        'page': self._current_page,
                        'per_page': 100,
                        **self._extra_params
                    },
                )
                if response.ok:
                    info_logger.info(f'fetched {self._current_page}')

                    result = response.json()

                    if len(result) == 0:
                        info_logger.log('fetch completed!')
                        break

                    with open(f'{folder_path}/{self._current_page}.json', 'w') as f:
                        json.dump(result, f)
                        self._current_page += 1

                else:
                    info_logger.info(f'error in fetch. page number: {self._current_page}')
                    info_logger.info('status code: {0}'.format(response.status_code))
                    if response.status_code == 404:
                        info_logger.info('shutting down!')
                        return
                    info_logger.info('---')
                    info_logger.info(response.content)
                    info_logger.info('---')
                    # sleep for 5 minutes
                    sleep(5 * 60)
            except Exception as e:
                info_logger.info(e)
                # sleep for a minute if exception has been raised
                sleep(1 * 60)
