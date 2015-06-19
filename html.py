import re
import urllib2
baseURL = 'https://www.google.com'
url = "https://www.google.com/search?q=test+"
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
con = urllib2.urlopen(req).read()

searchObj = re.search( r'<a class="q qs" href="([^"]*)">Images</a>', con)

imgHash = searchObj.group(1)

imgHash = imgHash.replace('&amp;', '&')

imageURL = baseURL + imgHash

print imageURL
