import streamlit as st
from utils import read_markdown_file
from consts.annotations_consts import LIBRARIES_TO_FILE_PATHS

st.header("Annotations")

library_name = st.selectbox("Library", options=LIBRARIES_TO_FILE_PATHS.keys(
), index=0, label_visibility="collapsed")

st.divider()

st.markdown(read_markdown_file(LIBRARIES_TO_FILE_PATHS[library_name]))
