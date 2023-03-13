from pytube import YouTube
from lameenc import Encoder 
from AudioManager import * 
import tempfile
from moviepy.editor import AudioFileClip

# Creates a temp dir
temp_dir = tempfile.TemporaryDirectory()
temp_path = temp_dir.name
video_url = input("Insert video URL: ")

is_wav = False
bitrate = None

while True:
    print("\nSelect audio quality:\n 1. Low (128kbps)\n 2. Medium (256kbps)\n 3. High (320kbps)\n 4. HiFi (WAV)\n")
    choice = int(input("Your choice: "))

    if choice == 1:
        bitrate = 128
        break

    elif choice == 2:
        bitrate = 256
        break

    elif choice == 3:
        bitrate = 320
        break

    elif choice == 4:
        is_wav = True
        break

# Creates instances of Youtube and Encoder
youtube = YouTube(video_url)
encoder = Encoder()

# Creates an AudioManager instance with the previous ones as parameters
audio_manager = AudioManager(youtube=youtube, encoder=encoder, temp_path=temp_path)
formatted_filename = audio_manager.get_formatted_filename()
wav_path = audio_manager.get_wav_path(formatted_filename)

# Converts the audio
webm_path = audio_manager.get_webm(formatted_filename)
webm_file = AudioFileClip(webm_path)
audio_manager.webm_to_wav(formatted_filename, webm_file, webm_path)

if is_wav is True:
    audio_manager.save_as_wav(formatted_filename, wav_path)
else:
    audio_manager.save_as_mp3(bitrate, formatted_filename)


print("Song converted successfully.")

# Closes the temp dir
temp_dir.cleanup()