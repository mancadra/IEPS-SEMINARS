from bs4 import BeautifulSoup
import zlib
import re
import random
import math

class MinHasher():

    # Picks coefficients for hash functions and saves shingle size.
    def __init__(self, shingle_size = 3, hash_number=250):
        self.shingle_size = shingle_size
        self.hash_functions = []
        self.coef = []
        self.p = 4294967311        # large prime (black magic)
        for _ in range(hash_number):
            a = random.randint(1, 2**16)   
            b = random.randint(0, 2**16)
            self.coef.append((a, b))

    # Computes a hash value of a given html file using the min hash algorithm
    def min_hash(self, html, is_file=False):
        shingles = self.shingle_document(html, is_file=is_file)
        min_hash = []
        for (a, b) in self.coef:
            min = math.inf
            for s in shingles:
                hash = (a * s + b) % self.p
                if hash < min:
                    min = hash
            min_hash.append(str(min))
        return "|".join(min_hash)
    
    # Takes two hash values computed using the min hash algorithm and
    # returns an estimate of their similarity.
    def min_hash_similarity(self, hash1, hash2):
        values1 = hash1.split("|")
        values2 = hash2.split("|")
        n = len(values1)
        c = 0
        for i in range(n):
            if values1[i] == values2[i]:
                c = c + 1
        return c / n
    
    # Computes the Jacard similarity of two html files directly
    # ONLY FOR TESTING
    def jacard_similarity(self, html1, html2, is_file=False):
        shingles1 = set(self.shingle_document(html1, convert_to_int=False, is_file=is_file))
        shingles2 = set(self.shingle_document(html2, convert_to_int=False, is_file=is_file))
        J = len(shingles1.intersection(shingles2)) / len(shingles1.union(shingles2))
        return J

    # Takes an html file, extracts its content using BeautifulSoup and converts it into tokens.
    # Tokens are then used to create shingles of predetermined size which are mapped to integers using crc32.
    def shingle_document(self, html, convert_to_int = True, is_file=False):

        if is_file:     # for testing using local files
            with open(html, "r", encoding="utf-8") as page:
                soup = BeautifulSoup(page, "html.parser")
                page.close()
        else:
            soup = BeautifulSoup(html, "html.parser")

        content = soup.get_text().strip()
        content = re.sub('\s+',' ', content)    # replaces whitespace characters with single spaces

        tokens = content.split(" ")
        tokens = list(filter(lambda x : len(x) > 1, tokens))    # remove stopwords and stray utf-8 characters

        shingles = []
        for i in range(len(tokens) - (self.shingle_size - 1)):
            shingle = ""   
            for j in range(self.shingle_size):
                shingle = shingle + " " + tokens[i + j]
            if convert_to_int:
                shingle = zlib.crc32(shingle.encode('utf-8'))
            shingles.append(shingle)
        return shingles




