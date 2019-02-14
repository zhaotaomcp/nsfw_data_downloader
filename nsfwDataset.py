#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import requests

def imageDownload(url, folder):
    file_name = url.split("/")[-1]
    file_path = folder + "\\" + file_name
    if os.path.exists(file_path):
        print(file_path, "is exists, skip")
        return

    print("Downloading %s from %s" % (file_name, url))
    try:
        download_file = requests.get(url)
        status = download_file.status_code
        if status == 200:
            with open(file_path, 'wb') as outfile:
                outfile.write(download_file.content)
        else:
            print("download forbidden!!")
    except:
        print("download fail")

if __name__ == "__main__":
    rootdir = "E:\\nsfw_data_source_urls"
    image_roo_dir = "E:\\nsfw_data_source_urls_images"
    for dirpath, dirnames, filenames in os.walk(rootdir):
        if len(filenames) > 0:
            for filename in filenames:
                suffix = filename.split(".")[-1]
                if suffix != "txt":
                    continue
                path = os.path.join(dirpath, filename)
                with open(path, 'r') as f:
                    lines = f.readlines()
                    for url in lines:
                        imageDownload(url.strip(), dirpath)
