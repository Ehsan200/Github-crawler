import abc


class BaseCrawler:
    def __init__(self, repo_name: str, repo_owner: str, token: str, current_page=1):
        assert repo_name is not None
        assert repo_owner is not None
        if token is None:
            raise Exception('please provide token')

        self._repo_name = repo_name
        self._repo_owner = repo_owner
        self._current_page = current_page
        self._token = token

    @property
    def _folder_name(self):
        return f'{self._repo_owner}-{self._repo_name}'

    @property
    @abc.abstractmethod
    def _final_folder_name(self):
        pass

    @property
    @abc.abstractmethod
    def _base_url(self):
        pass

    @property
    def _extra_params(self):
        return {}

    @abc.abstractmethod
    def crawl(self):
        pass
