import unittest
import santas_tavern.rag as rag


class RagTestCase(unittest.TestCase):
    def test_lore(self):
        rag.run_import_pipeline("tests/lore_test_data")
        names = rag.run_query_pipeline(
            "Elenca i nomi dei personaggi principali menzionati nei documenti e la loro Storia"
        )
        print(names)
