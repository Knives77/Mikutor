# MIKUTOR

Sistema modular de inferencia de voz (Text-to-Speech + Retrieval-based Voice Conversion) acelerado por GPU, diseñado para generar audios de alta fidelidad con perfiles acústicos específicos.

## Arquitectura

El protocolo utiliza un pipeline automatizado de dos fases:

1. **Síntesis acústica base:** Utiliza `edge-tts` para generar la fonética y cadencia estructural nativa (japonés, inglés, español).
2. **Transposición de timbre:** Un motor RVC impulsado por PyTorch aplica el modelo de voz sobre el audio base utilizando el algoritmo determinista `harvest` para preservar las micro-variaciones de frecuencia en alta resolución (48kHz).

## Requisitos del sistema

- Entorno Linux (optimizado para Arch Linux)
- GPU NVIDIA compatible con procesamiento CUDA (probado en RTX 3050 Ti)
- `uv` (gestor ultrarrápido de paquetes de Python)
- `ffmpeg` (para compresión de salida)

## Despliegue del entorno

1. **Clonar el código fuente:**

   ```bash
   git clone git@github.com:Knives77/Mikutor.git
   cd Mikutor
   ```

2. **Restaurar los pesos neuronales (Data Backup):**
   Los modelos `.pth` están excluidos del control de versiones. Descarga la carpeta `models/` desde tu almacenamiento en la nube (Google Drive) y colócala en la raíz del proyecto, asegurando esta estructura:

   ```
   models/Tomori_v2/Tomori.pth
   ```

3. **Ejecución y resolución de dependencias:**
   El gestor `uv` instalará automáticamente las librerías necesarias en la primera ejecución.

## Interfaz de línea de comandos (CLI)

El orquestador principal (`main.py`) acepta comandos directos para facilitar la generación de diálogos.

**Sintaxis base:**

```bash
uv run python main.py "Texto a procesar" --lang [ja|en|es] [--mp3]
```

**Ejemplos de uso:**

- Práctica de conversación en inglés (nivel B1):

  ```bash
  uv run python main.py "My name is Teto and I am testing this pipeline." --lang en
  ```

- Renderizado de mensaje en japonés con compresión web lista para envío:
  ```bash
  uv run python main.py "こんにちは、ソフィア。大好きだよ。" --lang ja --mp3
  ```

---

Desarrollado para automatización de doblaje y proyectos web.
