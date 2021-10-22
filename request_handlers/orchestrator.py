import pandas as pd
from collections import Counter
import json
from OCR.ocr_handwriting import HandwritingOCR
from OCR.ocr_table import TableOCR


class orchestrator:

    def scan_ocr_handwriting(self, path_file):
        hw = HandwritingOCR(path_file)
        scan = hw.ocr_handwriting()
        return scan

    def scan_ocr_table(self, path_file):
        ot = TableOCR(path_file)
        scan = ot.ocr_table()
        result = scan.to_json(orient='records')
        return result



