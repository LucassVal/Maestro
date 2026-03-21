import os
import re

def load_codex_paths(codex_path):
    if not os.path.exists(codex_path):
        print(f"❌ Codex não encontrado em: {codex_path}")
        return set()
    
    with open(codex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrair todos os caminhos da coluna "Path" (entre `)
    # Padrão: | Name | `Path` | ...
    paths = set(re.findall(r'`([^`]+\.(?:py|ps1|iss|json|md))`', content))
    return paths

def scan_project_files(root_dir):
    extensions = ('.py', '.ps1', '.iss', '.json', '.md')
    files = set()
    
    # Pastas para ignorar
    ignore_dirs = ['.git', '.panda', '__pycache__', 'venv', '.vscode', '.idea', 'build', 'dist', 'node_modules']
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modificar dirnames in-place para ignorar pastas
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        
        for f in filenames:
            if f.endswith(extensions):
                # Ignorar arquivos sensíveis/temporários conforme .gitignore
                if any(ignore in f.lower() for ignore in ['lucas.json', 'desktop.ini']):
                    continue
                
                full = os.path.relpath(os.path.join(dirpath, f), root_dir)
                # Normalizar para barras normais (estilo linux/git)
                full = full.replace('\\', '/')
                files.add(full)
    return files

def main():
    codex_file = 'GENIO_FILE_REGISTRE_.md'
    print(f"🔍 Iniciando Phantom Finder v46.5...")
    
    codex_paths = load_codex_paths(codex_file)
    project_files = scan_project_files('.')
    
    # Arquivos que estão no projeto mas não no Codex
    missing_in_codex = project_files - codex_paths
    
    # Arquivos que estão no Codex mas não existem fisicamente
    ghosts_in_codex = codex_paths - project_files
    
    print(f"\n📊 Resumo da Auditoria:")
    print(f"   - Total no Codex: {len(codex_paths)}")
    print(f"   - Total no Projeto: {len(project_files)}")
    
    if missing_in_codex:
        print("\n⚠️  ARQUIVOS FANTASMAS (No Projeto, mas não no Codex):")
        for f in sorted(missing_in_codex):
            print(f"   - {f}")
    else:
        print("\n✅ Todos os arquivos físicos estão documentados.")
        
    if ghosts_in_codex:
        print("\n🛑 LINKS QUEBRADOS (No Codex, mas não existem no disco):")
        for f in sorted(ghosts_in_codex):
            print(f"   - {f}")
    else:
        print("\n✅ Todos os links do Codex são válidos.")

if __name__ == "__main__":
    main()
