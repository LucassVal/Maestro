import os
import importlib

# [EXTRACTOR] FACTORY v46.2 - GL
# Orchestrates all sensors in the LAB category.

class FabricaExtratores:
    @staticmethod
    def obter_extrator(caminho):
        """Returns the appropriate extractor class for a file extension."""
        ext = os.path.splitext(caminho)[1].lower()
        
        mapping = {
            ".pdf": "extrator_pdf_soldado_SRC_GL",
            ".docx": "extrator_docx_soldado_SRC_GL",
            ".xlsx": "extrator_xlsx_soldado_SRC_GL",
            ".rtf": "extrator_rtf_soldado_SRC_GL",
            ".log": "extrator_log_soldado_SRC_GL",
            ".zip": "extrator_archive_soldado_SRC_GL",
            ".msg": "extrator_email_soldado_SRC_GL",
            ".html": "extrator_html_soldado_SRC_GL",
            ".csv": "extrator_csv_soldado_SRC_GL",
            ".xml": "extrator_xml_soldado_SRC_GL",
            ".json": "extrator_json_soldado_SRC_GL",
            ".png": "extrator_imagem_soldado_SRC_GL",
            ".jpg": "extrator_imagem_soldado_SRC_GL",
            ".jpeg": "extrator_imagem_soldado_SRC_GL",
            ".webp": "extrator_imagem_soldado_SRC_GL",
            ".mp3": "extrator_audio_whisper_SRC_GL",
            ".txt": "extrator_txt_soldado_SRC_GL"
        }
        
        if ext in mapping:
            modulo_nome = mapping[ext]
            try:
                # Dynamic import to avoid circular dependencies and only load what is needed
                modulo = importlib.import_module(f"src.agentes.passivos.extratores.{modulo_nome}")
                # Conventional naming: class name is CamelCase version of filename without _SRC_GL
                # But to be safe, we'll try to find the class inside the module.
                for attr in dir(modulo):
                    if attr.startswith("Extrator") and attr != "ExtratorBase":
                        return getattr(modulo, attr)
            except Exception as e:
                print(f"[ERR] Factory failed to load {modulo_nome}: {e}")
                return DefaultExtractor
        
        return DefaultExtractor

class DefaultExtractor:
    def executar(self, dados):
        caminho = dados.get("caminho")
        try:
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                return {"status": "SUCCESS", "texto": f.read()[:5000]}
        except Exception as e:
            return {"status": "ERROR", "erro": str(e)}
