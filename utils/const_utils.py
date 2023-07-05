from enums.const_enums import Constant


def import_constants(constants_src: Constant) -> {str: str}:
    if constants_src == Constant.ANNOTATIONS:
        from consts.anno_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is Constant.EXCEPTION:
        from consts.exception_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is Constant.GIT:
        from consts.git_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is Constant.KEYWORDS:
        from consts.key_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is Constant.REDIS:
        from consts.redis_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is Constant.SOA:
        from consts.soa_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is Constant.TESTING:
        from consts.test_consts import CONSTS_DICT
        return CONSTS_DICT
