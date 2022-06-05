from my import core

from .main.my import module 

# NOTE: this works if we symlink module_common into main package :shrug:
from . import module_common

print("HI FROM overlay1", __name__, __file__)
