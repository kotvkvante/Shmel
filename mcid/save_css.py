import requests

from config import *

import main as mn

if __name__ == '__main__':
    s = mn.prepare_session()
    h = mn.prepare_html(s, TARGET_CSS)

    print(type(h))
    print(h)
    with open("mcid.css", "wb") as f:
        f.write(h)
