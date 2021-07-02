import os
from moviepy.editor import *
from config import *

# Create list of video file names
mp4_filenames = os.listdir('Videos')

# Convert all file names to strings before using
for i in range(len(mp4_filenames)):
    mp4_filenames[i] = str(mp4_filenames[i])
    
# Create list of mp3 files
mp3_filenames = []
for filename in mp4_filenames:
    mp3_filenames.append(filename.replace('.mp4','.mp3'))

# Create list of mp4 and mp3 file paths
mp3_filepaths = []
mp4_filepaths = []
for i in range(len(mp3_filenames)):
    file_path = os.path.join(os.getcwd(), 'Videos', mp4_filenames[i])
    mp4_filepaths.append(file_path)

    file_path = os.path.join(os.getcwd(), 'Audios', mp3_filenames[i])
    mp3_filepaths.append(file_path)

# Use moviepy to convert files
# Create audio clips then write audio from each one to audio folder
if audio_stream_only:
    # Executes if user has only downloaded audio streams (although this may be pointless since the file extensions could just be changed to mp3 in this case)
    for i in range(len(mp4_filepaths)):
        AudioClip = AudioFileClip(mp4_filepaths[i])
        AudioClip.write_audiofile(mp3_filepaths[i])
        AudioClip.close()
else:
    # Executes if the user has chosen to download the video stream as well (necessary) 
    for i in range(len(mp4_filepaths)):
        VideoClip = VideoFileClip(mp4_filepaths[i])
        AudioClip = VideoClip.audio
        AudioClip.write_audiofile(mp3_filepaths[i])
        AudioClip.close()

#TODO:
# Make this work with mp4 files that have actual video streams not just audio streams
# Might want to use a try / catch or just have it check what option the user chose for conversion