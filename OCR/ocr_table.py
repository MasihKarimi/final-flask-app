import boto3
from OCR.trp import Document
import pandas as pd

class TableOCR:

    def __init__(self, documentName):
        self.documentName = documentName

    def ocr_table(self):
        # Amazon Textract client
        textract = boto3.client("textract", aws_access_key_id="AKIAVENFQTC3ETUZ2HNC",
                                aws_secret_access_key="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",
                                region_name="us-east-1")
        # Read document content
        with open(self.documentName, "rb") as document:
            response = textract.analyze_document(
                Document={
                    'Bytes': document.read(),
                },
                FeatureTypes=["TABLES"])
        doc = Document(response)
        for page in doc.pages:
            #  tables
            for table in page.tables:
                ca = []
                for r, row in enumerate(table.rows):
                    if r == 1:
                        lst = []
                        for c, cell in enumerate(row.cells):
                            lst.append(cell.text)
                    if r > 1:
                        ka = []
                        for c, cell in enumerate(row.cells):
                            ka.append(cell.text)
                        ca.append(ka)
        df = pd.DataFrame(ca, columns=lst)
        return df


# Document
path_file = (r'C:\Users\Oussama\PycharmProjects\textract\test5.jpg')
hw = TableOCR(path_file)
hw.ocr_table()


