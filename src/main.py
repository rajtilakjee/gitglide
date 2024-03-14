import streamlit as st 
from utils import get_repo_details
import requests



st.set_page_config(
    page_title="GitGlide",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header('Git:blue[Glide]')
st.subheader('Discover your Code Crush', divider='rainbow')

def like_repo():
    return get_repo_details.generate_details()

if __name__ == "__main__":
    repo_details = ""
    if st.button("👍🏻 Like", type="primary"):
        repo_details = get_repo_details.generate_details()

    st.button("👉🏻 Next")

    container = st.container(border=True)
    if repo_details:
        with container:
            st.markdown("### Repository Details:")
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
                st.write(readme_text)
            else:
                st.write(f"Failed to fetch README: {readme_response.status_code}")
