import urllib.request, urllib.error, urllib.parse
import obo
from collections import Counter
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
print(text)
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)

#adding in Counter object
word_count = Counter(wordlist)
print(f"Amount of unique words: {len(word_count)}")
for word, count in word_count:
    print(f"{word}: {count}")


dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
