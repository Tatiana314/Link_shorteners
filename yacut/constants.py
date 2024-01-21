from string import ascii_letters, digits

MAX_LEN_ORIGINAL_LINK = 2000
MAX_LEN_SHORT = 16
LEN_SHORT = 6
ITERATIONS = 100

SHORT_LINK_SIMBOLS = ascii_letters + digits
REGEX = f'^[{SHORT_LINK_SIMBOLS}]+$'

ORIGINAL_LINK_VIEW = 'original_link_view'
