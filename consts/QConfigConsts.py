from consts.Consts import Consts


class QConfigConsts(Consts):
    def __init__(self):
        self.HEADER = "QConfig"
        self.SELECTBOX_TITLE = "Components"
        self.FOLDER_NAME = "qconfig/"
        self.FILE_PATH_PREFIX = "qconfig"
        self.SELECTBOX_OPTION_TO_FILE_PATHS = {
            "Traditional Configuration": "Old",
            "Configuration Center": "Center"
        }
