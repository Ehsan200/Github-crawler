import argparse

from const import GH_TOKEN
from utils import PullCrawler, CommitCrawler


def validate_args(args):
    if args.current_page < 1:
        raise Exception('current_page can not be less than 1')
    if args.r_owner is None or args.r_name is None:
        raise Exception('please provide both owner and name of your repo')


def crawl_pull_requests(args):
    try:
        validate_args(args)
        print(f'project={args.r_owner[0]}/{args.r_name[0]}')
        print('start crawling prs!')
        PullCrawler(
            current_page=args.current_page,
            token=GH_TOKEN,
            repo_owner=args.r_owner[0],
            repo_name=args.r_name[0],
        ).crawl()
    except Exception as e:
        # todo: add color
        print(e)


# \033[91m

def crawl_commits(args):
    try:
        validate_args(args)
        print(f'project={args.r_owner[0]}/{args.r_name[0]}')
        print('start crawling commits!')
        CommitCrawler(
            current_page=args.current_page,
            token=GH_TOKEN,
            repo_owner=args.r_owner[0],
            repo_name=args.r_name[0],
        ).crawl()
    except Exception as e:
        print(e)


global_parser = argparse.ArgumentParser(
    description=
    """
    with this app you can Crawl from Github :))
    before run scripts set GH_TOKEN in your environment
    """
)
# subparsers = global_parser.add_subparsers(
#     title="subcommands", help="choose which data you want to crawl",
# )

global_parser.add_argument(
    '--r_owner',
    type=str,
    help="your owner name",
    nargs=1,
)
global_parser.add_argument(
    '--r_name',
    type=str,
    help="your repo name",
    nargs=1,
)
global_parser.add_argument(
    '--current_page',
    type=int,
    help="current page for list type crawlers",
    nargs=1,
    default=1,
    metavar='1',
)

# todo: invoke functions in a better way
# todo: complete
FUNCTION_MAP = {
    'pull-requests': crawl_pull_requests,
    'commits': crawl_commits,
}

global_parser.add_argument('command', choices=FUNCTION_MAP.keys())

global_args = global_parser.parse_args()
func = FUNCTION_MAP[global_args.command]
func(global_args)
