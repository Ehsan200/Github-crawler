from const import BASE_FOLDER_NAME
from .pull_crawler import PullCrawler
from .utility import get_all_pull_numbers


class PullDependency(PullCrawler):
    _pull_number = 0
    _dependency_name = None

    @property
    def _extra_params(self):
        return {}

    @property
    def _pull_folder_path(self):
        return f'{self._folder_name}/pull'

    @property
    def _final_folder_name(self):
        return f'{self._pull_folder_path}/{self._pull_number}/{self._dependency_name}'

    @property
    def _base_url(self):
        assert self._dependency_name is not None
        return f'https://api.github.com/repos/{self._repo_owner}/{self._repo_name}/pulls/' \
               f'{self._pull_number}/{self._dependency_name}'

    def crawl(self):
        all_pull_numbers = get_all_pull_numbers(f'{BASE_FOLDER_NAME}/{self._pull_folder_path}')
        for pull_number in all_pull_numbers:
            # if in child class developers override self._pull_number
            if pull_number < self._pull_number:
                continue
            self._pull_number = pull_number
            assert self._pull_number != 0
            self._current_page = 1
            super().crawl()
            print(f'pull number {self._pull_number} for {self._dependency_name} completed')
