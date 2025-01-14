CARET_SIZES = {
    "16": "19x14",
    "24": "29x21",
    "36": "44x32"
}


CARET_PADDING = {
    "16": "6",
    "24": "10",
    "36": "15"
}


class COLORS:
    BLACK = "0,0,0"
    EM_BLUE = "0,93,170"
    EM_GRAY = "210,210,210"
    WHITE = "255,255,255"


DRIVE_LABELS = {
    'C': 'system',
    'D': 'flash',
    'E': 'ram'
}


FILE_LABELS ={
    '!': '!', 
    '"': '"', 
    '#': '#', 
    '$': '$', 
    '%': '%', 
    '&': '&', 
    "'": "'", 
    '(': '(', 
    ')': ')',
    '*': '*', 
    '+': '+', 
    ',': ',', 
    '-': '-', 
    '.': '.', 
    '/': '/', 
    '0': '0', 
    '1': '1', 
    '2': '2',
    '3': '3', 
    '4': '4', 
    '5': '5', 
    '6': '6', 
    '7': '7', 
    '8': '8', 
    '9': '9', 
    ':': ':', 
    ';': ';',
    '<': '<', 
    '=': '=', 
    '>': '>', 
    '?': '?', 
    '@': '@', 
    'A': 'A', 
    'B': 'B', 
    'C': 'C', 
    'D': 'D',
    'E': 'E', 
    'F': 'F', 
    'G': 'G', 
    'H': 'H', 
    'I': 'I', 
    'J': 'J', 
    'K': 'K', 
    'L': 'L', 
    'M': 'M',
    'N': 'N', 
    'O': 'O', 
    'P': 'P', 
    'Q': 'Q', 
    'R': 'R', 
    'S': 'S', 
    'T': 'T', 
    'U': 'U', 
    'V': 'V',
    'W': 'W', 
    'X': 'X', 
    'Y': 'Y', 
    'Z': 'Z', 
    '[': '[', 
    '\\': '\\', 
    ']': ']', 
    '^': '^', 
    '_': '_',
    '`': '`', 
    'a': 'a', 
    'b': 'b', 
    'c': 'c', 
    'd': 'd', 
    'e': 'e', 
    'f': 'f', 
    'g': 'g', 
    'h': 'h',
    'i': 'i', 
    'j': 'j', 
    'k': 'k', 
    'l': 'l', 
    'm': 'm', 
    'n': 'n', 
    'o': 'o', 
    'p': 'p', 
    'q': 'q',
    'r': 'r', 
    's': 's', 
    't': 't', 
    'u': 'u', 
    'v': 'v', 
    'w': 'w', 
    'x': 'x', 
    'y': 'y', 
    'z': 'z',
    '{': '{', 
    '|': '|', 
    '}': '}'
}


FOLDER_LABELS = {
    "P": "picture",
    "S": "string",
    "T": "text"
}


class FONT_SIZES:
    _16 = "16"
    _24 = "24"
    _36 = "36"


GROUP_IDS = {
    "None": "None",
    '00': '00',
    '01': '01',
    '02': '02',
    '03': '03',
    '04': '04',
    '05': '05',
    '06': '06',
    '07': '07',
    '08': '08',
    '09': '09',
    '10': '10',
    '11': '11',
    '12': '12',
    '13': '13',
    '14': '14',
    '15': '15',
    '16': '16',
    '17': '17',
    '18': '18',
    '19': '19',
    '20': '20',
    '21': '21',
    '22': '22',
    '23': '23',
    '24': '24',
    '25': '25',
    '26': '26',
    '27': '27',
    '28': '28',
    '29': '29',
    '30': '30',
    '31': '31',
    '32': '32',
    '33': '33',
    '34': '34',
    '35': '35',
    '36': '36',
    '37': '37',
    '38': '38',
    '39': '39',
    '40': '40',
    '41': '41',
    '42': '42',
    '43': '43',
    '44': '44',
    '45': '45',
    '46': '46',
    '47': '47',
    '48': '48',
    '49': '49',
    '50': '50',
    '51': '51',
    '52': '52',
    '53': '53',
    '54': '54',
    '55': '55',
    '56': '56',
    '57': '57',
    '58': '58',
    '59': '59',
    '60': '60',
    '61': '61',
    '62': '62',
    '63': '63',
    '64': '64',
    '65': '65',
    '66': '66',
    '67': '67',
    '68': '68',
    '69': '69',
    '70': '70',
    '71': '71',
    '72': '72',
    '73': '73',
    '74': '74',
    '75': '75',
    '76': '76',
    '77': '77',
    '78': '78',
    '79': '79',
    '80': '80',
    '81': '81',
    '82': '82',
    '83': '83',
    '84': '84',
    '85': '85',
    '86': '86',
    '87': '87',
    '88': '88',
    '89': '89',
    '90': '90',
    '91': '91',
    '92': '92',
    '93': '93',
    '94': '94',
    '95': '95',
    '96': '96',
    '97': '97',
    '98': '98',
    '99': '99'
}


