from os import getenv


from .controller import GameController

__all__ = [
    'GameController'
]


if getenv("RUNNING_TESTS"):
    from common import *
    from controller import *
    from model import *
    from  view import *

    __all__ = [
        ''
    ]
