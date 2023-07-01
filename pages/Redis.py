import streamlit as st
from utils import read_markdown_file

tab1, tab2, tab3 = st.tabs(["Basics", "Scenarios", "Theories"])

with tab1:
  st.markdown(read_markdown_file("Redis.md"))
