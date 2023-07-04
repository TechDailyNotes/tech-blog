import streamlit as st
from utils import read_markdown_file
from consts.anno_consts import (
    FILE_PATH_PREFIX,
    LIBRARIES_TITLE
)

st.header("Annotations")

library_name = st.selectbox(
    "Library", options=LIBRARIES_TITLE, index=0, label_visibility="collapsed")

st.divider()

st.markdown(read_markdown_file(FILE_PATH_PREFIX + library_name + ".md"))
