# -*- coding: utf-8 -*-
import heapq


class DinnerPlates:
    def __init__(self, capacity):
        self.stack = []
        self.que = []
        self.capacity = capacity
    def push(self, val):
        i = self._get()
        if i != -1:
            self.stack[i].append(val)
        else:
            if not self.stack or len(self.stack[-1]) == self.capacity:
                self.stack.append([])
            self.stack[-1].append(val)
    def pop(self):
        if self.stack:
            if self.stack[-1]:
                v = self.stack[-1].pop()
                if self.stack and not self.stack[-1]:
                    self.stack.pop()
                return v
        return -1
    def popAtStack(self, index):
        if index >= len(self.stack) or not self.stack[index]:
            return -1
        v = self.stack[index].pop()
        heapq.heappush(self.que, index)
        return v
    
    def _get(self):
        if self.que:
            i = heapq.heappop(self.que)
            if i < len(self.stack) and len(self.stack[i]) < self.capacity:
                return i
        return -1