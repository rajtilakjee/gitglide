import requests
import random
import streamlit as st 



st.set_page_config(
    page_title="GitGlide",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header('Git:blue[Glide]')
st.subheader('Discover your Code Crush', divider='rainbow')

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

if __name__ == "__main__":
    repos = get_random_repos()
    random_repo = select_random_repo(repos)
    repo_details = get_repo_details(random_repo)

    if repo_details:
        st.markdown("## Repository Details:")
        st.write(f"Name: {repo_details['name']}")
        st.write(f"Description: {repo_details['description']}")
        st.write(f"Language: {repo_details['language']}")
        st.write(f"Stars: {repo_details['stargazers_count']}")
        st.write(f"Forks: {repo_details['forks_count']}")
        st.write(f"URL: {repo_details['html_url']}")
        st.write("\nREADME:")
        readme_url = repo_details['url'] + '/readme'
        readme_response = requests.get(readme_url)
        if readme_response.status_code == 200:
            readme_content = readme_response.json().get('content')
            # The content is Base64 encoded, decode it
            import base64
            readme_text = base64.b64decode(readme_content).decode('utf-8')
            st.markdown(readme_text)
        else:
            st.write(f"Failed to fetch README: {readme_response.status_code}")