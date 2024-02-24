from collections import defaultdict as ddict, deque

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = ddict(set)
        self.restnet = ddict(int)
        self.used = [False] * n
        self.INF = float("inf")

    def add_edge(self, u, v, cap):
        #plese tell me what is the meaning of len(self.graph[v]) in the following line
        self.graph[v].add(u)
        self.graph[u].add(v)
        self.restnet[(u, v)] = cap
        self.restnet[(v, u)] = 0
    

    def dfs(self, v, t, f):
        if v == t:
            return f
        self.used[v] = True
        for u in self.graph[v]:
            # v -> u
            cap = self.restnet[(v, u)]
            if not self.used[u] and cap > 0:
                d = self.dfs(u, t, min(f, cap))
                if d > 0:
                    self.restnet[(v, u)] -= d
                    self.restnet[(u, v)] += d
                    return d
        return 0

        
    def ford_fulkerson(self, s, t):
        flow = 0
        while True:
            self.used = [False] * self.n
            f = self.dfs(s, t, self.INF)
            if f == 0:
                return flow
            else:
                flow += f
    
    def bfs(self, s, t):
        used = [False] * self.n
        used[s] = True
        maxflow = [(0, -1)] * self.n
        maxflow[s] = (self.INF, -1)
        q = deque([s])
        while q:
            v = q.popleft()
            for u in self.graph[v]:
                if not used[u] and self.restnet[(v, u)] > 0:
                    used[u] = True
                    f = min(maxflow[v][0], self.restnet[(v, u)])
                    if f > maxflow[u][0]:
                        maxflow[u] = (f, v)
                    q.append(u)
        f = maxflow[t][0]
        if f == 0:
            return 0
        v = t
        while v != s:
            u = maxflow[v][1]
            self.restnet[(u, v)] -= f
            self.restnet[(v, u)] += f
            v = u
        return f
    
    def edmonds_karp(self, s, t):
        flow = 0
        while True:
            f = self.bfs(s, t)
            if f == 0:
                return flow
            else:
                flow += f
    
    def dinic(self, s, t):
        def bfs(s, t):
            level = [-1] * self.n
            level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                for u in self.graph[v]:
                    if self.restnet[(v, u)] > 0 and level[u] == -1:
                        level[u] = level[v] + 1
                        q.append(u)
            self.level = level
            return level[t] != -1
        
        def dfs(v, t, f):
            if v == t:
                return f
            for u in self.graph[v]:
                if self.restnet[(v, u)] > 0 and level[v] < level[u]:
                    d = dfs(u, t, min(f, self.restnet[(v, u)]))
                    if d > 0:
                        self.restnet[(v, u)] -= d
                        self.restnet[(u, v)] += d
                        return d
            return 0
        
        flow = 0
        while bfs(s, t):
            level = [-1] * self.n
            f = dfs(s, t, self.INF)
            while f > 0:
                flow += f
                f = dfs(s, t, self.INF)
        return flow
    
mf = MaxFlow(4)
mf.add_edge(0, 1, 1000)
mf.add_edge(0, 2, 1000)
mf.add_edge(1, 2, 1)
mf.add_edge(1, 3, 1000)
mf.add_edge(2, 3, 1000)
print(mf.ford_fulkerson(0, 3))
mf = MaxFlow(4)
mf.add_edge(0, 1, 1000)
mf.add_edge(0, 2, 1000)
mf.add_edge(1, 2, 1)
mf.add_edge(1, 3, 1000)
mf.add_edge(2, 3, 1000)
print(mf.edmonds_karp(0, 3))
mf = MaxFlow(4)
mf.add_edge(0, 1, 1000)
mf.add_edge(0, 2, 1000)
mf.add_edge(1, 2, 1)
mf.add_edge(1, 3, 1000)
mf.add_edge(2, 3, 1000)
print(mf.dinic(0, 3))

    

