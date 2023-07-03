import streamlit as st
from utils import read_markdown_file

st.header("Git")

tab1 = st.tabs(["Commands", "Theories"])

with tab1:
  st.markdown(read_markdown_file("gitCommands.md"))
