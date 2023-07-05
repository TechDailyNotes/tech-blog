import streamlit as st
from utils.doc_utils import read_markdown_doc

st.markdown(read_markdown_doc("README.md", is_home_page=True))
