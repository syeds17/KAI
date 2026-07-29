from .config import PROJECT_NAME, OWNER_NAME, VERSION
from .banner import show_banner

def startup():
    show_banner(PROJECT_NAME, VERSION, OWNER_NAME)