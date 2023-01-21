import random
import urllib.request
import urllib.parse
import requests

class word_finder:
    def __init__ (self, url, response):
        """wf = word_finder('https://www.mit.edu/~ecprice/wordlist.10000')
        """
        get_list = response
        string_of_words = response.content.decode('utf-8')
        list_of_words = string_of_words.splitlines()
        words = list_of_words
        print(f"{len(self.words)} words read")

    def random(self, words):
        random_word = random.choice(words)
        print(random_word)