HEIGHT_LABEL_LOOKUP = {
    "16": 51,
    "24": 75,
    "36": 113
}


HEIGHT_VALUE_LOOKUP = {
    "16": 33,
    "24": 49,
    "36": 73
}


HEIGHT_BUTTON_LOOKUP = {
    "16": HEIGHT_LABEL_LOOKUP["16"] + HEIGHT_VALUE_LOOKUP["16"],
    "24": HEIGHT_LABEL_LOOKUP["24"] + HEIGHT_VALUE_LOOKUP["24"],
    "36": HEIGHT_LABEL_LOOKUP["36"] + HEIGHT_VALUE_LOOKUP["36"]
}


MESSAGE_MODES = [
    "content",
    "settings",
    "variable"
]


ADDRESS_MODES = [
    "basic",
    "advanced"
]


PADDING = {
    "16": 5,
    "24": 30,
    "36": 45
}


SETTINGS_VALUES = {
    "clear_flash_and_ram": '$$$$',  
    "clear_ram": '$',      
    "clear_playlist": '.', 
    "set_date": ';',       
    "set_day_of_week": '&',
    "set_defaults": '#',   
    "set_playlist": '.SL', 
    "set_time": ' ',       
    "set_time_format": "'"
}


DAY_OF_WEEK = {
    "sunday": "1",
    "monday": "2",
    "tuesday": "3",
    "wednesday": "4",
    "thursday": "5",
    "friday": "6",
    "saturday": "7"
}


TIME_FORMAT = {
    "12 hour": "S",
    "24 hour": "M"
}


DEFAULT_COLORS = {
    "black": "0", 
    "red": "1", 
    "green": "2", 
    "yellow": "3"
}


DEFAULT_DRIVES ={
    "flash": "D",
    "RAM": "E"
}


DEFAULT_FONTS = {
    "normal 5": "0",
    "normal 7": "1",
    "normal 14": "2",
    "normal 15": "3",
    "normal 16": "4",
    "bold 14": "5",
    "bold 15": "6",
    "bold 16": "7"
}


DEFAULT_HOLD_TIMES = {
    "1 second": "1",
    "2 seconds": "2",
    "3 seconds": "3",
    "4 seconds": "4",
    "5 seconds": "5",
    "6 seconds": "6",
    "7 seconds": "7",
    "8 seconds": "8",
    "9 seconds": "9"
}


DEFAULT_HORIZONTAL_ALIGNMENTS = {
    "center": "C",
    "left": "L",
    "right": "R"
}


DEFAULT_MODES = {
    "Rotate": "a",
    "Hold": "b",
    "Flash": "c",
    "Random": "d",
    "Move left": "e",
    "Move right": "f",
    "Scroll O/L": "g",
    "Scroll O/R": "h",
    "Move up": "i",
    "Move down": "j",
    "Scroll O/C": "k",
    "Unveil up": "l",
    "Unveil down": "m",
    "Unveil in": "n",
    "Unveil up/in": "o",
    "Unveil up/out": "p",
    "Splice": "q",
    "Splice": "r",
    "Fall": "s",
    "Fall": "t",
    "VenetianHor": "u",
    "VenetianVer": "v",
    "Rain": "w",
    "Materialize": "x",
    "Twinkle": "z",
    "Squiggle": "1",
    "Radar": "2",
    "FanOpen": "3",
    "FanClose": "4",
    "RotateRight": "5",
    "RotateLeft": "6",
    "Center2Corner": "7",
    "Corner2center": "8",
    "Center2Allsz": "9",
    "Alls2Center": "A",
    "FourBlock2Cor": "B",
    "FourBlock2Cen": "C",
    "FourBlockOut": "D",
    "FourBlockIn": "E",
    "LeftCorRectIn": "F",
    "RightCorRectIn": "G",
    "LBottomRectI": "H",
    "RBottomRectI": "I",
    "LftCoDiagonal": "J",
    "RtCoDiagonalI": "K",
    "LBtmDiagonal": "L",
    "RBtmDiagonal": "M",
    "Lft2RtDownCor": "N",
    "Rt2LftDownCor": "",
    "Left2RtUpCor": "P",
    "Rit2LftUpCor": "Q",
    "GrowUp": "R"
}


