from queue import PriorityQueue
from threading import Lock

class Frontier():

    def __init__(self, seed_url):
        self.frontier = PriorityQueue()
        self.frontier_lock = Lock()
        self.seen = set()
        self.hashes = dict()
        self.crawled = set()
        self.frontier.put((0, seed_url))
        self.seen.add(seed_url)
        self.crawled.add(seed_url)

    def get(self):
        priority, link = self.frontier.get()
        with open("crawled_log.txt", "a") as file:
            file.write(link + "\n")
        self.crawled.add(link)
        return (priority, link)

    def put(self, links):
        already_visited = []

        with self.frontier_lock:
            for l in links:
                (priority, url) = l
                n = len(self.seen)
                self.seen.add(url)
                if len(self.seen) == n:
                    already_visited.append(url)
                else:
                    with open("seen_log.txt", "a") as file:
                        file.write(url + "\n")
                    if priority == 0:
                        self.frontier.put(l)
                        with open("frontier_log.txt", "a") as file:
                            file.write(f"({priority}, {url})\n")
        return already_visited
    
    def add_hash(self, url, hash):
        with self.frontier_lock:
            self.hashes[url] = hash
            with open("hash_log.txt", "a") as file:
                file.write(url + " : " + hash + "\n")

    def add_seen(self, link):
        with self.frontier_lock:
            self.seen.add(link)
            with open("seen_log.txt", "a") as file:
                file.write(link + "\n")

    def restart(self):
        with open("seen_log.txt", "r") as file:
            self.seen = set(file.read().split("\n"))

        with open("hash_log.txt", "r") as file:
            read_lines = file.read().split("\n")
            for l in read_lines:
                pair = l.split(" : ")
                if len(pair) == 2:
                    self.hashes[pair[0]] = pair[1]

        with open("crawled_log.txt", "r") as file:
            crawled = file.read().split("\n")
            seed_url = crawled[0]
            self.crawled = set(crawled)

        with open("frontier_log.txt", "r") as file:
            lines = file.read().split("\n")
            lines.remove('')
            lines = list(map(lambda x : x.split(", "), lines))
            for l in lines:
                if not l[1] in crawled:
                    self.frontier.put((int(l[0][1:]), int(l[1][:-1])))
        
        return seed_url
        
            
