import streamlit as st

from enums.const_enums import Constant


def display_default_page(constants_src: Constant) -> None:
    from utils.component_utils import display_default_select_box
    from utils.const_utils import import_constants
    from utils.doc_utils import read_markdown_doc

    consts_dict = import_constants(constants_src=constants_src)

    st.header(consts_dict["HEADER"])

    option_title = display_default_select_box(
        selectbox_title=consts_dict["SELECTBOX_TITLE"],
        selectbox_title_to_file_paths=consts_dict["SELECTBOX_OPTION_TO_FILE_PATHS"]
    )

    st.divider()

    file_suffix = consts_dict["SELECTBOX_OPTION_TO_FILE_PATHS"][option_title]
    st.markdown(read_markdown_doc(
        markdown_doc_name=consts_dict["FILE_PATH_PREFIX"] + file_suffix,
        folder_name=consts_dict["FOLDER_NAME"]
    ))
