# wikipedia-url-parser

WikiParser - v0.1

A collection of Python tools to turn a string into a wikipedia URL.

Supports all major wikipedia languages, i.e. languages from wikipedias
with more than 1 million articles, as can be found at
https://meta.wikimedia.org/wiki/List_of_Wikipedias#1_000_000.2B_articles

If you want to contribute, by adding more languages or adding reversing features (URL to string), please contact salvioner on GitHub or on Telegram

*** ADDING LANGUAGES***
	* Create a new branch
	* Open file wp.py
	* Open following URL: https://meta.wikimedia.org/wiki/List_of_Wikipedias#1_000_000.2B_articles
	* Add language prefixes as strings to the list "languages"
 
 *** ADDING FEATURES ***
	* Create a new branch
	* Either open file wp.py or create new file
	* Once you are done, save your file in folder "wikiparser";
	* IF YOU WROTE YOUR CODE ON A FILE DIFFERENT FROM wp.py:
		1) please give your file a short name; this makes using this package easier, because every time a function is called you need to type "filename.function()"
		2) append the new file's name without ".py" to the import command in the first line of main.py.
		
		e.g.	after adding my new file "foo.py" in wikiparser folder, i open "main.py" and edit the first line.
				So, that line will contain:			from wikiparser import wp, foo
