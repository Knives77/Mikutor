# tts_engine.py
import subprocess
from config import DEFAULT_VOICE, INPUT_AUDIO

def generar_audio_base(texto: str, voice: str = DEFAULT_VOICE, output_path: str = INPUT_AUDIO):
    print(f"Generando base acústica para: '{texto}'")
    comando_tts = [
        "edge-tts", 
        "--text", texto, 
        "--voice", voice, 
        "--write-media", output_path
    ]
    # Ejecutamos edge-tts de forma silenciosa
    subprocess.run(comando_tts, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Base acústica generada.")
