def import_constants(constants_src: str) -> {str: str}:
    if constants_src == "anno":
        from consts.anno_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "git":
        from consts.git_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "key":
        from consts.key_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "soa":
        from consts.soa_consts import CONSTS_DICT
        return CONSTS_DICT
    elif constants_src is "test":
        from consts.test_consts import CONSTS_DICT
        return CONSTS_DICT
