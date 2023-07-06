from consts.Consts import Consts


class PatternConsts(Consts):
    def __init__(self):
        self.HEADER = "Design Patterns"
        self.SELECTBOX_TITLE = "Classification"
        self.FOLDER_NAME = "design-patterns/"
        self.FILE_PATH_PREFIX = "pattern"
        self.SELECTBOX_OPTION_TO_FILE_PATHS = {
            "Design Principals": "Principal",
            "Creational Patterns": "Creational",
            "Structural Patterns": "Structural",
            "Behavioral Patterns": "Behavioral"
        }
