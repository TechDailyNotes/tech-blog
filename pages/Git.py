import streamlit as st
from utils import read_markdown_file

st.header("Git")

tab1, tab2 = st.tabs(["Branch", "Cherry Pick"])

with tab1:
  st.markdown(read_markdown_file("gitBranches.md"))

with tab2:
  st.markdown(read_markdown_file("gitCherryPick.md"))
