import streamlit as st
from utils import (
    display_default_select_box,
    read_markdown_file
)
from consts.key_consts import (
    HEADER,
    SELECTBOX_TITLE,
    FILE_PATH_PREFIX,
    SELECTBOX_OPTION_TO_FILE_PATHS
)

st.header(HEADER)

option_title = display_default_select_box(
    SELECTBOX_TITLE, SELECTBOX_OPTION_TO_FILE_PATHS)

st.divider()

file_suffix = SELECTBOX_OPTION_TO_FILE_PATHS[option_title]
st.markdown(read_markdown_file(FILE_PATH_PREFIX + file_suffix))
