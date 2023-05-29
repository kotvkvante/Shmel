import logging
import re

import cssutils
cssutils.log.setLevel(logging.CRITICAL)

# .items-28-1-4
block_id_re = re.compile("(\d+)\-(\d+)")

def get_item_id(item):
    m = block_id_re.match(n[10:])
    if m is None:
        print("Failed to parse item id!")
        exit(-1)

    return (m.group(1), m.group(2))



with open("mcid.css", "rb") as f:
    css = f.read()
    # stylesheet = parser.parse_stylesheet_bytes(bstr)

sheet = cssutils.parseString(css)

i = 0
for rule in sheet:
    if rule.type != rule.STYLE_RULE:
        continue

    n = rule.selectorText
    if ".items" not in n:
        continue

    id = get_item_id(n)
    # print(type(rule))
    # print(list(rule.selectorList))

    sp = list(rule.style)
    w = sp[0].value
    h = sp[1].value
    bg = sp[2]

    vv = list(bg.propertyValue)
    x = vv[1].value
    y = vv[2].value

    print("{} => {} {} {} {}".format(id, w, h, x, y))
    # print(w.name, w.value)
    # print(h.name, h.value)
    # print(x.type, x.value)
    # print(y.type, y.value)

    i+=1
    if (i > 10): break
    # for property in rule.style:
    #     n = property.name
        # if len(n) < 2:


    #     if property.name == 'color':
    # if rule.type == rule.STYLE_RULE:
        # find property

        # print()
        # for property in rule.style:
        #     if property.name == 'color':
        #         property.value = 'green'
        #         property.priority = 'IMPORTANT'
        #         break
        # or simply:
        # rule.style['margin'] = '01.0eM' # or: ('1em', 'important')

# sheet.encoding = 'ascii'
# sheet.namespaces['xhtml'] = 'http://www.w3.org/1999/xhtml'
# sheet.namespaces['atom'] = 'http://www.w3.org/2005/Atom'
# sheet.add('atom|title {color: #000000 !important}')
# sheet.add('@import "sheets/import.css";')
#
# # cssutils.ser.prefs.resolveVariables == True since 0.9.7b2
# print sheet.cssText


# import tinycss
#
# parser = tinycss.make_parser()
#
#
# print(stylesheet)
# print(stylesheet.errors)
#
# # print(help(stylesheet.rules[375]))
# # print(stylesheet.rules[375])
#
# # print(help(stylesheet.rules[375]))
#
# for r in stylesheet.rules:
#     s = r.selector.as_css()
#     # if s[0] != ".":
#     #     continue
#     if len(s) < 2:
#         continue
#     if s[1] != "i":
#         continue
#     print(s)
