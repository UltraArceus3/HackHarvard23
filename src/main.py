import whisperExtract
import llamaSum

if __name__ == "__main__":
    vid = "video/pizza.mp4"
    data_path = "data/"
    audio_file = data_path + "audio/pizza.wav"
    output_file = data_path + "output/pizza"

    print("extracting audio...")
    whisperExtract.extract_audio(vid, audio_file)

    print("transcribing audio...")
    whisperExtract.speech_to_text(audio_file, output_file)
