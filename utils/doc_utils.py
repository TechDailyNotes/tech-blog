import os

from pathlib import Path
from consts.common_consts import (
    DIRECTORY_PREFIX,
    FILE_PATH_SUFFIX
)

path_prefix = os.getcwd() + DIRECTORY_PREFIX


def read_markdown_doc(
        markdown_doc_name: str,
        folder_name: str = "",
        is_home_page: bool = False
) -> str:
    if is_home_page:
        return Path(markdown_doc_name).read_text()
    return Path(
        path_prefix
        + folder_name
        + markdown_doc_name
        + FILE_PATH_SUFFIX
    ).read_text()
