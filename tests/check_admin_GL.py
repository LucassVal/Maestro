# -*- coding: utf-8 -*-
"""
check_admin_GL.py Verificador de Soberania v44.3.
Valida se o processo atual possui direitos de Administrador no Windows.
""" import os
import ctypes
import sys def is_admin(): try: return ctypes.windll.shell32.IsUserAnAdmin() != 0 except: return False def check_status(): print("\n" + "="*50) print("[GUARD] CHECK DE SOBERANIA - G NIO LLM v44.3") print("="*50) if is_admin(): print("[OK] STATUS: ADMINISTRADOR ATIVO") print("[BOOST] O organismo tem permiss o total para operar.") else: print("[ERR] STATUS: USU RIO PADR O (RESTRITO)") print("[WARN] Aviso: O Windows bloquear o Python e os Daemons.") print("[IDEA] Sugest o: Reinicie o Host (VS Code) como Administrador.") print("="*50 + "\n") if __name__ == "__main__": check_status()
