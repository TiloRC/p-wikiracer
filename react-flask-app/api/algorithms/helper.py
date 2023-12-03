"""
File with a bunch of miscellaneous helper functions.
If this gets big enough, maybe the functions should be
moved to other files.
"""

import requests
import wikipediaapi
from typing import List

from sentence_transformers import SentenceTransformer, util

# Download model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  

class FailedPath(Exception):
    """
    Raised when a WikiRacer fails to find a path between the
    destination and start page.

    Note that if a WikiRacer fails to find a path because of
    an issue with an api call, that should *not* be considered
    a FailedPath exception.
    """
    pass

class PageRequestError(Exception):
    pass

class PathDeadend(FailedPath):
    """
    Raised when there are no pages left to visit.
    """
    pass


def get_random_page():
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,  # Retrieve pages only from the main namespace (articles)
    }

    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        raise PageRequestError(f"Status code {response.status_code}")

    data = response.json()
    random_page_title = data["query"]["random"][0]["title"]

    return random_page_title

def is_valid_path(path: List[str]):
    """
    Checks if each page in path is linked from
    the previous page.
    """
    pass

def get_first_linked_page(page):
    """
    Returns the first linked page on `page`.

    See https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy.
    """

def get_linked_pages(page):
    """
    returns the title of all the linked pages of a wikipedia page
    """
    links = page.links
    linked_pages = []
    for title in sorted(links.keys()):
        linked_pages.append(title)
    # api_url = "https://en.wikipedia.org/w/api.php"

    # params = {
    # 'action': 'parse',
    # 'page': page,
    # 'format': 'json'
    # }

    # response = requests.get(api_url, params=params)
    # data = response.json()
    # # print(type(data['parse']['links']))

    # res = []
    # #res.append(page)

    # for row in data['parse']['links']:
    #     res.append(row['*'])

    return linked_pages

def get_cos_sim(links, target_page):
    # target_embed = model.encode(getLinkedPages(target_page))
    highest_sim = ("", -1)
    encoded_target = model.encode(target_page)

    for ind in range(len(links)):
        encoded_link = model.encode(links[ind])
        sim = util.cos_sim(encoded_link, encoded_target)
        sim_val = sim[0][0].item()
        if sim_val > highest_sim[1]:
            highest_sim = (links[ind], sim_val)
    return highest_sim[0]
    # return type(sim_list[1][1][0][0].item())

# wiki_wiki = wikipediaapi.Wikipedia('Aldo & Rich', 'en')
# page_py = wiki_wiki.page('Colorado River (Texas)')
# print (get_linked_pages(page_py))
# print(get_cos_sim(links, "Colorado River"))
