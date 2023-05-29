import requests
import shutil

from config import TARGET_TEXTURE

def save_texture(url, output=MCID_IMAGE_PATH):
    r = requests.get(TARGET_TEXTURE, stream=True)
    if r.status_code == 200:
        with open(output, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

if __name__ == '__main__':
    save_texture(TARGET_TEXTURE)
