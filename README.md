# SpellingCorrector

The goal of this project is to read a text file consisting of 1000 sentences extracted from new articles, find out the number of incorrect words and to correct them.

1) LOADING:

The text file named “testdata.txt” containing 1000 sentences extracted from new articles is read
first. Each line of the text file contains one sample with three items, including sentence id,
number of errors in the sentence and the sentence. Out of which, 50 instances contain real word
errors.


2) PREPARING DATA:

In this process we removed unwanted characters and extra spaces from the text,
imported a dictionary called “vocab.txt” which is used as dictionary to look up the correct words.


3) BUILDING MODEL:

We are using number of functions ;

● To find out the possibilities of a word.

● Most probable spelling correction for word.

● To generate possible spelling corrections for a word.

● The subsets of words that are there in the dictionary.


4) METHODOLOGY:

● First the program checks for the word that needs to be corrected using a function.

● It stores that word in an index.

● Then it checks for the possible generation of the words for that particular word using the
dictionary.

● Finally, the most likely word will be chosen


Result:

The result after the spelling correction is put in a file called “result.txt” file.
