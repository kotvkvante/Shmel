import os

import logging
import re

import numpy as np
import cv2
import cssutils
cssutils.log.setLevel(logging.CRITICAL)

from config import *

# .items-28-1-4
block_id_re = re.compile("(\d+)\-(\d+)")

def get_item_id(item):
    m = block_id_re.match(item[10:])
    if m is None:
        print("Failed to parse item id!")
        exit(-1)

    return (m.group(1), m.group(2))

def read_image(path):
    image = cv2.imread(path)
    return image

def save_image_slice(image, x, y, w, h, output = "cropped.png"):
    crop = image[y:y+h,x:x+w]
    cv2.imwrite(output, crop)
    pass

def main():

    with open(MCID_CSS_PATH, "rb") as f:
        css = f.read()
        # stylesheet = parser.parse_stylesheet_bytes(bstr)

    image = read_image(MCID_IMAGE_PATH)
    sheet = cssutils.parseString(css)

    for rule in sheet:
        if rule.type != rule.STYLE_RULE:
            continue

        n = rule.selectorText
        if ".items" not in n:
            continue

        id = get_item_id(n)

        sp = list(rule.style)
        w = sp[0].value
        h = sp[1].value
        bg = sp[2]

        vv = list(bg.propertyValue)
        x = vv[1].value
        y = vv[2].value

        print("{} => {} {} {} {}".format(id, w, h, x, y))
        save_image_slice(image, abs(int(x)), abs(int(y)), 32, 32, ITEM_OUTPUT_FILENAME.format(id[0], id[1]))




if __name__ == '__main__':
    main()
    # image = read_image("mcid.png")
    # save_image_slice(image, 10, 20, 50, 80)
