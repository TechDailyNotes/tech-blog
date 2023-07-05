from consts.Consts import Consts


class AnnoConsts(Consts):
    def __init__(self):
        self.HEADER = "Annotations"
        self.SELECTBOX_TITLE = "Packages"
        self.FOLDER_NAME = "annotations/"
        self.FILE_PATH_PREFIX = "anno"
        self.SELECTBOX_OPTION_TO_FILE_PATHS = {
            "Jackson": "Jackson",
            "Javax": "Javax",
            "JUnit": "JUnit",
            "Mockito": "Mockito",
            "PowerMockito": "PowerMock",
        }
