import streamlit as st
from utils import read_markdown_file
from consts.anno_consts import (
    LIBRARIES_TO_FILE_PATHS,
    TABS_TITLE
)

st.header("Annotations")

library_name = st.selectbox("Library", options=LIBRARIES_TO_FILE_PATHS.keys(
), index=0, label_visibility="collapsed")

tab1, tab2, tab3 = st.tabs([title['tab-name'] for title in TABS_TITLE])

i = 0
file_path_prefix = LIBRARIES_TO_FILE_PATHS[library_name]
for tab in [tab1, tab2, tab3]:
    tab.markdown(read_markdown_file(file_path_prefix +
                 TABS_TITLE[i]['file-name'] + ".md"))
    i += 1
