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
        return self.frontier.get()

    def put(self, links):
        already_visited = []

        with self.frontier_lock:
            for l in links:
                (priority, url, _) = l
                n = len(self.visited)
                self.visited.add(url)
                if len(self.visited) == n:
                    already_visited.append(url)
                else:
                    if priority == 0:
                        self.frontier.put(l)
                    #print(self.frontier.queue)
            #print(self.visited)
        return already_visited
    
    def add_hash(self, url, hash):
        self.hashes[url] = hash

    def add_visited(self, link):
        with self.frontier_lock:
            self.visited.add(link)

        
            
