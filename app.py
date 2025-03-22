from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 허용 (웹 연동용)

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
    app.run()
