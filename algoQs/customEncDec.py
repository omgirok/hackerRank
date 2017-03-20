import string
import random
class Codec:
    # alphabet to choose from
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            print "the code we generated is:",code

        if code not in self.code2url:
            self.code2url[code] = longUrl
            self.url2code[longUrl] = code

        return "http://www.tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # use the last 6 characters of the tinyUrl to reverse lookup into the code
        print "looking up long url of shortened code:",shortUrl

        return self.code2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
url = "https://poloniex.com/balances"
codec = Codec()
url2 = "https://leetcode.com/problems/encode-and-decode-tinyurl/#/solutions"

print codec.decode(codec.encode(url))
print ""
print codec.decode(codec.encode(url2))