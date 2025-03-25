from queue import PriorityQueue
from threading import Lock

class Frontier():

    def __init__(self, seed_url):
        self.frontier = PriorityQueue()
        self.frontier_lock = Lock()
        self.visited = set()
        self.hashes = dict()
        self.frontier.put((0, seed_url, 0))
        self.visited.add(seed_url)

    def get(self):
        priority, link, from_page = self.frontier.get()
        with open("crawled_log.txt", "a") as file:
            file.write(link + "\n")
        return (priority, link, from_page)

    def put(self, links):
        already_visited = []

        with self.frontier_lock:
            for l in links:
                (priority, url, from_page) = l
                n = len(self.visited)
                self.visited.add(url)
                if len(self.visited) == n:
                    already_visited.append(url)
                else:
                    with open("visited_log.txt", "a") as file:
                        file.write(url + "\n")
                    if priority == 0:
                        self.frontier.put(l)
                        with open("frontier_log.txt", "a") as file:
                            file.write(f"({priority}, {url}, {from_page})\n")
        return already_visited
    
    def add_hash(self, url, hash):
        with self.frontier_lock:
            self.hashes[url] = hash
            with open("hash_log.txt", "a") as file:
                file.write(url + " : " + hash + "\n")

    def add_visited(self, link):
        with self.frontier_lock:
            self.visited.add(link)
            with open("visited_log.txt", "a") as file:
                file.write(link + "\n")

    def restart(self):
        with open("visited_log.txt", "r") as file:
            self.visited = set(file.read().split("\n"))

        with open("hash_log.txt", "r") as file:
            read_lines = file.read().split("\n")
            for l in read_lines:
                pair = l.split(" : ")
                if len(pair) == 2:
                    self.hashes[pair[0]] = pair[1]

        with open("crawled_log.txt", "r") as file:
            crawled = file.read().split("\n")
            seed_url = crawled[0]
            crawled = set(crawled)

        with open("frontier_log.txt", "r") as file:
            lines = file.read().split("\n")
            lines.remove('')
            lines = list(map(lambda x : x.split(", "), lines))
            for l in lines:
                if not l[1] in crawled:
                    self.frontier.put((int(l[0][1:]), l[1], int(l[2][:-1])))
        
        return seed_url
        
            
