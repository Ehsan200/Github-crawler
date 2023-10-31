from .pull_dependency import PullDependency


class PullFilesCrawler(PullDependency):
    _dependency_name = 'files'


class PullReviewsCrawler(PullDependency):
    _dependency_name = 'reviews'


class PullCommitsCrawler(PullDependency):
    _dependency_name = 'commits'


class PullReviewsCommentsCrawler(PullDependency):
    _dependency_name = 'comments'
