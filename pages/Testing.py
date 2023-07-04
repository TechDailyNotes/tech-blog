import streamlit as st
from utils import read_markdown_file
from consts.test_consts import (
    FILE_PATH_PREFIX,
    TESTING_TITLE_TO_FILE_PATHS
)

st.header("Testing")

test_type_name = st.selectbox("Testing types", options=TESTING_TITLE_TO_FILE_PATHS.keys(
), index=0, label_visibility="collapsed")

st.divider()

test_file_suffix = TESTING_TITLE_TO_FILE_PATHS[test_type_name]
st.markdown(read_markdown_file(FILE_PATH_PREFIX + test_file_suffix))
