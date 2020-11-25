# !python3

# Define colors and formats for fonts

TEXT_NORMAL         = '\033[0m'
TEXT_BOLD           = '\033[1m'
TEXT_FAINT          = '\033[2m'
TEXT_ITALIC         = '\033[3m'
TEXT_UNDERSCORE     = '\033[4m'
TEXT_BLINK          = '\033[5m'
TEXT_REVERSE        = '\033[7m'
TEXT_CONCEAL        = '\033[8m'

FONT_BLACK      = '\033[30m'
FONT_RED        = '\033[31m'
FONT_GREEN      = '\033[32m'
FONT_YELLOW     = '\033[33m'
FONT_BLUE       = '\033[34m'
FONT_MAGENTA    = '\033[35m'
FONT_CYAN       = '\033[36m'
FONT_WHITE      = '\033[37m'

BACKGROUND_BLACK    = '\033[40m'
BACKGROUND_RED      = '\033[41m'
BACKGROUND_GREEN    = '\033[42m'
BACKGROUND_YELLOW   = '\033[43m'
BACKGROUND_BLUE     = '\033[44m'
BACKGROUND_MAGENTA  = '\033[45m'
BACKGROUND_CYAN     = '\033[46m'
BACKGROUND_WHITE    = '\033[47m'


def print_color(message, color_attr="", endchar="\n"):
    color_end = TEXT_NORMAL
    print(color_attr + message + color_end, end=endchar)
