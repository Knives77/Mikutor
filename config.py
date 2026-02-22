# config.py
import os

# Rutas de archivos
MODEL_FOLDER = "models/Tomori_v2/"
INPUT_AUDIO = "audios/temp/base_audio.mp3"
OUTPUT_AUDIO = "audios/output/tomori_practice_b1.wav"

# Configuración de Edge-TTS
DEFAULT_VOICE = "ja-JP-NanamiNeural"

# Hiperparámetros Acústicos de RVC
RVC_CONFIG = {
    "device": "cuda:0",
    "f0_method": "rmvpe",
    "index_rate": 0.0,
    "protect": 0.33,
    "rms_mix_rate": 0.25,
    "pitch": 2,
    "f0_up_key": 2,
    "resample_sr": 40500 # Corregido a la tasa nativa del modelo
}
