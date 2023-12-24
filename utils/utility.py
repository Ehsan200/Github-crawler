import os
import json


def _get_all_json_files_in_folder(folder_path):
    return [pos_json for pos_json in os.listdir(folder_path) if pos_json.endswith('.json')]


def get_all_pull_numbers(pull_folder_path):
    json_files = _get_all_json_files_in_folder(pull_folder_path)

    pull_numbers = []
    for json_file in json_files:
        with open(f'{pull_folder_path}/{json_file}', 'r') as f:
            data = json.load(f)
            pull_numbers += [
                _['number'] for _ in data
            ]

    return list(sorted(list(set(pull_numbers))))


def get_all_reviews_commit_ids(pull_folder_path):
    pull_numbers = get_all_pull_numbers(pull_folder_path)
    commit_ids = []

    for pr_number in pull_numbers:
        json_files = _get_all_json_files_in_folder(pull_folder_path)

        for json_file in json_files:
            with open(f'{pull_folder_path}/{pr_number}/reviews/{json_file}', 'r') as f:
                data = json.load(f)

                commit_ids += [
                    _['commit_id'] for _ in data
                ]

    return commit_ids


def get_all_commit_ids(commit_folder_path):
    json_files = _get_all_json_files_in_folder(commit_folder_path)

    commit_ids = []
    for json_file in json_files:
        with open(f'{commit_folder_path}/{json_file}', 'r') as f:
            data = json.load(f)

            commit_ids += [
                _['sha'] for _ in data
            ]

    return commit_ids
