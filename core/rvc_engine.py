# rvc_engine.py
import os
import glob
import torch

# --- PARCHE DE SEGURIDAD PYTORCH 2.6 ---
_original_load = torch.load
def _patched_load(*args, **kwargs):
    kwargs['weights_only'] = False
    return _original_load(*args, **kwargs)
torch.load = _patched_load
# ---------------------------------------

from rvc_python.infer import RVCInference
from config import RVC_CONFIG, MODEL_FOLDER

class Mikutor:
    def __init__(self):
        try:
            self.model_path = glob.glob(os.path.join(MODEL_FOLDER, "*.pth"))[0]
        except IndexError:
            raise FileNotFoundError(f"Error: No se encontró el archivo .pth en {MODEL_FOLDER}")

        print(f"Motor RVC Iniciado | Modelo: {os.path.basename(self.model_path)}")
        print(f"Hardware detectado: {torch.cuda.get_device_name(0)}")
        
        # Inicializar RVC con la configuración
        self.rvc = RVCInference(device=RVC_CONFIG["device"])
        self.rvc.load_model(self.model_path)
        self._aplicar_filtros()

    def _aplicar_filtros(self):
        if hasattr(self.rvc, 'set_f0_method'):
            self.rvc.set_f0_method(RVC_CONFIG["f0_method"])
            
        self.rvc.index_rate = RVC_CONFIG["index_rate"]
        self.rvc.protect = RVC_CONFIG["protect"]
        self.rvc.rms_mix_rate = RVC_CONFIG["rms_mix_rate"]
        # self.rvc.pitch = RVC_CONFIG["pitch"]
        self.rvc.f0_up_key = RVC_CONFIG["f0_up_key"]
        self.rvc.resample_sr = RVC_CONFIG["resample_sr"]

    def procesar_voz(self, input_audio: str, output_audio: str):
        print("Tomori está procesando el audio con calidad de estudio...")
        self.rvc.infer_file(input_audio, output_audio)
        print(f"¡Protocolo completado con éxito! Archivo listo: {output_audio}")
