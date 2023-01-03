print("Starting")

import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()

# split: http://kmkfw.io/docs/split_keyboards/
split = Split(
    split_side=SplitSide.LEFT,
    split_type=SplitType.UART,
    data_pin=board.TX,
    data_pin2=board.RX,
    use_pio=True,
    uart_flip=True)

keyboard.modules.append(split)

keyboard.modules.append(Layers())
# keyboard.debug_enabled = True

_______ = KC.TRNS
XXXXXXX = KC.NO
LOWER = KC.MO(1)
RAISE = KC.MO(2)
SPECIAL = KC.MO(3)

# macos screenshot
SHOT_SLCP = KC.LGUI(KC.LCTRL(KC.LSHIFT(KC.N4)))  # select copy
SHOT_SLSV = KC.LGUI(KC.LSHIFT(KC.N4))  # select save
SHOT_ALCP = KC.LGUI(KC.LCTRL(KC.LSHIFT(KC.N3)))  # all copy
SHOT_ALSV = KC.LGUI(KC.LSHIFT(KC.N3))  # all save

keyboard.keymap = [
   # 0 = BASE
   [
        KC.TAB, 	KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,       KC.Y,	    KC.U,       KC.I,		KC.O,		KC.P,		KC.BSPACE,
        KC.ESC,		KC.A,		KC.S,		KC.D,		KC.F,		KC.G,		KC.H,       KC.J,		KC.K,		KC.L,       KC.SCOLON,  KC.ENTER,
        KC.LSHIFT,	KC.Z,		KC.X,		KC.C,		KC.V,		KC.B,		KC.N,		KC.M,		KC.COMMA,	KC.DOT,		KC.SLASH,	KC.QUOTE,
        XXXXXXX,    KC.LCTRL,	KC.LALT,    KC.LGUI,	LOWER,  	KC.SPACE,   KC.SPACE,	RAISE,  	SPECIAL,	KC.PGDN,    KC.PGUP,
   ],
   # 1 = LOWER
   [
        KC.TILDE,   KC.EXLM, 	KC.AT,		KC.HASH,    KC.DOLLAR,  KC.PERCENT, KC.CIRC,    KC.AMPR,    KC.ASTR,	KC.LPRN,    KC.RPRN,    KC.BSPACE,
        KC.DEL,		KC.F1,      KC.F2,		KC.F3,		KC.F4,		KC.F5,		KC.F6,   	KC.UNDS,	KC.PLUS,	KC.LCBR,    KC.RCBR,    KC.PIPE,
        _______,	KC.F7,		KC.F8,		KC.F9,		KC.F10,		KC.F11,		KC.F12,		_______,    _______,	KC.HOME,    KC.END,	    _______,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
   ],
   # 2 = RAISE
   [
        KC.TAB,     KC.N1, 	    KC.N2,		KC.N3,		KC.N4,		KC.N5,		KC.N6,      KC.N7,	 	KC.N8,	    KC.N9,		KC.N0,		KC.BSPACE,
        KC.DEL,		KC.F1,      KC.F2,		KC.F3,		KC.F4,		KC.F5,		KC.F6,   	KC.MINUS,	KC.EQUAL,	KC.LBRC,    KC.RBRC,    KC.BSLASH,
        _______,	KC.F7,		KC.F8,		KC.F9,		KC.F10,		KC.F11,		KC.F12,		KC.F13,     KC.F14,     KC.F15,     KC.F16,     KC.F17,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
   ],
   # 3 = SPECIAL
   [
        SHOT_SLCP,  SHOT_SLSV,  XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,   XXXXXXX,     XXXXXXX,
        SHOT_ALCP,  SHOT_ALSV,  XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,   XXXXXXX,     XXXXXXX,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,   XXXXXXX,     XXXXXXX,
        KC.RESET,   XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,   XXXXXXX,
   ],
]

if __name__ == '__main__':
    keyboard.go()
