from consts.Consts import Consts


class TestConsts(Consts):
    def __init__(self):
        self.HEADER = "Testing"
        self.SELECTBOX_TITLE = "Testing types"
        self.FOLDER_NAME = "testing"
        self.FILE_PATH_PREFIX = "test"
        self.SELECTBOX_OPTION_TO_FILE_PATHS = {
            "Unit Testing": "Unit",
            "Integration Testing": "Integration",
            "Functional Testing": "Functional"
        }
