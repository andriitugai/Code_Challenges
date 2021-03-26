import string
import random


class Codec:
    prefix = 'http://tinyurl.com/'
    id_size = 6
    symbolset = string.ascii_lowercase + string.digits + string.ascii_uppercase

    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        id = self._create_id()
        self.urls[id] = longUrl

        return self.prefix + id

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        id = shortUrl.split(self.prefix)[1]
        return self.urls[id]

    def _create_id(self):
        while True:
            id = ''.join(random.choices(self.symbolset, k=self.id_size))
            if id not in self.urls.keys():
                break

        return id

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
