''' 
933. Number of Recent Calls


Ítalo Andrade

'''
from typing import List
from collections import deque


class RecentCounter:
    """Class Solution for question.

    Returns:
        None
    """

    def __init__(self):
        self.lista = []

    def ping(self, t: int) -> int:
        self.lista.append(t)
        for i, num in enumerate(self.lista):
            if abs(num-t) < 3000:
                j = len(self.lista)-i
                self.lista = self.lista[i:len(self.lista)]
                return j


class RecentCounter_fast:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


t = 5

obj = RecentCounter_fast()
param_1 = obj.ping(t)
param_1 = obj.ping(t+500)
param_1 = obj.ping(t+4000)
param_1 = obj.ping(t+300)
