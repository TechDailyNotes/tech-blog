from consts.AnnoConsts import AnnoConsts
from consts.PatternConsts import PatternConsts
from consts.ExceptionConsts import ExceptionConsts
from consts.GitConsts import GitConsts
from consts.KeyConsts import KeyConsts
from consts.QConfigConsts import QConfigConsts
from consts.RedisConsts import RedisConsts
from consts.SOAConsts import SOAConsts
from consts.SQLConsts import SQLConsts
from consts.TestConsts import TestConsts
from enums.const_enums import Constant


def import_constants(constants_src: Constant) -> {str: str}:
    if constants_src == Constant.ANNOTATIONS:
        return AnnoConsts().to_dict()
    elif constants_src == Constant.DESIGN_PATTERNS:
        return PatternConsts().to_dict()
    elif constants_src is Constant.EXCEPTION:
        return ExceptionConsts().to_dict()
    elif constants_src is Constant.GIT:
        return GitConsts().to_dict()
    elif constants_src is Constant.KEYWORDS:
        return KeyConsts().to_dict()
    elif constants_src is Constant.QCONFIG:
        return QConfigConsts().to_dict()
    elif constants_src is Constant.REDIS:
        return RedisConsts().to_dict()
    elif constants_src is Constant.SOA:
        return SOAConsts().to_dict()
    elif constants_src is Constant.SQL_TUNING:
        return SQLConsts().to_dict()
    elif constants_src is Constant.TESTING:
        return TestConsts().to_dict()
    else:
        raise ValueError(f"Unknown constant source: {constants_src}")
