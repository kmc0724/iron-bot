# https://github.com/JHni2

import yt_dlp
import requests
import json
import iron_token

default_num_search = 1
opts = {
    'extract-audio': True,
    'format': 'bestaudio',
    'outtmpl': '%(title)s.mp3'
}

def search_api(keyword, num_search = default_num_search):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "maxResults": default_num_search,
        "q": keyword,
        "type": "video",
        "key": iron_token.YOUTUBE_API_KEY
    }
    resp = requests.get(url, params = params)
    resp.encoding = "utf-8"
    resp_data = resp.json()
    return resp_data


def download(link):
    dl = yt_dlp.YoutubeDL(opts)
    res = dl.extract_info(link)
    return dl.prepare_filename(res)
