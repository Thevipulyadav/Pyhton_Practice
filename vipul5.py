#function caching in python

import time
from functools import lru_cache

@lru_cache(maxsize=3)

def some_work(n):
    time.sleep(n)
    return n


if __name__ ==  '  __main__':
    print("Till now working some work")
    some_work(3)
    print("Done ..... calling again")
    some_work(3)
    print("call in again")

