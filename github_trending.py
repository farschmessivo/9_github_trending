import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    time_now = datetime.now()
    last_week = (time_now - timedelta(days=7)).strftime('%Y-%m-%d')
    created_less_than_week_ago = 'created:>={}'.format(last_week)
    params = {
        'q': created_less_than_week_ago,
        'sort': 'stars',
        'order': 'desc',
        'page': '1',
        'per_page': top_size
    }
    trending_repos = requests.get(url, params=params)
    return trending_repos.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    issues = requests.get(url)
    return len(issues.json())


if __name__ == '__main__':
    top_size = 20
    top_github_repos = get_trending_repositories(top_size)
    for repo in top_github_repos:
        repo_name = repo['name']
        repo_owner = repo['owner']['login']
        repo_url = repo['url']
        print('Name: {}'.format(repo_name))
        print('Issues: {}'.format(get_open_issues_amount(
            repo_owner,
            repo_name
        )))
        print('Link: {}\n'.format(repo_url))
