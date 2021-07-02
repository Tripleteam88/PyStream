from pytube import YouTube
from config import *

# read from file
def read_queue():
    '''
    Reads from text file of urls
    -----------
    Returns list of urls
    '''
    queue = []

    urls = open('urls.txt', 'r')
    queue = urls.readlines()
    urls.close()
    
    print('Reading urls...')

    return queue

def convert_queue(queue: list):
    '''
    Creates a list of youtube objects
    --------------------
    Returns list of youtube objects
    '''
    yt_list = []
    for i in range(len(queue)):
        yt_list.append(YouTube(queue[i]))
    
    print("Creating download queue.")

    return yt_list

def ready_queue(yt_list: list, audio_only=False):
    '''
    Identifies proper streams to download
    Either Audio only or just default (for now)
    ---------------
    Returns a list of stream objects to download
    '''
    print("Please wait while download streams are initialized...")

    streams = []
    for yt in yt_list:
        if audio_only == True:
            streams.append(yt.streams.get_audio_only())
        else:
            streams.append(yt.streams.first())

    return streams

def download_streams(streams: list):
    '''
    Downloads all the videos to a folder named "Videos"

    If the user has only downloaded the audio stream. It will download to audios instead. (WORK IN PROGRESS)
    -----------
    Returns nothing: Void
    '''

    print('Preparing to download streams...')
    i = 1
    for stream in streams:
        print(f'Download queue: {i}')
        stream.download('Videos')
        print(f'Download: {i} has finished!')
        i += 1

# Lists (used as parameters for next function)
queue = []
yt_list = []
streams = []

# Order of  use (how to use the downloader program)
q = read_queue()
yt_list = convert_queue(q)
streams = ready_queue(yt_list, audio_stream_only)
download_streams(streams)

# NOTE
# Implemented option to download video stream instead of just audio stream 
