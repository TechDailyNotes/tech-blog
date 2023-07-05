class Consts:
    def __init__(self):
        self.HEADER: str = ""
        self.SELECTBOX_TITLE: str = ""
        self.FOLDER_NAME: str = ""
        self.FILE_PATH_PREFIX: str = ""
        self.SELECTBOX_OPTION_TO_FILE_PATHS: {str: str} = {}

    def to_dict(self):
        return {
            "HEADER": self.HEADER,
            "SELECTBOX_TITLE": self.SELECTBOX_TITLE,
            "FOLDER_NAME": self.FOLDER_NAME,
            "FILE_PATH_PREFIX": self.FILE_PATH_PREFIX,
            "SELECTBOX_OPTION_TO_FILE_PATHS": self.SELECTBOX_OPTION_TO_FILE_PATHS
        }
