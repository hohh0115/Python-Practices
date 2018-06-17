# -*- coding: utf-8 -*-
"""
從命令列啟動
"""

import os
import sys
import time
import requests
from bs4 import BeautifulSoup

# which? 4chan or komica?
# which = 'komica'

# target URL
# tar_url = 'https://rem.komica2.net/00/pixmicat.php?res=10932098'

# maximum file size (MB)
max_file_size = '4.5'

# save directory, any better way?
folder = 'D:\craw_back_files\\'

# files that exceed maximum file size
too_big_files = []

# forbidden characters as a folder name
folder_forbidden_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

def string_to_number(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def list_to_string(list):
    str = ''.join(list)
    return str

def time_string():
    return str(time.strftime("%y%m%d%H%M%S"))

# any better way?
def check_folder_forbidden_chars(name):
    for char in folder_forbidden_chars:
        if char in name:
            name = name.replace(char, '')

    return name

def open_dir(thread_title):
    thread_title = check_folder_forbidden_chars(thread_title)
    try:
        path = folder + time_string() + ' ' + thread_title
        if not os.path.exists(path):
            os.makedirs(path)
            return path
    except Exception as e:
        print("e")

def bytesto(bytes, to, bsize=1024):
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize

    return(r)

def download_file(req_obj, save_path):
    file_name = req_obj.url
    last_char = file_name[::-1].find("/")
    file_name = file_name[len(file_name) - last_char:]
    save_path_file_name = save_path + "\\" + str(file_name)
    with open(save_path_file_name, 'wb') as fh:
        fh.write(req_obj._content)

    # file_name http://i.4cdn.org/c/1517542471418.jpg
    # file_name[::-1] # gpj.8141742457151/c/gro.ndc4.i//:ptth
    # last_char = gpj
    # last_char = jpg

def check_file_size(req_obj):
    req_file_size = bytesto(req_obj.headers['Content-Length'], 'm')
    if req_file_size > max_file_size:
        return False
    return True

def get_started(tar_url):

    if '4chan' in tar_url:
        thread_title_class = 'subject'
        file_href_class = 'fileThumb'
    elif 'komica' in tar_url:
        thread_title_class = 'title'
        file_href_class = 'file-thumb'
    else:
        print("Error: Can't recognize the url!")
        raise SystemExit

    # get page context
    html = requests.get(tar_url)
    soup = BeautifulSoup(html.text, 'lxml')  # get BeautifulSoup object
    # pprint(soup.prettify())
    thread_title = list_to_string(soup.find_all('span', class_=thread_title_class)[0].contents)
    if not thread_title:
        thread_title = 'No Title'
    save_path = open_dir(thread_title)

    print("Sending request for", tar_url)
    print("Save path is", save_path)

    all_files = soup.find_all('a', class_=file_href_class)
    files_count = len(all_files)
    too_big_files_count = 0

    for i in all_files:
        file_index = all_files.index(i) + 1
        print('Downloading', i['href'], '(', file_index, ' / ', files_count  ,')')
        try:
            i_url = 'https:' + i['href']
        except:
            print("This file couldn't be downloaded")
            continue
        req = requests.get(i_url)  # req.url = url
        result = check_file_size(req)
        if result:
            download_file(req, save_path)
        else:
            print('File No.', file_index, 'exceeds maximum file size')
            too_big_files_count += 1
            too_big_files.append(i_url)

    print('Download complete!')
    print (too_big_files_count,' files exceed maximum file size:', '\n '.join(too_big_files))




# let's start
max_file_size = string_to_number(max_file_size)
if len(sys.argv) > 1:
    if len(sys.argv) == 2:
        get_started(sys.argv[1])
    else:
        print("Error: unnecessary argument!")
elif len(sys.argv) == 1:
    print("Error: paste the url!")
