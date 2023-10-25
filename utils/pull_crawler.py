from .base_list_crawler import BaseListCrawler


class PullCrawler(BaseListCrawler):

    @property
    def _extra_params(self):
        return {'state': 'all'}

    @property
    def _final_folder_name(self):
        return f'{self._folder_name}/pull'

    @property
    def _base_url(self):
        return f'https://api.github.com/repos/{self._repo_owner}/{self._repo_name}/pulls'
