#!/usr/local/bin/python3
import os

# each website crawled creates a new folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating new project: ' + directory)
        os.mkdir(directory)
    else:
        print('Project already exists... continuing...')
    
# queue for new files and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#used to convert domain name to project name
def get_project_name(domain_name):
    split = domain_name.split('.')
    return split[0]

# used to make new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# adds data to existing files
def add_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete data from file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# read file and convert to set
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# convert set to file as new line
def set_to_file(sets_list, file):
    with open(file, 'w') as f:
        for l in sorted(sets_list):
            f.write(l + '\n')