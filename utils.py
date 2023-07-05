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


# def display_default_page(constants_src: str) -> None:
#     import streamlit as st
#     from utils import (
#         display_default_select_box,
#         read_markdown_file
#     )

#     import_constants(constants_src)

#     st.header(consts.HEADER)

#     option_title = display_default_select_box(
#         consts.SELECTBOX_TITLE, consts.SELECTBOX_OPTION_TO_FILE_PATHS)

#     st.divider()

#     file_suffix = consts.SELECTBOX_OPTION_TO_FILE_PATHS[option_title]
#     st.markdown(read_markdown_file(consts.FILE_PATH_PREFIX + file_suffix))


# def import_constants(constants_src: str):
#     if constants_src == "anno":
#         import consts.anno_consts as consts
    # elif constants_src is "common":
    #     from consts.common_consts import *
    # elif constants_src is "git":
    #     from consts.git_consts import *
    # elif constants_src is "key":
    #     from consts.key_consts import *
    # elif constants_src is "soa":
    #     from consts.soa_consts import *
    # elif constants_src is "test":
    #     from consts.test_consts import *
