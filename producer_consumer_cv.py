#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'ProducerConsumer using condition, fixed-sized queue'

from threading import Thread, Lock, Condition
import time
import random

MAX_CAP = 10
que = []
condition = Condition()


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global que
        while True:
            condition.acquire()
            if len(que) == MAX_CAP:
                print("Queue full")
                condition.wait()
                print("Producer continue...")
            num = random.choice(nums)           
            que.append(num)
            print("Produced", num)
            condition.notify()
            condition.release()
            time.sleep(random.random()*2)


class ConsumerThread(Thread):
    def run(self):
        global que
        while True:
            condition.acquire()
            while not que:
                print("Nothing in que")
                condition.wait()
                print("Consumer continue...")
            num = que.pop(0)
            print("Consumed", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


if __name__ == '__main__':
    ProducerThread().start()
    ConsumerThread().start()