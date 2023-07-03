import streamlit as st
from utils import read_markdown_file

tab1, tab2, tab3 = st.tabs(3)

with tab1:
  st.markdown(read_markdown_file("git.md"))
