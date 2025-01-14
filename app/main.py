import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils  import cleanText


def createStreamLitApp(llm, portfolio, cleanText):
    st.title('Cold Email generator')
    url_input = st.text_input('Enter the URL:')
    submit_button = st.button('Generate email')


    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = cleanText(loader.load().pop().page_content)
            portfolio.loadPortfolio()
            jobs = llm.extractJobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.queryLinks(skills)
                email = llm.writeEmail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    chain = Chain()
    Portfolio = Portfolio()
    st.set_page_config(layout="wide",page_title="Cold Email Generator", page_icon="📧") 
    createStreamLitApp(chain, Portfolio, cleanText)


