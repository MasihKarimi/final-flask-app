import boto3


class HandwritingOCR:

    def __init__(self, documentName):
        self.documentName = documentName

    def ocr_handwriting(self):
        # Read document content
        with open(self.documentName, 'rb') as document:
            imageBytes = bytearray(document.read())
        # Amazon Textract client
        textract = boto3.client("textract", aws_access_key_id="AKIAVENFQTC3ETUZ2HNC",
                                aws_secret_access_key="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",
                                region_name="us-east-1")
        # Call Amazon Textract
        response = textract.detect_document_text(Document={'Bytes': imageBytes})
        # Print detected text
        text = []
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                print('\033[94m' + item["Text"] + '\033[0m')
                text_ =  item["Text"]
                text.append(text_)
        return text


# Document
path_file = (r'C:\Users\Oussama\PycharmProjects\textract\test3.jpg')
hw = HandwritingOCR(path_file)
hw.ocr_handwriting()
