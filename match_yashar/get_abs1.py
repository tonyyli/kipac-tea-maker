
import urllib
url = 'http://export.arxiv.org/api/query?search_query=id:+ARXIVNUMBER&start=0&max_results=1'
data = urllib.urlopen(url).read()
print data

