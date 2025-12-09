import os
import unittest



from santas_tavern.cli.generate import generate_adv
from santas_tavern.models import AdventureGenerationParams
from judge import llm_as_a_judge
from pathlib import Path

class AdventureTestCase(unittest.TestCase):
    def test_generate_adventure_direct(self):
        output_dir = os.path.abspath("./") + "output_test"
        os.makedirs(output_dir, exist_ok=True)

        params = AdventureGenerationParams(
            party_level=3,
            party_size=4,
            tone="cozy",
            duration_hours=3,
            output_dir=str(output_dir)
        )
        generate_adv(str(output_dir),params)
        output_path = Path(output_dir)
        files = list(output_path.iterdir())
        assert files, "Nessun file generato nella cartella di output"
        assert any(f.suffix == ".json" for f in files), "File JSON non trovato nella cartella di output"
        assert any(f.suffix == ".md" for f in files), "File Markdown non trovato nella cartella di output"
        md_file = next(f for f in files if f.suffix == ".md")
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            verdict = llm_as_a_judge(content)
            assert verdict.result, f"L'avventura non è stata giudicata valida: {verdict.feedback}"


if __name__ == '__main__':
    unittest.main()
