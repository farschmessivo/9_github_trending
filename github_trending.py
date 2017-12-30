import requests
from datetime import datetime, timedelta

top_size = 20


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    time_now = datetime.now()
    last_week = (time_now - timedelta(days=7)).strftime('%Y-%m-%d')
    prepare_date = 'created:>={}'.format(last_week)
    params = {
        'q': prepare_date,
        'sort': 'stars',
        'order': 'desc',
        'page': '1',
        'per_page': top_size
    }
    result = requests.get(url, params=params)
    return result.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    issues = requests.get(url)
    return len(issues.json())


def print_top_github_repo(list_repo):
    for repo in list_repo:
        print('Name: {}'.format(repo['name']))
        print('Issues: {}'.format(get_open_issues_amount(repo['owner']['login'], repo['name'])))
        print('Link: {}\n'.format(repo['url']))


if __name__ == '__main__':
    list_top_github_repo = get_trending_repositories(top_size)
    print_top_github_repo(list_top_github_repo)
