import requests
import random



def get_random_repos(language="python", stars=">=1000", per_page=10):
    url = f"https://api.github.com/search/repositories?q=language:{language}+stars:{stars}&per_page={per_page}"
    response = requests.get(url)
    data = response.json()
    repos = data.get("items", [])
    return repos

def select_random_repo(repos):
    return random.choice(repos)

def get_repo_details(repo):
    url = repo["url"]
    response = requests.get(url)
    if response.status_code == 200:
        repo_details = response.json()
        return repo_details
    else:
        print(f"Failed to fetch repository details: {response.status_code}")
        return None

def generate_details():
    repos = get_random_repos()
    random_repo = select_random_repo(repos)
    repo_details = get_repo_details(random_repo)
    return repo_details