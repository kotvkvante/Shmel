import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

from config import *

# URL of the web page you want to extract

def prepare_session():
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = DEFAULT_USER_AGENT

    return session

def prepare_html(session, url):
    # get the HTML content
    html = session.get(url).content

    # parse HTML using beautiful soup
    return html

def get_css_urls(soup):
    # get the CSS files
    css_files = []

    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = urljoin(URL, css.attrs.get("href"))
            css_files.append(css_url)

    print("Total CSS files in the page:", len(css_files))
    return css_files

def save_css_urls(css_files, default_filename=DEFAULT_CSS_FILENAME):
    with open(default_filename, "w") as f:
        for css_file in css_files:
            print(css_file, file=f)

def main():
    s = prepare_session()
    h = prepare_html(s, URL)
    soup = bs(h, "html.parser")
    c = get_css_urls(soup)
    save_css_urls(c)

    return 0;

if __name__ == '__main__':
    main()
