# WebCrawler
* Python application that crawls a website for urls
* uses urllib and link_finder to parse html from a url and saves newly found urls into crawled.txt
* multi-threaded approach by using sets in Python
* program is able to be interrupted and resumed at any time. threads save sets to a .txt file after parsing one url. all threads have access to queue.txt and crawled.txt (input/output)
* user inputs a url (http://example.com/), program creates a project folder which is the domain name (example), user is able to set desired number of threads, saves urls to be checked in queue.txt and outputs urls found into crawled.txt
* sub-domains will fall into same project folder as main domain. eg: http://test.example.com/ falls into project folder example, but still crawls all links available from http://test.example.com/
* outputs exit string when all links have been crawled
* currently, IP addresses can be accepted as a url however the project name will be created with the first few digits of the IP
