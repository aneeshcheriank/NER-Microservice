"""
The module is to extact content from wikipedia and to supply to the ner module to extract entities.
"""

import wikipedia

def get_wiki_content(page):
    """
    Exract content of a given page
    input: page (string)
    output: content(string)
    """
    try:
        content = wikipedia.page(page).content
    except:
        content = "No content found"

    return content

def get_wiki_suggetion(query):
    """
    Get wiki page based on the query
    input: query(string)
    output: page(string)
    """

    page = wikipedia.suggest(query)

    if page is None:
        search = wikipedia.search(query)

        if len(search) > 0:
            page = search[0]
    
    return page

def search_wiki(query):
    """
    Search wikipedia based on some information
    return the page of the most relevant information if found
    input: query(string)
    output: page(string) parsed page
    """
    page = get_wiki_suggetion(query)
    if page is not None:
        return get_wiki_content(page)
    return "No content found"

if __name__ == "__main__":
    print(search_wiki("Barak Obama"))