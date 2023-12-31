import json
import os
from time import sleep
from functools import cached_property

import requests

from const import BASE_FOLDER_NAME
from .base_crawler import BaseCrawler
from .logger import info_logger
from .utility import get_all_commit_ids, get_all_reviews_commit_ids


class SingleCommitCrawler(BaseCrawler):
    _commit_sha = None

    @property
    def _final_folder_name(self):
        return f'{self._folder_name}/commit/all'

    @property
    def _base_url(self):
        return f'https://api.github.com/repos/{self._repo_owner}/{self._repo_name}/commits/{self._commit_sha}'

    @cached_property
    def all_commit_ids(self):
        base_folder_path = f'{BASE_FOLDER_NAME}/{self._folder_name}'

        return list(
            set(
                get_all_commit_ids(f'{base_folder_path}/commit') +
                get_all_reviews_commit_ids(f'{base_folder_path}/pull')
            )
        )

    @property
    def final_file_name(self):
        folder_path = f'{BASE_FOLDER_NAME}/{self._final_folder_name}'
        return f'{folder_path}/{self._commit_sha}.json'

    def crawl(self):
        folder_path = f'{BASE_FOLDER_NAME}/{self._final_folder_name}'
        is_exists = os.path.exists(folder_path)
        if not is_exists:
            os.makedirs(folder_path)

        for commit_sha in self.all_commit_ids:
            self._commit_sha = commit_sha
            if os.path.exists(self.final_file_name):
                continue

            while True:
                try:
                    response = requests.get(
                        url=self._base_url,
                        headers={
                            'Accept': 'application/vnd.github+json',
                            'Authorization': f'Bearer {self._token}',
                        },
                        params={
                            **self._extra_params
                        },
                    )
                    if response.ok:

                        result = response.json()

                        with open(self.final_file_name, 'w') as f:
                            json.dump(result, f)
                            info_logger.info(f'fetch completed for "{self._commit_sha}"!')

                        # get out of while True loop and go to next commit to fetch
                        break

                    else:
                        info_logger.info('status code: {0}'.format(response.status_code))
                        if response.status_code == 404:
                            info_logger.info('shutting down!')
                            return
                        info_logger.info(f'error in fetch. commit sha: "{self._commit_sha}" try again in 5 minutes!')

                        info_logger.info('---')
                        info_logger.info(response.content)
                        info_logger.info('---')
                        # sleep for 5 minutes
                        sleep(5 * 60)
                except Exception as e:
                    info_logger.info(e)
                    # sleep for a minute if exception has been raised
                    sleep(1 * 60)
