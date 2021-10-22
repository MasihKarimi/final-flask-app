from flask_restplus import Resource
from request_handlers.orchestrator import orchestrator
from flask import jsonify, request, abort
from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app=app)


@api.param('path_file', 'image_path', _in='formData')
@api.route('/ocrscanhandwriting/')
class Ocrhandwriting(Resource):
    def post(self):
        path_file = request.form.get('path_file')
        orc = orchestrator()
        result = orc.scan_ocr_handwriting(path_file)
        return jsonify(result=result)


@api.param('path', 'table_path', _in='formData')
@api.route('/ocrscantable/')
class Ocrtable(Resource):
    def post(self):
        path = request.form.get('path')
        orc = orchestrator()
        result = orc.scan_ocr_table(path)
        if result is None:
            abort(401)
        else:
            return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
