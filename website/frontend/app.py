from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    # Replace these with your video URLs
    video_urls = [
        "pizza.mp4",
        "video2.mp4",
        "video3.mp4"
    ]

    # Replace these with your transcription text
    transcriptions = [
        "Transcription 1",
        "Transcription 2",
        "Transcription 3"
    ]



    return render_template('index.html', video_urls=video_urls, transcriptions=transcriptions)

if __name__ == '__main__':
    app.run(debug=True)