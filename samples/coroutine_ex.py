#!/usr/bin/python
# Copyright (c) 2009 Denis Bilenko. See LICENSE for details.
import time
import gevent
from gevent import monkey


"""Spawn multiple workers and wait for them to complete"""

urls = ['https://www.google.com', 'https://www.yandex.ru', 'https://www.python.org', 'https://www.yandex.ru', 'https://www.yandex.ru', 'https://www.yandex.ru', 'https://www.yandex.ru', 'https://www.yandex.ru']

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
import requests


def print_head(url):
    # print('Starting %s' % url)
    data = requests.get(url).content
    print('%s: %s bytes: %r' % (url, len(data), data[:50]))

start = time.time()
jobs = [gevent.spawn(print_head, url) for url in urls]
gevent.joinall(jobs)
print(f"coroutine: {time.time() - start}")

start2 = time.time()
for url in urls:
    # print('Starting %s' % url)
    data = requests.get(url).content
    print('%s: %s bytes: %r' % (url, len(data), data[:50]))
print(f"one-by-one: {time.time() - start2}")
