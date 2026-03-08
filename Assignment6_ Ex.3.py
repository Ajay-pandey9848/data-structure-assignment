# CHAPTER 6 EXERCISE 3
'''
URL Shortener Simulator Exercise

Create a mini URL shortener like a simplified TinyURL.

Requirements

- A long URL should get a short code (for example: "a1b2c3")
- If the same URL is shortened again, return the same code
- If a collision happens (same code for different URL), resolve it
- Be able to:
    - shorten a URL
    - retrieve the original URL from a short code
    - track how many times a short code was used

Hint!
Use hashlib (built-in Python module)
Store:
    code -> url
    url -> code
    code -> click_count

'''


# Here's a base where you can start! Implement the TODO's

import hashlib

class URLShortener:
    """
    Mini URL shortener.

    Store:
    - code_to_url   : short_code -> long_url
    - url_to_code   : long_url -> short_code
    - click_counts  : short_code -> int

    Collision rule:
    - If generated code already exists for another URL,
      generate a new one using an extra value (counter).
    """

    def __init__(self):
        # TODO: initialize dictionaries
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        """
        Create a short code using hashing.

        HINT 1 (recommended):
            import hashlib
            digest = hashlib.md5((url + extra).encode()).hexdigest()
            return digest[:6]

        HINT 2 (simpler beginner option):
            Use Python's built-in hash(), but note:
            hash() values can differ between runs.
        """
        # TODO: implement code generation
        digest = hashlib.md5((url + extra).encode()).hexdigest()

        return digest[:6]

    def shorten(self, url):
        """
        Return a short code for the URL.

        Rules:
        - If URL already shortened, return existing code
        - Otherwise generate code
        - Resolve collisions if code belongs to a different URL
        - Save mappings + click count = 0
        """
        # TODO: implement
        if url in self.url_to_code:
            return self.url_to_code[url]
        else:
            code = self._make_code(url)
            counter = 0
            while True:
                if code not in self.code_to_url:
                    break
                elif code in self.code_to_url and self.code_to_url[code] == url:
                    break
                else:
                    counter += 1
                    code = self._make_code(url,str(counter))
                    

            self.url_to_code[url] =  code
            self.code_to_url[code] = url
            self.click_counts[code] = 0
            return code

    def open_url(self, code):
        """
        Return original URL and increase click count.
        Return None if code not found.
        """
        # TODO: implement
        if code in self.code_to_url:
            url = self.code_to_url[code]
            self.click_counts[code] +=1
            return url
        else:
            return None

    def get_stats(self, code):
        """
        Return a dictionary with:
        { "code": ..., "url": ..., "clicks": ... }

        Return None if code not found.
        """
        # TODO: implement
        if code in self.code_to_url:
            return {"code" : code , "url" : self.code_to_url[code] ,"clicks" : self.click_counts[code]}
        else:
            return None




# FOR TESTING:

shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"  # same as url1

# TODO: Uncomment after implementing methods
code1 = shortener.shorten(url1)
code2 = shortener.shorten(url2)
code3 = shortener.shorten(url3)
print("Codes:", code1, code2, code3)  # code1 and code3 should match
print("Open code1:", shortener.open_url(code1))
print("Open code1 again:", shortener.open_url(code1))
print("Stats code1:", shortener.get_stats(code1))