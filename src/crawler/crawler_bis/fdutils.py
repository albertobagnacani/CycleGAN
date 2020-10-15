import multiprocessing
import os
import time
import urllib3
import urllib.request
from urllib.error import URLError, HTTPError


def string_or_path(string_or_file):
    if os.path.isfile(string_or_file):
        ret = open(string_or_file, 'r').read()
    else:
        ret = string_or_file
    return ret

def web_downloader_mp(link_list, download_path, save_filename_prefix, save_filename_postfix, forced_extension, start, end, i):
    link_list = link_list[start:end]

    for k in range(len(link_list)):
        if forced_extension is not None:
            extension = forced_extension
        else:
            extension = os.path.splitext(link_list[k])[1].lower()
        output_file = os.path.join(download_path, save_filename_prefix + save_filename_postfix + str(i*1000+k)
                                   + extension)

        response = urllib.request.urlretrieve(link_list[k], output_file)

        print("completed by {}, {}/{}".format(i, k, len(link_list)))

def web_downloader(link_list, download_path, k=0, save_filename_prefix="", save_filename_postfix="_", forced_extension=None,
                   verbose=False, ignore_errors=False):
    # type: (list(str), str, str, str, bool, bool) -> None

    client_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}

    if download_path != "" and not os.path.isdir(download_path):
        os.mkdir(download_path)

    processes = multiprocessing.cpu_count()
    chunk = len(link_list) // processes
    inputs = []
    for i in range(processes):
        inputs.append((link_list, download_path, save_filename_prefix, save_filename_postfix, forced_extension, (i * chunk), ((i + 1) * chunk), i))

    with multiprocessing.Pool(processes) as p:
        p.starmap(web_downloader_mp, inputs)

    if verbose:
        print("\nAll are downloaded")

    return 0


import re


def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)