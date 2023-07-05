import streamlit as st


def display_default_select_box(selectbox_title: str, selectbox_title_to_file_paths: str) -> str:
    return st.selectbox(selectbox_title,
                        options=selectbox_title_to_file_paths.keys(),
                        index=0, label_visibility="collapsed")
