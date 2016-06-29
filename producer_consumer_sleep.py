#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Producer Consumer Pattern: using sleep'


from threading import Thread, Lock
import time
import random

que = []
lock = Lock()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global que
        while True:
            num = random.choice(nums)
            lock.acquire()
            que.append(num)
            print("Produced", num)
            lock.release()
            time.sleep(random.random()*2)


class ConsumerThread(Thread):
    def run(self):
        global que
        while True:
            while not que:
                print("Nothing in que")
                time.sleep(random.random())
            lock.acquire()
            num = que.pop(0)
            print("Consumed", num)
            lock.release()
            time.sleep(random.random())


if __name__ == '__main__':
    ProducerThread().start()
    ConsumerThread().start()