from .base_list_crawler import BaseListCrawler


class CommitCrawler(BaseListCrawler):
    @property
    def _final_folder_name(self):
        return f'{self._folder_name}/commit'

    @property
    def _base_url(self):
        return f'https://api.github.com/repos/{self._repo_owner}/{self._repo_name}/commits'
