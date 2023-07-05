from consts.Consts import Consts


class SOAConsts(Consts):
    def __init__(self):
        self.HEADER = "SOA"
        self.SELECTBOX_TITLE = "Components"
        self.FOLDER_NAME = "soa"
        self.FILE_PATH_PREFIX = "soa"
        self.SELECTBOX_OPTION_TO_FILE_PATHS = {
            "Concepts": "Concepts",
            "Development": "Dev",
            "Dubbo": "Dubbo"
        }
