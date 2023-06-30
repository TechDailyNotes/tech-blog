from pathlib import Path
import os


path_prefix = os.getcwd() + "/docs/"


def read_markdown_file(markdown_file, is_home_page=False):
    if is_home_page:
        return Path(markdown_file).read_text()
    return Path(path_prefix + markdown_file).read_text()
