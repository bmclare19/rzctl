import ctypes 
import sys
from os import path

# get the values for the function calls by using (64 bit version)
# dumpbin /exports rzctl.dll

def root_dir():
    try:
        return sys._MEIPASS
    except Exception:
        return path.abspath(".")

ROOT_DIR = root_dir()

lib = ctypes.CDLL(path.join(ROOT_DIR, 'out\\rzctl.dll'))
rzctl_init = getattr(lib, "?init@rzctl@@YA_NXZ")
rzctl_init.restype = ctypes.c_bool

rzctl_mouse_click = getattr(lib, "?mouse_click@rzctl@@YAXH@Z")
rzctl_mouse_click.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_bool]
rzctl_mouse_click.restype = None

rzctl_mouse_move = getattr(lib, "?mouse_move@rzctl@@YAXHH_N@Z")
rzctl_mouse_move.argtypes = [ctypes.c_int]
rzctl_mouse_move.restype = None

rzctl_key_state = getattr(lib, "?key_state@rzctl@@YAXFF@Z")
rzctl_key_state.argtypes = [ctypes.c_int16, ctypes.c_int16]
rzctl_key_state.restype = None

from time import sleep

while True:
    rzctl_key_state(30, 0)
    sleep(0.05)
    rzctl_key_state(30, 1)
    sleep(1)