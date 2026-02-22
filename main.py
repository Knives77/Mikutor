# main.py
import argparse
import subprocess
from config import INPUT_AUDIO, OUTPUT_AUDIO
from core.tts_engine import generar_audio_base
from core.rvc_engine import Mikutor

def convertir_a_mp3(wav_path: str, mp3_path: str):
    print(f"Comprimiendo archivo para envío: {mp3_path}")
    comando_ffmpeg = [
        "ffmpeg", "-y", "-i", wav_path, 
        "-b:a", "320k", mp3_path
    ]
    subprocess.run(comando_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("MP3 ligero generado con éxito.")

def main():
    parser = argparse.ArgumentParser(description="PROJECT: MIKUTOR")
    parser.add_argument("texto", help="El texto que  dirá")
    parser.add_argument("--lang", choices=["ja", "en", "es"], default="ja", help="Idioma de la voz base")
    parser.add_argument("--mp3", action="store_true", help="Generar también un archivo MP3 comprimido")
    
    args = parser.parse_args()

    # Mapeo de voces según el idioma elegido
    voces = {
        "ja": "ja-JP-NanamiNeural",
        "en": "en-US-AriaNeural",
        "es": "es-MX-DaliaNeural"
    }
    
    voz_seleccionada = voces[args.lang]

    # Ejecutar el pipeline modular
    generar_audio_base(args.texto, voice=voz_seleccionada)
    
    motor_rvc = Mikutor()
    motor_rvc.procesar_voz(INPUT_AUDIO, OUTPUT_AUDIO)
    
    # Compresión opcional si se solicita en la terminal
    if args.mp3:
        mp3_filename = OUTPUT_AUDIO.replace(".wav", ".mp3")
        convertir_a_mp3(OUTPUT_AUDIO, mp3_filename)

if __name__ == "__main__":
    main()
