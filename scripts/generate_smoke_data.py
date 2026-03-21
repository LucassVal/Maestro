import os
from pathlib import Path

def generate_smoke_data():
    base_dir = Path("tests/data_smoke")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Textos e Códigos
    files = {
        "sample.txt": "Gênio LLM SOTA Validation Test.",
        "sample.py": "def hello(): print('SOTA Active')",
        "sample.json": '{"status": "active", "version": "46.2"}',
        "sample.yaml": "version: 46.2\nstatus: active",
        "sample.csv": "id,name,status\n1,Genio,SOTA",
        "sample.sql": "SELECT * FROM agents WHERE status = 'SOTA';",
        "sample.html": "<html><body><h1>Genio LLM</h1></body></html>",
        "sample.xml": "<genio><status>SOTA</status></genio>",
        "sample.log": "2026-03-20 INFO: System stabilized in SOTA mode.",
        "sample.rtf": "{\\rtf1\\ansi Genio LLM RTF Test}",
    }
    
    # Binários (Stubs)
    binary_extensions = [
        "pdf", "docx", "xlsx", "pptx", "jpg", "png", "zip", "tar.gz"
    ]
    # Audio (8 tipos)
    audio_extensions = [
        "mp3", "wav", "ogg", "flac", "aac", "m4a", "aiff", "wma"
    ]
    # Video (8 tipos)
    video_extensions = [
        "mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "mpeg"
    ]
    
    for name, content in files.items():
        with open(base_dir / name, "w", encoding="utf-8") as f:
            f.write(content)
            
    for ext in binary_extensions + audio_extensions + video_extensions:
        filename = f"sample.{ext}"
        with open(base_dir / filename, "wb") as f:
            f.write(b"STUB_DATA_SOTA_" + ext.encode())
            
    print(f"Smoke data generated successfully for {len(files) + len(binary_extensions) + len(audio_extensions) + len(video_extensions)} formats.")

if __name__ == "__main__":
    generate_smoke_data()
