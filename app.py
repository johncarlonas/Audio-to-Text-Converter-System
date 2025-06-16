import os
import re
import tempfile
import subprocess

import whisper
import librosa
import soundfile as sf
from flask import Flask, request, send_file, render_template, Response

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
TEXT_FOLDER = "texts"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEXT_FOLDER, exist_ok=True)

model = whisper.load_model("base")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return "No audio file uploaded", 400

    file = request.files['audio']
    filename = request.form.get('filename', 'transcript').strip()
    filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', filename)

    audio_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(audio_path)

    # Convert to WAV to ensure compatibility
    wav_path = convert_to_wav(audio_path)

    try:
        formatted_text = silence_chunk_transcription(wav_path)
    except Exception as e:
        print("Transcription error:", e)
        return f"Error during transcription: {str(e)}", 500

    text_path = os.path.join(TEXT_FOLDER, f"{filename}.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(formatted_text)

    
    return Response(formatted_text, mimetype='text/plain')


@app.route('/download')
def download():
    filename = request.args.get("filename", "")
    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', filename)
    text_path = os.path.join(TEXT_FOLDER, f"{safe_name}.txt")

    if os.path.exists(text_path):
        return send_file(text_path, as_attachment=True)
    else:
        return "File not found", 404


def convert_to_wav(input_path):
    wav_path = os.path.splitext(input_path)[0] + ".wav"
    subprocess.run(
        ["ffmpeg", "-y", "-i", input_path, wav_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return wav_path


def silence_chunk_transcription(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    intervals = librosa.effects.split(y, top_db=30)

    all_segments = []

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, (start, end) in enumerate(intervals):
            chunk_path = os.path.join(tmpdir, f"chunk{i}.wav")
            sf.write(chunk_path, y[start:end], sr)

            result = model.transcribe(chunk_path)
            if 'segments' in result:
                all_segments.extend(result['segments'])
            else:
                all_segments.append({'text': result['text']})

    return format_transcript(all_segments)


def format_transcript(segments):
    transcript = ""
    for seg in segments:
        text = seg['text'].strip()
        text = text.replace("[inaudible]", "____")

        for filler in ["you know", "like", "I mean", "so", "actually", "basically"]:
            text = re.sub(rf"\b{filler}\b", "", text, flags=re.IGNORECASE)

        for utterance in ["uh", "um", "uh-huh", "mm-hmm"]:
            text = re.sub(rf"\b{utterance}\b", "", text, flags=re.IGNORECASE)

        if text.endswith(","):
            text += "..."

        transcript += f"\n\n{text}"

    return transcript.strip()


if __name__ == '__main__':
    app.run(debug=True)
