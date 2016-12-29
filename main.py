#!/usr/local/bin/python3

import threading
import atexit
from queue import Queue 
from spider import Spider
from domain import *
from general import *

HOMEPAGE = input('Enter website homepage (http://www.example.com/index.html): ')
DOMAIN_NAME = get_domain_name(HOMEPAGE)
PROJECT_NAME = get_project_name(DOMAIN_NAME)
print('Using project: \'' + PROJECT_NAME + '\'')
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = int(input('Enter number of threads (program may crash if too many threads requested): '))
thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# check if items in queue, then start crawling
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if(len(queued_links)) > 0:
        print('Remaining links in queue: ' + str(len(queued_links)))
        create_jobs()

# creates job for each queued link
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()

# create worker threads, dies when program exits
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True 
        t.start()

# define work for threads (spider crawling)
def work():
    while True:
        url = thread_queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        thread_queue.task_done()

# displays final message when program finishes 
def exit_handler():
    print('Finished crawling ' + DOMAIN_NAME + '\t...\nResults can be found in /' + PROJECT_NAME + '/crawled.txt')

create_workers()
crawl()
atexit.register(exit_handler)