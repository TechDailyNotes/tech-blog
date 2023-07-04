import streamlit as st
from utils import read_markdown_file
from consts.git_consts import GIT_COMMANDS_TO_FILE_PATHS

st.header("Git Commands")

command_name = st.selectbox(
    "Command names", options=GIT_COMMANDS_TO_FILE_PATHS.keys(), index=0, label_visibility="collapsed")

st.markdown(read_markdown_file(GIT_COMMANDS_TO_FILE_PATHS[command_name]))
