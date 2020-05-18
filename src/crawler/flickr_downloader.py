import csv
import requests
import os
import sys
import time

from flickrapi import FlickrAPI
import pandas as pd


def get_urls(image_tag, key, secret, max_count, output):
    flickr = FlickrAPI(key, secret)

    photos = flickr.walk(text=image_tag,
                         tag_mode='all',
                         tags=image_tag,
                         extras='url_o',
                         per_page=500,
                         sort='relevance')
    count = 0
    urls = []

    for photo in photos:
        if count < max_count:
            count += 1
            print("Fetching url for image number {}".format(count))

            try:
                url = photo.get('url_o')
                urls.append(url)
            except:
                print("Url for image number {} could not be fetched".format(count))
        else:
            print("Done fetching urls, fetched {} urls out of {}".format(len(urls), max_count))
            break

    urls = pd.Series(urls)

    print("Writing out the urls in the current directory")
    urls.to_csv(output)
    print("Done")


def put_images(fn, output):
    urls = []

    with open(fn, newline="") as csvfile:
        doc = csv.reader(csvfile, delimiter=",")

        for row in doc:
            if row[1].startswith("https"):
                urls.append(row[1])

    t0 = time.time()
    count = 0
    for url in enumerate(urls):
        try:
            resp = requests.get(url[1], stream=True)
            name = str(count) + ".jpg"
            with open(output + name, "wb") as f:
                f.write(resp.content)

            count += 1

            print("Downloaded {}/{}".format(count, len(urls)))
        except:
            print("Failed to download url number {}".format(url[0]))

    t1 = time.time()
    print("Done with download, job took {} seconds".format(t1-t0))


def main():
    output_csv = "../../res/dataset/csv/urls.csv"

    with open("../secret", "r") as f:
        lines = f.readlines()

    key = lines[0].rstrip()
    secret = lines[2].rstrip()

    tag = sys.argv[1]
    max_count = int(sys.argv[2])

    if "dof" in tag:
        output_data = "../../res/dataset/y/"
    else:
        output_data = "../../res/dataset/x/"

    #if os.path.exists(output_csv):
    #    os.remove(output_csv)

    #get_urls(tag, key, secret, max_count, output_csv)

    put_images(output_csv, output_data)


if __name__ == '__main__':
    main()
