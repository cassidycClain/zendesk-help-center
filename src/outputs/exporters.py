thonpython
import json
import logging
from pathlib import Path

class JsonExporter:
    @staticmethod
    def export(data, output_filename: str):
        out_path = Path(output_filename)
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Exported {len(data)} records to {out_path}")
        except Exception as e:
            logging.error(f"Failed to write output: {e}")