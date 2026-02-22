# config.py
import os

# Rutas de archivos
MODEL_FOLDER = "models/gumi"
INPUT_AUDIO = "audios/temp/base_audio.wav"
OUTPUT_AUDIO = "audios/output/result.wav"

# Configuración de Edge-TTS
DEFAULT_VOICE = "en-US-AnaNeural"

RVC_CONFIG = {
    "device": "cuda:0",
    "f0_method": "crepe",     # <-- Algoritmo neuronal más suave
    "index_rate": 0.5,        # <-- Reducido para evitar artefactos
    "protect": 0.1,           
    "rms_mix_rate": 0.3,
    "pitch": 0,             
    "f0_up_key": 0,         
    "resample_sr": 48000      # Puedes probar 48000 si crepe te lo pide
}