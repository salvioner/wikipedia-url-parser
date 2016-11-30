from wikiparser import wp
# adding more features: save your file in folder ./wikiparser and add the new file's name at the end of the import
# e.g.: after adding ./wikiparser/foo.py, the first line of this page shall look like this:
# from wikiparser import wp, foo

# currently supporting wikipedia languages with more that 1M articles:
languages = ["en", "sv", "ceb", "de", "nl", "fr", "ru", "it", "es", "war", "pl", "vi", "ja"]
defaultLang = "en"

wp.viewlang()
