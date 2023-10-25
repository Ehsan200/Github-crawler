import abc
import os
import json
from time import sleep

import requests

from const import BASE_FOLDER_NAME
from .base_crawler import BaseCrawler


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
                    print(f'fetched {self._current_page}')

                    result = response.json()

                    if len(result) == 0:
                        print('fetch completed!')
                        break

                    with open(f'{folder_path}/{self._current_page}.json', 'w') as f:
                        json.dump(result, f)
                        self._current_page += 1

                else:
                    print(f'error in fetch. page number: {self._current_page}')
                    print('status code: {0}'.format(response.status_code))
                    if response.status_code == 404:
                        print('shutting down!')
                        return
                    print('---')
                    print(response.content)
                    print('---')
                    # sleep for 5 minutes
                    sleep(5 * 60)
            except Exception as e:
                print(e)
                # sleep for a minute if exception has been raised
                sleep(1 * 60)
