import streamlit as st
from utils import read_markdown_file

st.header("Exception")

tab1 = st.tabs(["Questions"])

tab1[0].markdown(read_markdown_file("exceptionQuestions"))
