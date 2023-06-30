import streamlit as st
from utils import read_markdown_file

st.markdown(read_markdown_file("README.md", True))
