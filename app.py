# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)
CORS(app)

@app.route('/get_transcript')
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'error': 'No video_id provided'}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = "\n".join([item['text'] for item in transcript])
        return jsonify({'transcript': full_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
