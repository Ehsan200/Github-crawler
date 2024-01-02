# Github-crawler

This is a Python-based project that uses the GitHub API to crawl and fetch data related to commits and pull requests from various repositories.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python and pip installed on your machine. You can download Python from [here](https://www.python.org/downloads/) and pip is included in Python 3.4 and later versions.

### Installing

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Environment Variables

Before running the project, you need to set the following environment variable:

- `GITHUB_TOKEN`: Your personal GitHub token. This is required to authenticate with the GitHub API and increase the rate limit. You can generate a personal access token from [here](https://github.com/settings/tokens).

You can set the environment variable in your terminal like this:

```bash
export GITHUB_TOKEN=your_token_here
```

Replace `your_token_here` with your actual GitHub token. This command needs to be run in the same terminal session before you start the application. If you close the terminal or start a new session, you will need to run the command again.

**Please note that you should keep your tokens secret; do not commit them or share them online.**

## Usage

The project can be used to crawl and fetch data related to commits and pull requests from various repositories. The following commands are available:


- To see help:
    ```bash
    python crawl.py --help
    ```
- To crawl commits:
    ```bash
    python crawl.py commits --r_owner <repository_owner> --r_name <repository_name>
    ```
- To crawl pull requests:
    ```bash
    python crawl.py pull-requests --r_owner <repository_owner> --r_name <repository_name>
    ```
- To crawl pull commits:
    ```bash
    python crawl.py pull-commits --r_owner <repository_owner> --r_name <repository_name>
    ```
- To crawl pull files:
    ```bash
    python crawl.py pull-files --r_owner <repository_owner> --r_name <repository_name>
    ```
- To crawl pull reviews:
    ```bash
    python crawl.py pull-reviews --r_owner <repository_owner> --r_name <repository_name>
    ```
- To crawl single commits:
    ```bash
    python crawl.py single-commits --r_owner <repository_owner> --r_name <repository_name>
    ```
- To crawl pull reviews comments:
    ```bash
    python crawl.py pull-reviews-comments --r_owner <repository_owner> --r_name <repository_name>
    ```

Replace `<repository_owner>` and `<repository_name>` with the owner and name of the repository you want to crawl.

**It's important to note that before crawling pull dependencies (`pull-deps`), you must first crawl the pull requests of the project. Similarly, before crawling single commits, ensure that you have crawled both the pull reviews and commits.**

## Data Storage and Logs

The crawled data will be stored in a directory named `crawled-data`. The crawler will create it if it doesn't exist.

Logs related to the crawling process will be stored in a directory named `logs`. This includes information such as the start and end time of the crawl, any errors encountered, and the number of items crawled. The crawler will create it if it doesn't exist.

## Built With

- [Python](https://www.python.org/)
- [requests](https://docs.python-requests.org/en/latest/)

## Authors

- [Ehsan Movaffagh](https://github.com/Ehsan200)
