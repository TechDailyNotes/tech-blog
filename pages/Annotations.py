import streamlit as st
from utils import read_markdown_file
from consts.anno_consts import (
    LIBRARIES_TO_FILE_PATHS,
    TABS_TITLE
)

st.header("Annotations")

library_name = st.selectbox("Library", options=LIBRARIES_TO_FILE_PATHS.keys(
), index=0, label_visibility="collapsed")

file_path_prefix = LIBRARIES_TO_FILE_PATHS[library_name]

tab1, tab2, tab3 = st.tabs(TABS_TITLE)

tab1.markdown(read_markdown_file(file_path_prefix + TABS_TITLE[0] + ".md"))
tab2.markdown(read_markdown_file(file_path_prefix + TABS_TITLE[1] + ".md"))
tab3.markdown(read_markdown_file(file_path_prefix + TABS_TITLE[2] + ".md"))
