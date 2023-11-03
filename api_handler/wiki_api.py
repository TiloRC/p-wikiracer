import wikipediaapi 
import wikipedia

# take in 1 input (str) and return bool as to whether there exists a wiki page for that string
# wiki_object = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
def check(entry, wiki_object):
    page = wiki_object.page(entry)
    return page.exists()

def wikiobject():
    return wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')