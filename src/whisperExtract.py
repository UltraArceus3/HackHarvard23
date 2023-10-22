import whisper
import subprocess


def extract_audio(video_file, output_file):
    # Extract audio from video
    cmd = ["ffmpeg", "-i", video_file, "-ab", "160k", "-ac", "2", "-ar", "44100", "-vn", output_file]
    subprocess.call(cmd)


# Use whisper to convert audio to text
def speech_to_text(audio_file, output_file):
    model = whisper.load_model("base")
    transcript = model.transcribe(audio_file)

    with open(output_file + "_full.txt", "w") as f:
        f.write(transcript['text'])

    with open(output_file + "_segments.txt", "w") as f:
        header = "id\tseek\tstart\tend\ttext"
        f.write(header + "\n")
        for line in transcript['segments']:
            '''
            {'id': 0, 'seek': 0, 'start': 0.0, 'end': 6.16, 
                'text': " Today we're making this easy five minute no-y's pizza. I'm going to show you two versions,", 
                'tokens': [50364, 2692, 321, 434, 1455, 341, 1858, 1732, 3456, 572, 12, 88, 311, 8298, 13, 286, 478, 516, 
                            281, 855, 291, 732, 9606, 11, 50672], 
                'temperature': 0.0, 'avg_logprob': -0.25480910142262775, 'compression_ratio': 1.5916666666666666, 
                'no_speech_prob': 0.024740071967244148}
            '''

            f.write(str(line['id']) + "\t" + 
                    str(line['seek']) + "\t" + 
                    str(line['start']) + "\t" + 
                    str(line['end']) + "\t" + 
                    line['text'] + "\n")