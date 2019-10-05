# -*- coding: utf-8 -*-

def string_freq(queries, words):
    queries_count = [s.count(min(s)) for s in queries]
    word_count = [w.count(min(w)) for w in words]
    answer = [sum(q < w for w in word_count) for q in queries_count]
    
    return answer
