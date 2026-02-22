# tts_engine.py
import subprocess
import os
from config import DEFAULT_VOICE, INPUT_AUDIO

def generar_audio_base(texto: str, voice: str = DEFAULT_VOICE, output_path: str = INPUT_AUDIO):
    print(f"Generando base acústica para: '{texto}'")
    # Definimos una ruta temporal para el MP3 crudo
    temp_mp3 = "audios/temp/raw_tts.mp3"
    comando_tts = [
        "edge-tts", 
        "--text", texto, 
        "--voice", voice, 
        "--write-media", temp_mp3
    ]
    # Ejecutamos edge-tts de forma silenciosa
    subprocess.run(comando_tts, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # --- PASO 2: HUMANIZACIÓN CON FFMPEG ---
    print(f"🎛️ Humanizando audio (EQ + Compresión) para RVC...")
    comando_ffmpeg = [
        "ffmpeg", "-y", "-i", temp_mp3,
        "-af", "lowpass=8000,highpass=70,acompressor=threshold=-18dB:ratio=2",
        "-c:a", "pcm_s16le", output_path
    ]
    subprocess.run(comando_ffmpeg, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # --- PASO 3: LIMPIEZA ---
    if os.path.exists(temp_mp3):
        os.remove(temp_mp3)
        
    print("✅ Base acústica humanizada en formato WAV lista.")


    
    
    
    