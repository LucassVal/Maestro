import os
import re

def parse_codex_endpoints(codex_path):
    if not os.path.exists(codex_path):
        return []
    
    with open(codex_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    results = []
    # Regex para capturar Path e Endpoint da tabela markdown
    # Exemplo: | Name | `src/path.py` | Function | `endpoint` | ...
    # Ou simplesmente procurar por pares de backticks na mesma linha
    for line in lines:
        if '|' in line and '`' in line:
            parts = re.findall(r'`([^`]+)`', line)
            if len(parts) >= 2:
                # O primeiro backtick costuma ser o path, o segundo o endpoint ou arsenal
                # Mas no Codex v46.4, as colunas são: Path (2), SOTA Function (3), API/Endp (4)
                # Vamos tentar ser mais espertos com o split da tabela
                cols = [c.strip() for c in line.split('|')]
                if len(cols) > 5:
                    path = re.sub(r'^`|`$', '', cols[2]) # Coluna do Path
                    endpoint = re.sub(r'^`|`$', '', cols[4]) # Coluna do Endpoint
                    
                    if '.' in path and endpoint and endpoint != 'API / Endp.':
                        results.append((path, endpoint))
    return results

def verify_endpoint(path, endpoint):
    if not os.path.exists(path):
        return False, "Arquivo não encontrado"
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Procura por definições de funções, métodos ou chamadas específicas
    # Ex: def executar, class ..., etc.
    if endpoint in content:
        return True, "OK"
    else:
        return False, f"Endpoint '{endpoint}' não encontrado no código"

def main():
    codex_file = 'GENIO_FILE_REGISTRE_.md'
    print(f"🛡️ Iniciando Endpoint Auditor v46.5...")
    
    mappings = parse_codex_endpoints(codex_file)
    
    errors = []
    passed = 0
    
    for path, endpoint in mappings:
        # Normalizar path
        path = path.replace('/', os.sep)
        
        success, msg = verify_endpoint(path, endpoint)
        if success:
            passed += 1
        else:
            errors.append(f"{path} -> {msg}")
            
    print(f"\n📊 Resultado da Auditoria de API:")
    print(f"   - Total de Endpoints verificados: {len(mappings)}")
    print(f"   - Sucesso: {passed}")
    print(f"   - Falhas: {len(errors)}")
    
    if errors:
        print("\n❌ DISCREPÂNCIAS DETECTADAS:")
        for err in errors:
            print(f"   - {err}")
    else:
        print("\n✅ Todos os endpoints documentados foram validados no código fonte.")

if __name__ == "__main__":
    main()
