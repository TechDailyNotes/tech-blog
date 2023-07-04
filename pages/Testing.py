import streamlit as st
from utils import read_markdown_file

st.header("Testing")

st.divider()

st.markdown(read_markdown_file("test.md"))
