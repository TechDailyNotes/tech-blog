import streamlit as st


def display_default_page(constants_src: str) -> None:
    from utils.component_utils import display_default_select_box
    from utils.const_utils import import_constants
    from utils.doc_utils import read_markdown_doc

    consts_dict = import_constants(constants_src)

    st.header(consts_dict["HEADER"])

    option_title = display_default_select_box(
        consts_dict["SELECTBOX_TITLE"],
        consts_dict["SELECTBOX_OPTION_TO_FILE_PATHS"]
    )

    st.divider()

    file_suffix = consts_dict["SELECTBOX_OPTION_TO_FILE_PATHS"][option_title]
    st.markdown(read_markdown_doc(
        consts_dict["FILE_PATH_PREFIX"] +
        file_suffix
    ))
