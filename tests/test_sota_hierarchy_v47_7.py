import unittest
import sys
import os

# Ajuste de path para importar do src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agentes.passivos.classificador_roteamento_SRC_GL import ClassificadorPrompts
from src.core.kernel_genio_CORE_GL import carregar_manifesto

class TestSotaHierarchyV47_7(unittest.TestCase):
    def setUp(self):
        self.classifier = ClassificadorPrompts()

    def test_simple_goes_to_ambassador(self):
        """Valida que comandos triviais são roteados para o Embaixador."""
        prompt = "Que horas são?"
        target = self.classifier.triage_complexity(prompt)
        self.assertEqual(target, "ambassador")

    def test_complex_goes_to_high_command(self):
        """Valida que missões e scripts são roteados para o Alto Comando."""
        prompt = "Crie um script automotor para backup do Codex."
        target = self.classifier.triage_complexity(prompt)
        self.assertEqual(target, "high_command")

    def test_ambassador_read_only_status(self):
        """Valida se o manifesto do Embaixador está marcado como READ_ONLY."""
        manifest_path = "config/mcp/tier3_ambassador_MCP_GL.json"
        manifest = carregar_manifesto(manifest_path)
        self.assertIsNotNone(manifest)
        self.assertEqual(manifest.get("mcp_access"), "READ_ONLY")

    def test_high_command_full_access_status(self):
        """Valida se o manifesto do Alto Comando está marcado como FULL_ACCESS."""
        manifest_path = "config/mcp/tier1_high_command_MCP_GL.json"
        manifest = carregar_manifesto(manifest_path)
        self.assertIsNotNone(manifest)
        self.assertEqual(manifest.get("mcp_access"), "FULL_ACCESS")

    def test_routing_permission_check(self):
        """Simula o roteamento e a verificação de permissão."""
        prompt = "Explique como funciona o sensor de temperatura."
        target_slug, config = self.classifier.rotear(prompt)
        
        self.assertEqual(target_slug, "ambassador")
        # Verifica se o classificador reconheceu a permissão no manifesto
        self.assertTrue(self.classifier.has_read_only_permission("ambassador"))

if __name__ == "__main__":
    unittest.main()
