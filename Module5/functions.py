# __name__ special variable that tells us if a module is ran as a script or imported 
# into another module
from urllib.request import urlopen
import sys


# the def keywor just binds a code to a string, ie the name of the method to its code
def fetch_words(url):
    """This is a docstring for this method"""
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    print(story_words)


print(__name__)
# this will print "functions" when imported into another module
# if this is ran as a script it will write "__main__"


def main(url):
    fetch_words(url)


if __name__ == '__main__':
    fetch_words(sys.argv[1])
# now we can import it without any consequences and run as a script


# a way to import multiple methods from a module:
#from functions import (method1, method2)

#run with:
# python .\functions.py http://sixty-north.com/c/t.txt