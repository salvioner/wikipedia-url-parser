# currently supporting wikipedia languages with more that 1M articles:
languages = ["en", "sv", "ceb", "de", "nl", "fr", "ru", "it", "es", "war", "pl", "vi", "ja"]
defaultLang = "en"

def viewlang():
    global languages
    print "Available languages until now are:\n"
    for i in range(len(languages)):
        print languages[i]
    """ FOR FURTHER EDITING: please update the message below when adding new languages """
    print "Currently supporting languages from wikis with more that 1M articles, as found at\nhttps://meta.wikimedia.org/wiki/List_of_Wikipedias#1_000_000.2B_articles"
    print "If you want to contribute, please contact salvioner on GitHub"

def setLanguage(lang):
    try:
        global defaultLang
        lang = lang.lower()
        if (lang not in languages and lang != "default"):
            raise Exception
        else:
            # user can specify
            if(lang == "default"):
                defaultLang = "en"
            else:
                defaultLang = lang

            print "Default language set:", defaultLang

        return
    except Exception as e:
        print "invalid language:", lang

""" TESTED """

def baseWPUrl():
    global defaultLang
    return "https://" + defaultLang + ".wikipedia.org/wiki/"

def specChar(c):
    # checking whether c is a special char and determining its substitute
    if (c == ' '):
        spec = '_'
    elif (c == '\''):
        spec = "%27"
    elif (c == '\"'):
        spec =  "%22"
    elif (c == ','):
        spec = "%2C"
    elif (c == ';'):
        spec = "%3B"
    elif (c == '<'):
        spec = "%3C"
    elif(c == '>'):
        spec = "%3E"
    elif (c == '?'):
        spec = "%3F"
    elif (c == '['):
        spec = "%5B"
    elif (c == ']'):
        spec = "%5D"
    elif (c == '{'):
        spec = "%7B"
    elif (c == '|'):
        spec =  "%7C"
    elif (c == '}'):
        spec = " %7D"
    else:
        # c is not a special char
        spec = c
    return spec

def WParse(st):
    url = ""
    i = 0
    while (i < len(st)):
        # adding c or its special char code to the final url
        url += specChar(st[i])
        i += 1
    return baseWPUrl() + url
