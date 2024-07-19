from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if (not text_to_analyze):
        return jsonify({'error': 'No text provided'}), 400

    try:
        emotion_text = emotion_detector(text_to_analyze)
        print(emotion_text)
        return emotion_text

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
