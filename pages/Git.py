import streamlit as st
from utils import read_markdown_file

commands_to_file_name_map = {
  "Branch": "gitCommands.md",
  "Cherry Pick": "gitCherryPick.md"
}

def show_git_commands(file_name: str) -> void:
  st.markdown(read_markdown_file(file_name))

st.header("Git")
file_name = st.selectbox("Commands", options = ["Branch", "Cherry Pick"])
show_git_commands(commands_to_file_name_map[file_name])
