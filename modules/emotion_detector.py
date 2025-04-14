import librosa
import numpy as np

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40).T, axis=0)
    return mfccs

def fake_emotion_classifier(audio_path):
    # For now, return fake output (simulate behavior)
    # Later, plug in a trained ML model (SVM, etc.)
    print(f"🎧 [Mock] Analyzing audio at: {audio_path}")
    return "Calm"
