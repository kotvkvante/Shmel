from os import path

URL = "https://minecraft-ids.grahamedgecombe.com/"
DEFAULT_USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

STATIC_FOLDER = "static"
ITEMS_FOLDER = "items"

MCID_IMAGE_PATH = path.join(STATIC_FOLDER, "mcid.png")
MCID_CSS_PATH = path.join(STATIC_FOLDER, "mcid.css")
DEFAULT_CSS_FILENAME = path.join(STATIC_FOLDER, "css_files.txt")
ITEM_OUTPUT_FILENAME   = path.join(ITEMS_FOLDER,  "{}_{}.png")



TARGET_CSS = "https://minecraft-ids.grahamedgecombe.com/stylesheets/bundles/all/1644090399.css"
TARGET_TEXTURE = "https://minecraft-ids.grahamedgecombe.com/images/sprites/items-28.png"
