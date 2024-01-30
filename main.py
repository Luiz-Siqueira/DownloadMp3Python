from pytube import YouTube
from pathlib import Path
from os import *
from pywebio.input import *
from pywebio.output import *
from youtubesearchpython import VideosSearch

def getVideoLink():
        videoTitulo = input("Informe o link do video: ")
        videosSearch = VideosSearch(videoTitulo, limit = 2)
        videoResult = videosSearch.result()
        return 'https://youtu.be/' + videoResult["result"][0]["link"].split("watch?v=")[1]

def video_download():
    while True:
        linkVideo = getVideoLink()
        print(linkVideo)
        if linkVideo.split("//")[0] == "https:":
            # put_text("Fazendo o download do video....".title()).style('color: red; font-size: 50px')
            video = YouTube(linkVideo)
            path_to_download = (r"d:projetos")
            video.streams.get_audio_only().download(path_to_download)
         
            # put_text("Video baixado com sucesso...".title()).style('color: blue; font-size: 50px')

if __name__ == "__main__":
    video_download()