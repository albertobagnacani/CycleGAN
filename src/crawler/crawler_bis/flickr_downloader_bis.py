# if you want to insert your apikey in source code
from crawler.crawler_bis.flickrDownloader import *

with open("../../secret", "r") as f:
    lines = f.readlines()

key = lines[0].rstrip()
api_key = key
license_id = 10  # "using public domain mark" license

task = 2
n_images = 6000

query = "portrait -blackandwhite -BW -monochrome -animal -cat -dog -bird -flower"
query2 = r"selfie -blackandwhite -BW -monochrome -animal -cat -dog -bird -flower"

camera = r'&camera=apple%2Fiphone_7'

if __name__ == "__main__":
    if task == 1 or task == 3:
        flickr_photos_downloader(api_key,
                                 n_images=n_images,
                                 query_text=query,
                                 tag_mode=FlickrTagMode.any,
                                 image_size=FlickrImageSize.longedge_1600,
                                 content_type=FlickrContentType.photos,
                                 media=FlickrMedia.photos,
                                 download_path="bokeh_downloads",
                                 save_filename_prefix="bokeh_downloaded_",
                                 forced_extension=None,
                                 verbose=True,
                                 ignore_errors=False,
                                 license_id=license_id)

    if task == 2 or task == 3:
        flickr_photos_downloader(api_key,
                                 n_images=n_images,
                                 query_text=query2,
                                 tag_mode=FlickrTagMode.any,
                                 image_size=FlickrImageSize.longedge_1600,
                                 content_type=FlickrContentType.photos,
                                 media=FlickrMedia.photos,
                                 download_path="../iphone_downloads",
                                 save_filename_prefix="iphone_downloaded_",
                                 forced_extension=None,
                                 verbose=True,
                                 ignore_errors=False,
                                 license_id=license_id,
                                 camera=camera)
