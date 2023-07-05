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


def display_default_page(constants_src: str) -> None:
    import streamlit as st
    from utils import (
        display_default_select_box,
        read_markdown_file
    )

    consts_dict = import_constants(constants_src)

    st.header(consts_dict["HEADER"])

    option_title = display_default_select_box(
        consts_dict["SELECTBOX_TITLE"],
        consts_dict["SELECTBOX_OPTION_TO_FILE_PATHS"]
    )

    st.divider()

    file_suffix = consts_dict["SELECTBOX_OPTION_TO_FILE_PATHS"][option_title]
    st.markdown(read_markdown_file(
        consts_dict["FILE_PATH_PREFIX"] +
        file_suffix
    ))


def import_constants(constants_src: str) -> {str: str}:
    if constants_src == "anno":
        from consts.anno_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "git":
        from consts.git_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "key":
        from consts.key_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "soa":
        from consts.soa_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "test":
        from consts.test_consts import CONSTS_DICT
        return CONSTS_DICT
