import re 
import os
import shutil 
import wave
import numpy as np
from view import save_file
from http.client import IncompleteRead
import time

class AudioManager:

    def __init__(self, youtube, encoder, temp_path):
        self.youtube = youtube
        self.encoder = encoder
        self.temp_path = temp_path



    def get_formatted_filename(self) -> str:

        # Format the file name. This is done because otherwise the moviepy lib will throw an exception.
        formatted_filename = re.sub(r'[<>\\/:|"*?]', '', self.youtube.title)
        return formatted_filename
    
    def get_wav_path(self, formatted_filename) -> str:
        wav_path = f"{self.temp_path}\\{formatted_filename}.wav"
        return wav_path

    def get_webm(self, formatted_filename):
        yt = self.youtube
        
        # Choose the higher audio quality
        video = yt.streams.filter(only_audio=True).order_by('abr').last()

        for i in range(3):
            # Downloads the raw audio in .webm format
            try:
                print('Downloading file...')
                video.download(output_path=self.temp_path, filename=f"{formatted_filename}.webm")
            except IncompleteRead:
                if i == 2:
                    print("Error downloading.")
                    self.temp_path.cleanup()
                continue
            break
        webm_path = f"{self.temp_path}\\{formatted_filename}.webm"
        return webm_path

    # Converts the .webm file into a .wav
    def webm_to_wav(self, formatted_filename, webm_file, webm_path):
        start_time = time.time()
        print('Starting webm_to_wav()')
        print('Writing audio file')
        webm_file.write_audiofile(f'{formatted_filename}.wav')
        print('Removing webm file')
        os.remove(webm_path)
        audio_path = f"{formatted_filename}.wav"
        shutil.move(audio_path, self.temp_path)
        print('Finished webm_to_wav()')
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Total execution time: {execution_time:.2f} seconds')




    def save_as_mp3(self, bitrate, formatted_filename):
            wav_path = f"{self.temp_path}\\{formatted_filename}.wav"
            with wave.open(wav_path, "rb") as wave_file:
                # Gets the parameters from the .WAV file
                channels = wave_file.getnchannels()
                framerate = wave_file.getframerate()
                num_frames = wave_file.getnframes()

                # Reads the audio data from the .WAV
                pcm_data = wave_file.readframes(num_frames)

            # Converts non-interleaved PCM data to interleaved
            pcm_array = np.frombuffer(pcm_data, dtype=np.int16)
            interleaved_pcm_array = np.empty_like(pcm_array)
            interleaved_pcm_array[::2] = pcm_array[::channels]
            interleaved_pcm_array[1::2] = pcm_array[1::channels]
            
            # Encode audio to MP3
            self.encoder.set_channels(channels)
            self.encoder.set_bit_rate(bitrate)
            self.encoder.set_in_sample_rate(framerate)
            self.encoder.set_quality(2)
            mp3_data = self.encoder.encode(interleaved_pcm_array.tobytes())
            self.encoder.flush()
            audio_extension = ".mp3"
            # Asks the user where to save the file
            save_file(formatted_filename=formatted_filename, audio_extension=audio_extension, file_data=mp3_data)
            os.remove(wav_path)


    def save_as_wav(self, formatted_filename, wav_path):
            with open(wav_path, 'rb') as fd:
                wav_file = fd.read()
            audio_extension = ".wav"
            save_file(audio_extension=audio_extension, formatted_filename=formatted_filename, file_data=wav_file)
            os.remove(wav_path)