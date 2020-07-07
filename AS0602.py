# Name = Monish Manjunath
# Date = 02/15/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/anl8iR3LmSI "





from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen
import re                                           
from collections import OrderedDict

visited = set()                                                # Stores the link which have been visited
depth = 0                                                      # Variable to count the number of web pages visited
wordDict = {}                                                  # Dictinory to store the word as key and count as value

def webCrawl(url):
    """ This fucntion crawls through the list of links by recursivelly calling itself """

    global visited
    visited.add(url)

    global depth 
    depth = depth + 1

    links = analyze(url)                                        # Calling analyze function

    for link in links:
        if (link[:26] == "https://www.cdm.depaul.edu"):         # Restricting the crawl to only depaul web pages
            if depth <= 10:                                    # Setting the number of web pages  to be crawled
                if link not in visited:                         # Checking if the link is not in the set of visitied set of links
                    try:                
                        webCrawl(link)
                    except:
                        pass
       
    


def analyze(url):
    """ This function returns the list of urls and also reads the data content of the web pages """
    
    print("\n  Visting ", url)
   
    

    pageContent = urlopen(url)                                                          # Opening the url   
    pageContent = pageContent.read()                                                    # reading the page content 
    pageContent = pageContent.decode()                                                  # Decoding the page cotent to string

    collector = Collector(url)                                                          # Creating a object for collector class 
    collector.feed(pageContent)
    listOfUrls = collector.getLinks()                                                   # Calling get links function of collector class 

    pageContent = remove_between(pageContent, "<script>", "</script>")                  # Removing the js code written between the script tag
    pageContent= remove_between(pageContent, "<style>", "</style>")                     # Removing the css code written between the style tag
    pageContent = remove_between(pageContent, "<", ">")                                 # Removing all the tags
    words = re.sub("[^\w]", " ",  pageContent).split()                                  # Removing the escape characters from the page data
    
    

    for word in words:                                                                  # Looping through the words and adding them to dictionary with count value
        if word in wordDict:                                            
            wordCount = wordDict.get(word)
            wordDict[word] = wordCount + 1
        else:
            wordDict[word]= 1

    return listOfUrls




class Collector(HTMLParser):
    """ This class extends the inbuilt HTMLParser class; It checks for the anchor tag and returns the urls in the web page """

    def __init__(self, url):
        HTMLParser.__init__(self)                                       # Constructor class for the collector class

        self.url = url
        self.links = [ ]

    def  handle_starttag(self, tag, attrs):
        """ converts the relative paths into absoulte path and appends the link to the list of links """
        if tag == 'a':                                                  # Checking if is an anchor tag
            for attr in attrs:
                if attr[0] == 'href':                                   # Indexing the href atribute in the anchor tag
                    absolutePath = urljoin(self.url , attr[1])          
                    if absolutePath[ : 4] == 'http':
                        self.links.append(absolutePath)
        

    def getLinks(self):
        return self.links




def remove_between(document, start_str, end_str):
    """ This function ignores the contents between start and end tag and returns the data in the source code"""

    while start_str in document and end_str in document:
        start_str_index = document.find(start_str)
        end_str_index = document.find(end_str, start_str_index) + len(end_str) - 1
        document = document[0 : start_str_index] + document[end_str_index + 1 : len(document)]
    return document



def main():
    """This  fucntion calls the crawler function and prints the words with the highest count  """

    x = 0 
    url = "https://www.cdm.depaul.edu/Pages/default.aspx"
    webCrawl(url)

    OD= OrderedDict(sorted(wordDict.items(), key=lambda x: x[1], reverse = True))         # Soritng the dictionary wrt to values
    
    print("Top 25 words \n")
    print('{:20} {:10} '.format("Word", "Count \n"))                           
    
    for ele in OD:    
        print("{:20} {:10} ". format(ele ,str(OD[ele])))
        x = x + 1
        if x == 25:                                         # Printing only the top 25 words
            break


main()














