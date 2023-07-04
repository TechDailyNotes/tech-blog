import streamlit as st
from utils import read_markdown_file
from consts.keywords_consts import LANGUAGES_TO_FILE_PATHS

st.header("Keywords")

langugae_name = st.selectbox(
    "Languages", options=LANGUAGES_TO_FILE_PATHS.keys(), label_visibility="collapsed", index=0)

st.markdown(read_markdown_file(LANGUAGES_TO_FILE_PATHS[langugae_name]))
