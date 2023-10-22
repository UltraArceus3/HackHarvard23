from whisper_jax import FlaxWhisperPipline
import jax.numpy as jnp
import av
import numpy as np
from moviepy.editor import VideoFileClip
import os

def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")


convert_video_to_audio_moviepy("../week02 01 [nFjGsUayqBc].mp4", )

pipeline = FlaxWhisperPipline("openai/whisper-large-v2", dtype=jnp.bfloat16, batch_size=16)

# transcribe and return timestamps
# outputs = pipeline("audio.mp3",  task="transcribe", return_timestamps=True)
outputs = pipeline("../week02 01 [nFjGsUayqBc].mp3",  task="transcribe", return_timestamps=True)
print(outputs)
