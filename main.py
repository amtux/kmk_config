print("Starting")

import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.modtap import ModTap
from storage import getmount

keyboard = KMKKeyboard()
# keyboard.debug_enabled = True

# MODTAP: http://kmkfw.io/docs/modtap/
modtap = ModTap()
modtap.tap_time = 150  # ms
keyboard.modules.append(modtap)

# SPLIT: http://kmkfw.io/docs/split_keyboards/
# decide side based on label assigned to the storage of the board
# CIRCUITPYL is the left side, CIRCUITPYR is the right side
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(
        split_side=side,
        split_type=SplitType.UART,
        data_pin=board.TX,
        data_pin2=board.RX,
        use_pio=True,
        uart_flip=True)
keyboard.modules.append(split)

# LAYERS: http://kmkfw.io/docs/layers
keyboard.modules.append(Layers())


# KEYCODES: http://kmkfw.io/docs/keycodes/
_______ = KC.TRNS
XXXXXXX = KC.NO

# modtap based layers
NAV_LAYER = KC.MO(1)
SPC_NAV = KC.MT(KC.SPACE, NAV_LAYER)
NUM_LAYER = KC.MO(2)
BSPC_NUM = KC.MT(KC.BSPACE, NUM_LAYER)
SYM_LAYER = KC.MO(3)
ENT_SYM = KC.MT(KC.ENTER, SYM_LAYER)
FUN_LAYER = KC.MO(4)
SHFT_FUN = KC.MT(KC.LSHIFT, FUN_LAYER)

# nav layer combos
REDO = KC.LGUI(KC.LSHIFT(KC.Z))
PASTE = KC.LGUI(KC.V)
COPY = KC.LGUI(KC.C)
CUT = KC.LGUI(KC.X)
UNDO = KC.LGUI(KC.Z)

# macos screenshot combos
SHOT_SLCP = KC.LGUI(KC.LCTRL(KC.LSHIFT(KC.N4)))  # select copy
SHOT_SLSV = KC.LGUI(KC.LSHIFT(KC.N4))  # select save
SHOT_ALCP = KC.LGUI(KC.LCTRL(KC.LSHIFT(KC.N3)))  # all copy
SHOT_ALSV = KC.LGUI(KC.LSHIFT(KC.N3))  # all save

miryoku = [
        # QWERTY base
        [
            KC.TAB, 	KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,       KC.Y,	    KC.U,       KC.I,		KC.O,		KC.P,		KC.BSPACE,
            KC.ESC,		KC.A,		KC.S,		KC.D,		KC.F,		KC.G,		KC.H,       KC.J,		KC.K,		KC.L,       KC.SCOLON,  KC.ENTER,
            KC.LSHIFT,	KC.Z,		KC.X,		KC.C,		KC.V,		KC.B,		KC.N,		KC.M,		KC.COMMA,	KC.DOT,		KC.SLASH,	KC.QUOTE,
            XXXXXXX,    KC.LCTRL,   KC.LALT,    KC.ESC,     SPC_NAV,    KC.TAB,     ENT_SYM,    BSPC_NUM,   SHFT_FUN,   KC.RGUI,    KC.RCTRL,
            ],
        # SPC->NAV
        [
            XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    REDO,       PASTE,      COPY,       CUT,        UNDO,       XXXXXXX,
            XXXXXXX,    KC.LGUI,    KC.LALT,    KC.LCTRL,   KC.LSHIFT,  XXXXXXX,    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   XXXXXXX,    XXXXXXX,
            XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.INSERT,  KC.HOME,    KC.PGDN,    KC.PGUP,    KC.END,     XXXXXXX,
            XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.ENTER,   KC.BSPACE,  KC.DEL,     XXXXXXX,    XXXXXXX,
            ],
        # BSPC->NUM
        [
            XXXXXXX,    KC.LBRC,    KC.N7,      KC.N8,      KC.N9,      KC.RBRC,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            XXXXXXX,    KC.SCOLON,  KC.N4,      KC.N5,      KC.N6,      KC.EQUAL,   XXXXXXX,    KC.LSHIFT,  KC.LCTL,    KC.LALT,    KC.LGUI,    XXXXXXX,
            XXXXXXX,    KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.BSLASH,  XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.DOT,     KC.N0,      KC.MINUS,   XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            ],
        # ENT->SYM
        [
            XXXXXXX,    KC.LCBR,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RCBR,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            XXXXXXX,    KC.COLON,   KC.DOLLAR,  KC.PERCENT, KC.CIRC,    KC.PLUS,    XXXXXXX,    KC.LSHIFT,  KC.LCTL,    KC.LALT,    KC.LGUI,    XXXXXXX,
            XXXXXXX,    KC.TILDE,   KC.EXLM,    KC.AT,      KC.HASH,    KC.PIPE,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.LPRN,    KC.RPRN,    KC.UNDS,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            ],
        # DEL->FUN
        [
            XXXXXXX,    KC.F12,     KC.F7,      KC.F8,      KC.F9,      KC.PSCR,    XXXXXXX,    SHOT_SLCP,  SHOT_SLSV,  SHOT_ALCP,  SHOT_ALSV,  XXXXXXX,
            XXXXXXX,    KC.F11,     KC.F4,      KC.F5,      KC.F6,      XXXXXXX,    XXXXXXX,    KC.LSHIFT,  KC.LCTL,    KC.LALT,    KC.LGUI,    XXXXXXX,
            XXXXXXX,    KC.F10,     KC.F1,      KC.F2,      KC.F3,      XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.ESC,     KC.SPACE,   KC.TAB,     XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
            ],
        ]

keyboard.keymap = miryoku

if __name__ == '__main__':
    keyboard.go()
