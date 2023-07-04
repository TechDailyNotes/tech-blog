from pathlib import Path
from consts.common_consts import FILE_PATH_SUFFIX
import os
import streamlit as st


path_prefix = os.getcwd() + "/docs/"


def read_markdown_file(markdown_file, is_home_page=False):
    if is_home_page:
        return Path(markdown_file).read_text()
    return Path(path_prefix + markdown_file + FILE_PATH_SUFFIX).read_text()


def display_default_select_box(selectbox_title: str, selectbox_title_to_file_paths: str) -> str:
    return st.selectbox(selectbox_title,
                        options=selectbox_title_to_file_paths.keys(), index=0, label_visibility="collapsed")
