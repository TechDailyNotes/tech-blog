import streamlit as st
from utils import read_markdown_file

st.header("Redis")

tab1, tab2, tab3 = st.tabs(["Concepts", "Scenarios", "Theories"])

with tab1:
    st.markdown(read_markdown_file("redisConcepts"))