DEFAULT_LINE_SPACINGS = {
    "1 pixel": "1",
    "2 pixels": "2",
    "3 pixels": "3",
    "4 pixels": "4",
    "5 pixels": "5",
    "6 pixels": "6",
    "7 pixels": "7",
    "8 pixels": "8",
    "9 pixels": "9"
}


DEFAULT_SCROLL_SPEEDS = {
    "slowest": "1",
    "slow": "2",
    "normal": "3",
    "fast": "4",
    "fastest": "5"
}


DEFAULT_VERTICAL_ALIGNMENTS = {
    "bottom": "B",
    "center": "C",
    "fill": "F",
    "top": "T"
}


DEFAULT_WRAPS = {
    "off": "0",
    "on": "1"
}


SETTINGS_DEFAULTS = {
    "background_color": {
        "key": "B",
        "values": DEFAULT_COLORS
    },
    "drive": {
        "key": "D",
        "values": DEFAULT_DRIVES
    },
    "font": {
        "key": "F",
        "values": DEFAULT_FONTS
    },
    "foreground_color": {
        "key": "C",
        "values": DEFAULT_COLORS
    },
    "hold_time": {
        "key": "T",
        "values": DEFAULT_HOLD_TIMES
    },
    "horizontal_alignment": {
        "key": "V",
        "values": DEFAULT_HORIZONTAL_ALIGNMENTS
    },
    "in_mode": {
        "key": "M",
        "values": DEFAULT_MODES
    },
    "line_spacing": {
        "key": "L",
        "values": DEFAULT_LINE_SPACINGS
    }, 
    "out_mode": {
        "key": "O",
        "values": DEFAULT_MODES
    },
    "scroll_speed": {
        "key": "S",
        "values": DEFAULT_SCROLL_SPEEDS
    },
    "vertical_alignment": {
        "key": "H",
        "values": DEFAULT_VERTICAL_ALIGNMENTS
    },
    "wrap": {
        "key": "W",
        "values": DEFAULT_WRAPS
    }
}


# SETTINGS_VALUES = {   
#     "clear_flash_and_ram": "E$$$$",
#     "clear_ram": "E$",
#     "clear_playlist": "E.",
#     "set_date": None,
#     "set_day_of_week": None,
#     "set_defaults": None,
#     "set_playlist": None,
#     "set_time": None,
#     "set_time_format": None      
# }


SIGN_IDS = {
    '00': '00',
    '01': '01',
    '02': '02',
    '03': '03',
    '04': '04',
    '05': '05',
    '06': '06',
    '07': '07',
    '08': '08',
    '09': '09',
    '10': '10',
    '11': '11',
    '12': '12',
    '13': '13',
    '14': '14',
    '15': '15',
    '16': '16',
    '17': '17',
    '18': '18',
    '19': '19',
    '20': '20',
    '21': '21',
    '22': '22',
    '23': '23',
    '24': '24',
    '25': '25',
    '26': '26',
    '27': '27',
    '28': '28',
    '29': '29',
    '30': '30',
    '31': '31',
    '32': '32',
    '33': '33',
    '34': '34',
    '35': '35',
    '36': '36',
    '37': '37',
    '38': '38',
    '39': '39',
    '40': '40',
    '41': '41',
    '42': '42',
    '43': '43',
    '44': '44',
    '45': '45',
    '46': '46',
    '47': '47',
    '48': '48',
    '49': '49',
    '50': '50',
    '51': '51',
    '52': '52',
    '53': '53',
    '54': '54',
    '55': '55',
    '56': '56',
    '57': '57',
    '58': '58',
    '59': '59',
    '60': '60',
    '61': '61',
    '62': '62',
    '63': '63',
    '64': '64',
    '65': '65',
    '66': '66',
    '67': '67',
    '68': '68',
    '69': '69',
    '70': '70',
    '71': '71',
    '72': '72',
    '73': '73',
    '74': '74',
    '75': '75',
    '76': '76',
    '77': '77',
    '78': '78',
    '79': '79',
    '80': '80',
    '81': '81',
    '82': '82',
    '83': '83',
    '84': '84',
    '85': '85',
    '86': '86',
    '87': '87',
    '88': '88',
    '89': '89',
    '90': '90',
    '91': '91',
    '92': '92',
    '93': '93',
    '94': '94',
    '95': '95',
    '96': '96',
    '97': '97',
    '98': '98',
    '99': '99'
}


