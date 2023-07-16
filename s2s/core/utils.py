import os
import requests
from urllib.parse import urlparse

def get_binary(url, decode=None):
    """Get binary data from URL"""
    data = bytes()
    for chunk in requests.get(url, stream=True):
        data += chunk

    if decode == None:
        return data
    else:
        return data.decode("utf-8")

def sort_array_by_other(array1, array2):
    # Zip the two arrays into tuples
    zipped = zip(array2, array1)

    # Sort the tuples based on the values from the second array
    sorted_tuples = sorted(zipped)

    # Extract the sorted values from the first array
    sorted_array1 = [t[1] for t in sorted_tuples]

    return sorted_array1

def parse_string(input_string):
    # Check if the input string is a valid URL
    parsed_url = urlparse(input_string, allow_fragments=True)
    if parsed_url.scheme and parsed_url.netloc:
        # It's a URL
        return {
            "type": "url",
            "url": input_string,
        }
    else:
        # It's a file path
        return {
            "type": "file",
            "path": input_string,
            "dirname": os.path.dirname(input_string),
            "basename": os.path.basename(input_string),
            "abspath": os.path.abspath(input_string),
        }


def get_key(key_url):
    if key_url["type"] == "file":
        with open(key_url["abspath"], "r") as playlist:
            return playlist.read()
    else:
        return get_binary(key_url["url"])


def get_m3u8(m3u8_url):
    if m3u8_url["type"] == "file":
        with open(m3u8_url["abspath"], "r") as playlist:
            return playlist.read()
    else:
        return get_binary(m3u8_url["url"], decode=True)


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i : i + n]
