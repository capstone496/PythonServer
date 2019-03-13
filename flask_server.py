from pathlib import Path

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from serve_prediction import predict, get_tensors_for_prediction, spectrogram, graph_file

LABELS = dict(zip(range(8), ['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']))
graph, image_buffer_input, prediction, keep_prob = get_tensors_for_prediction(graph_file)

app = Flask(__name__)


@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "Root"


@app.route('/api/predict', methods=['POST'])
def get_emotion_prediction():
    f = request.files['file']

    audio_filename = secure_filename(f.filename)
    audio_dir = Path('received_audio')

    audio_dir.mkdir(exist_ok=True)
    audio_filename = str(audio_dir / Path(audio_filename))

    f.save(audio_filename)

    predicted_emotion = predict(graph,
                                image_buffer_input,
                                prediction,
                                keep_prob,
                                spectrogram(audio_filename))

    return jsonify({"predictedEmotion": LABELS[predicted_emotion]})


# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)