WIDTH_LOOKUP = {
    "16": 120,
    "24": 201,
    "36": 301
}


COLOR_CODES = {
    "black": "0",
    "red": "1",
    "green": "2",
    "yellow": "3",
    "mix 1": "4",
    "mix 2": "5",
    "mix 3": "6",
    "mix 4": "7",
    "blue": "8",
    "white": "9"
}


FLASH_CODES = {
    "off": "0",
    "on": "1"
}


FONT_CODES = {
    "normal_5": "0",
    "normal_7": "1",
    "normal_9": "8",
    "normal_11": "9",
    "normal_14": "2",
    "normal_15": "3",
    "normal_16": "4",
    "normal_22": "A",
    "normal_24": "B",
    "normal_30": "D",
    "normal_32": "E",
    "normal_40": "F",
    "bold_5": "G",
    "bold_11": "H",
    "bold_14": "5",
    "bold_15": "6",
    "bold_16": "7",
    "bold_22": "C",
    "bold_30": "I",
    "bold_32": "J",
    "bold_40": "K"
}


HORIZONTAL_ALIGNMENT_CODES = {
    "left": "0",
    "center": "1",
    "right": "2"
}


START_MODE_CODES = {
    "fill_scroll": "0a",
    "top_scroll": "\"a",
    "middle_scroll": " a",
    "bottom_scrol": "&a",
    "fill_hold": "0b",
    "top_hold": "\"b",
    "middle_hold": " b",
    "bottom_hold": "0b"
}


SCROLL_SPEED_CODES = {
    "slowest": "\\X15",
    "slow": "\\X16",
    "normal": "\\X17",
    "fast": "\\X18",
    "fastest": "\\X19"
}


IN_OUT_MODE_CODES = in_modes = {
    "scroll": "a",
    "hold": "b",
    "flash": "c",
    "random": "d",
    "move_left": "e",
    "move_right": "f",
    "scroll_out_left": "g",
    "scroll_out_right": "h",
    "move_up": "i",
    "move_down": "j",
    "scroll_out_to_center": "k",
    "unveil_up": "l",
    "unveil_down": "m",
    "unveil_in": "n",
    "unveil_up_in": "o",
    "unveil_up_out": "p",
    "splice_across": "q",
    "splice_vertically": "r",
    "fall_left": "s",
    "fall_right": "t",
    "venetian_horizontal": "u",
    "venetian_vertical": "v",
    "rain": "w",
    "materialize": "x",
    "twinkle": "z",
    "squiggle": "1",
    "radar": "2",
    "fan_open": "3",
    "fan_close": "4",
    "rotate_right": "5",
    "rotate_left": "6",
    "center_to_corner": "7",
    "corner_to_center": "8",
    "center_to_all_sides": "9",
    "all_sides_to_center": "A",
    "four_blocks_to_corners": "B",
    "four_blocks_to_center": "C",
    "four_blocks_out": "D",
    "four_blocks_in": "E",
    "left_top_in": "F",
    "right_top_in": "G",
    "left_bottom_in": "H",
    "right_bottom_in": "I",
    "left_top_diagonal": "J",
    "right_top_diagonal": "K",
    "left_bottom_diagonal": "L",
    "right_bottom_diagonal": "M",
    "left_to_right_down_corner": "N",
    "right_to_left_down_corner": "O",
    "left_to_right_up_corner": "P",
    "right_to_left_up_corner": "Q",
    "grow_up": "R",
}


OPTION_CODES = {
    "foreground_color": {
        "key": "\\X1C",
        "values": COLOR_CODES
    },
    "background_color": {
        "key": "\\X1D",
        "values": COLOR_CODES
    },
    "flash": {
        "key": "\\X07", 
        "values": FLASH_CODES
    },
    "font": {
        "key": "\\X1A",
        "values": FONT_CODES
    },
    "horizontal_alignment": {
        "key": "\\X0A",
        "values": HORIZONTAL_ALIGNMENT_CODES
    },
    "scroll_speed": {
        "key": "no key",
        "values": SCROLL_SPEED_CODES
    },
    "start_mode": {
        "key": "\\X1B",
        "values": START_MODE_CODES
    },
    "in_mode": {
        "key": "\\X1BI",
        "values": IN_OUT_MODE_CODES
    },
    "out_mode": {
        "key": "\\X1BO",
        "values": IN_OUT_MODE_CODES
    }
}


ELEMENT_MODES = [ 
    "format",
    "text",
    "line_feed"
]