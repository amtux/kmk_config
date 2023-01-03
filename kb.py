import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9,)
    row_pins = (board.A0, board.A1, board.A2, board.A3,)
    diode_orientation = DiodeOrientation.COL2ROW
